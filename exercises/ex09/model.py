"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730249754"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_point) -> int:
        """Returns the distance between the Point this function is called on and the other passed in as parameter."""
        x_dist = (other_point.x - self.x)**2   # is the second point's x and y subtracted from self's x and y, or vise versa?
        y_dist = (other_point.y - self.y)**2
        return sqrt(x_dist + y_dist)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self):   # automatically gets called by the view controller (in a loop)
        """Update the state of teh simulation by one time step."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self):
        """Assigns the INFECTED constant to the sickness attribute of the Cell the function is called on."""
        self.sickness = constants.INFECTED 

    def immunize(self): 
        """Assigns the IMMUNE constant to the sickness attribute of the Cell the function is called on."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Returns True when the cell's sickness attribute is equal to VULNERABLE and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns True when cell's sickness attribute is equal to INFECTED and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Returns 'gray' for cells with vulnerable sickness attribute and 'red' for cells with infected sickness attributes."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "yellow"

    def contact_with(self, other_cell):
        """If one of these cells is infected, and the other is still vulnerable, then the vulnerable cell will become infected."""
        if self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()

    def is_immune(self) -> bool:
        """Returns boolean state of whether or not a cell's sickness attribute is equal to IMMUNE."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initial_infected: int, initial_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if initial_infected >= cells or initial_infected <= 0:
            raise ValueError("Some number of the cells must begin infected.")
        if initial_immune >= cells or initial_immune < 0:
            raise ValueError("Some number of the cells must begin immunized.")
        for _ in range(0, cells - initial_infected - initial_immune):   # _ replaces an otherwise unused and thus unamed variable (e.g. i)
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        # create the initial infected cells 
        for _ in range(0, initial_infected):   # _ replaces an otherwise unused and thus unamed variable (e.g. i)
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.contract_disease()
            self.population.append(cell)
        # create the initial immune cells
        for _ in range(0, initial_immune):   # _ replaces an otherwise unused and thus unamed variable (e.g. i)
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""   # each round, it asks cell object to update itself via the Cell `tick` method
        self.time += 1
        for cell in self.population: 
            cell.tick()
            self.enforce_bounds(cell)   # even time model updates each cell, then we will enforce the model's bounds by making sure it didnt get placed too far out
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        # randdom() returns a random float between 0 nad 1 (non-inclusive of 1)
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_WIDTH - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:   # If this cell is past our boundary of 400, 
            cell.location.x = constants.MAX_X   # stop the cell right at the 400 boundary
            cell.direction.x *= -1.0   # redirect the cell in the negative (left) direction of the x-axis 
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1   # redirect the cell in the postive (right) direction of the x-axis
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1   # redirect the cell in the negative (down) direction of the y-axis
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1   # redirect cell in the positivec (up) direction of the y-axis

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        is_healthy: bool = True
        for cell in self.population:
            if cell.is_infected():
                is_healthy = False
        return is_healthy

        # return False

    def check_contacts(self):
        """Compares the distance between every two cell's location, calling the contact_with funciton on those with distances smaller than CELL_RADIUS."""
        i: int = 0 
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS: 
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1
       
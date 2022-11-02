"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str 
    toppings: int 
    extra_cheese: bool = False

    #constructor
    def __init__(self, size: str, toppings: int): # init short for initialization of object
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    # method call built into class
    def price(self, tax: float) -> float:
        """Calculate prize of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else: 
            total += 8

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3) # this constructs a new Pizza object
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}") # tax parameter = 1.05

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")
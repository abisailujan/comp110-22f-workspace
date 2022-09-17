"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list() # creating a list named rolls of type int and setting it to be empty

while len(rolls) == 0 or rolls[len(rolls) -1] != 1: # while the length of rolls is equal to 0 OR while the last index of the list named rolls is not equal to 1 (cause that's the winning number) we will loop
    rolls.append(randint(1, 6))

print(rolls)

# Remove an itme from the list by its index ("pop")
rolls.pop(len(rolls) -1)
print(rolls)

# Sum the values of our roles!
i: int = 0
sum: int = 0

while i < len(rolls): 
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")


# rolls.append(randint(1, 6)) # calling the append function, using the randint expression as an argument(generates a random die roll) as an argument to it, to add an item to our list 
# rolls.append(randint(1, 6)) 
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual idem
# print(rolls[0])
# print(rolls[1])
# print(rolls[2])

# # Access the length of a list (number of items)
# print(len(rolls))

# # Access the last item of list
# last_index: int = len(rolls) - 1
# print(rolls[last_index])
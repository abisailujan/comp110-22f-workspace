"""This is an example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5. What is is? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!")
    print("Go treat yourself")
else: 
    print("Sorry! That was an incorrect guess")
    print("Give it another try")
    if guess > SECRET: 
        print("Go lower")
    else: 
        print("Go higher")
print("Game over.")

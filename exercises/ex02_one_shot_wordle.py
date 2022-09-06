"""EX02 - One-Shot Wordle - Loops assignment."""

__author__ = "730249754"

secret_word: str = "python" 

secret_word_length: int = len(secret_word)

entered_word: str = input(f"What is your {secret_word_length}-letter guess? ")

i: int = 0

# assuring that entered word is the correct length of secret word
while i < len(secret_word): 
    if len(entered_word) != len(secret_word):
        entered_word: str = input(f"That was not {secret_word_length} letters! Try again: ")
        
    i = i + 1
    
# Part 2: Checking indices for correct matches

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

j: int = 0
emoji_result: str = ""

# assigning the correct coloroed emoji to the respective indecies 
while j < len(entered_word):
    if entered_word[j] == secret_word[j]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        # emoji_result = emoji_result + WHITE_BOX
        elsewhere: bool = False
        alternate_index: int = 0
        while not elsewhere and alternate_index < len(secret_word):
            if secret_word[alternate_index] == entered_word[j]:
                elsewhere = True
            alternate_index = alternate_index + 1
        if elsewhere: 
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX
    j = j + 1

print(emoji_result)

# example terminal code has the following conditionals printed after emoji string

if entered_word == secret_word:
    print("Woo! You got it!")

if entered_word != secret_word:
    print("Not quite. Play again soon!")
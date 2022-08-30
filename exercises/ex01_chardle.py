"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730249754"

entered_word: str = input("Enter a 5-character word: ")

if len(entered_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

entered_character: str = input("Enter a single character: ")

if len(entered_character) != 1:
    print("Error: Character must be a single character")
    exit()

matching_character_count: int = 0

print("Searching for " + entered_character + " in " + entered_word)

if entered_character == entered_word[0]:
    print(entered_character + " found at index 0")
    matching_character_count = matching_character_count + 1

if entered_character == entered_word[1]:
    print(entered_character + " found at index 1")
    matching_character_count = matching_character_count + 1

if entered_character == entered_word[2]:
    print(entered_character + " found at index 2")
    matching_character_count = matching_character_count + 1

if entered_character == entered_word[3]:
    print(entered_character + " found at index 3")
    matching_character_count = matching_character_count + 1

if entered_character == entered_word[4]:
    print(entered_character + " found at index 4")
    matching_character_count = matching_character_count + 1

if matching_character_count == 1:
    print(str(matching_character_count) + " instance of " + entered_character + " found in " + entered_word)

if matching_character_count > 1:
    print(str(matching_character_count) + " instances of " + entered_character + " found in " + entered_word)

if matching_character_count == 0:
    print("No instances of " + entered_character + " found in " + entered_word)
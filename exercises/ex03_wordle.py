"""EX03 - Structured Wordle."""

author: str = "730249754"


def contains_char(word: str, char: str) -> bool:
    """Evaluating if char is in word."""
    assert len(char) == 1 # this says that char must be 1 character long
    #using a while loop to seach for char in word's indices
    i: int = 0 
    while i < len(word): 
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Calling the contains_char function to assign the correct colored emojis to the returned value."""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # use a while loop to search through each indicies of guess and secret, and assign emojis respectfully

    i: int = 0
    emoji_color: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_color += GREEN_BOX
        else: 
            if contains_char(secret, guess[i]):
                emoji_color += YELLOW_BOX
            else:
                emoji_color += WHITE_BOX
        i += 1
    return emoji_color


def input_guess(expected_len: int) -> str:
    """Returning an input str guess of a length matching the int used to call function."""
    entered_word: str = input(f"Enter a {expected_len} character word: ")
    if len(entered_word) == expected_len:
        return entered_word
    else:
         while len(entered_word) != expected_len:
             retry: str = input(f"That wasn't {expected_len} chars! Try again: ")
             if len(retry) == expected_len:
                 return retry


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_count: int = 1
    win: bool = False

    while turn_count < 7 and not win: 
        print(f"=== Turn {turn_count}/6 ===")
        user_input: str = input_guess(len(secret_word))
        print(emojified(user_input, secret_word))
        if user_input == secret_word:
            win = True
        else: 
            turn_count += 1
    if win:
        print(f"You won in {turn_count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()
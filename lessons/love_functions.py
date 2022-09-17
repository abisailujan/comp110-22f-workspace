""""Some tender, loving functions."""

def love(subject: str) -> str:
    """Given a subject as a parameter, a loving string."""
    return f"I love you {subject}!!!!!!"


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n: 
        love_note += love(to) + "\n"
        i += 1
    return love_note


# def main() -> None:
#    """The program's entrypoint."""
 #   y: str = ""
  #  print(love(y))
  #  print(spread_love(y))

# if __name__ == "__main__":
 #   print("__name__ is '__main__'")
 #   main()
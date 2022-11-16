"""Examples of optional parameters and Union types."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightfful greeting."""
    greeting: str = "hello, "
    if isinstance(name, str):  # built-in function that test if `name` is a string
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Life from Sector " + str(name)
    return greeting


# Single argument:
print(hello("Abisai"))

# No arguments
print(hello())

# int argument 
print(hello(110))

# float argument 
print(hello(3.14))
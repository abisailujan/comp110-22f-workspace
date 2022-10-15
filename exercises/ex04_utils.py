"""EX04 - List Utility Functions."""


author: str = "730249754"

def all(a: list[int], b: int) -> bool:
    """Determines if list is composed of same number as int argument."""
    assert len(a) >= 1
    i: int = 0 
    while i < len(a):
        if a[i] != b:
            return False
        i += 1


def max(a: list[int]) -> int:
    """Determines the maximum int value of a list."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum: int = a[i]
    while(i < len(a)): 
        if a[i] >= maximum:
            maximum = a[i]
        i += 1
    return maximum


def is_equal(a: list[int], b: list[int]) -> bool:
    """Determines if each of lists indicies match."""
    i: int = 0
    if len(a) > len(b):
        while i < len(a):
            if a[i] != b[i]:
                return False
            i += 1
    elif len(b) > len(a):
        while i < len(b):
            if a[i] != b[i]:
                return False
            i += 1
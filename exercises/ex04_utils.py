"""EX04 - List Utility Functions."""

from xmlrpc.client import Boolean


author: str = "730249754"

def all(a: list[int], b: int) -> bool:
    """Determines if list is composed of same number as int argument."""
    assert len(a) > 0
    i: int = 0 
    matches: bool = False
    while i < len(a):
        if a[i] == b:
            matching = True
        else:
           matching = False
        i += 1
    return matching


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


def is_equal(a: list[int], b: list[int]) -> Boolean:
    """Determines if each of lists indicies match."""
    index_match: bool
    i: int = 0
    while i < len(a):
        if a[i] == b[i]:
             index_match = True
        else:
            index_match = False
        i += 1
    return index_match
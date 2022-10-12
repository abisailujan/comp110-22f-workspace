"""Ex05 - list Utility Functions."""

author: str = "730249754"


def only_evens(a: list[int]) -> int:
    """Returns a list of the even ints from a given list."""
    even_list: list[int] = []
    for even_num in a:
        if even_num % 2 == 0:
            even_list.append(even_num)
    return even_list


def concat(a: list[int], b: list[int]) -> str:
    """Adds the elements of list a, then list b into a new list."""
    new_list: list[int] = []
    for index in a:
        new_list.append(index)
    for item in b:
        new_list.append(item)
    return new_list


def sub(a: list[int], start: int, end: int) -> int:
    """Returns a sub list from an entered list, whose start and end are indicated by the arguments."""
    new_start: int = start
    new_end: int = end - 1
    new_list: list[int] = []
    """If the start index is neg, start from index 0. If the end index is greater than list length, end with index len(list) - 1."""
    if start < 0:
        new_start = 0
    elif end > len(a):
        new_end = len(a) - 1
    i: int = 0
    while i < len(a):
        if i >= new_start and i <= new_end:
            new_list.append(a[i])
        i += 1
    if len(a) == 0 or start > len(a) or end <= 0:
        return []
    return new_list
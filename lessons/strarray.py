"""Examples of "vectorized" operations via magic methods."""  # what if we wanted to concatinate our 

from __future__ import annotations
from typing import Union 


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
        # 1. Loop through every item in self's items list
            for item in self.items:   # item is actually the value at the index, not the index
        # 2. Concatenate the rhs parameter
                item += rhs
        # 3. Append the concatenated string to results' items attribute
                result.items.append(item)
        else: 
            # Otherwise, loop through each index of self's items
            for i in range(0, len(self.items)):
            # concatenate the corredsponding value of rhs' items at same index
            # Append the resulting string to results' items list
                result.items.append(self.items[i] + rhs.items[i])
                
        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + b)
print (a + " " + b)
print(b + ", " + a + "!")
"""An example of for in syntax."""

names: list[str] = ["Abisai", "Ailanny", "Abi", "Mel"]

# Example of iterating through names using a while loop
print("While output: ")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for .. in output: ")
# The following for..in loop is the same as the while loop above
for name in names: 
    print(name)

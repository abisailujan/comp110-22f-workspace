"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict() # easiest way to initialize to an empty dictionary is to call the dictionary constructor to build one for us

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19_400 # underscore means comma in python 
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# print a dictionary literal representation
print(schools)

# Access a value by its key -- lookup
print(f"UNC has {schools['UNC']} students") #use single quotes if key or value type is string, to avoid python error

# Remove a key-value pair from a dictionary 
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

# Update or reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal 
schools = {} # same as dict()
print(schools)
# Alternatively initialize key-value parameters 
schools = {"UNC": 19_400, "Dukie": 6_717, "NCSU": 26150}

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
# print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"]) # error type at bottom of error message, right above tells you on what line


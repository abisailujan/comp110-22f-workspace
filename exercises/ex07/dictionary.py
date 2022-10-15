"""Exercise 07 - Dictionary Functions."""

__author__: str = "730249754"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Reverses the keys and values of a dictionary passed in."""
    inverted_dict: dict[str, str] = {}
    match: str = ""
    for key in dictionary:
        new_key: str = dictionary[key]
        new_value: str = key 
        found: bool = new_key in match
        if not found:
            inverted_dict[new_key] = new_value
        else:
            raise KeyError("Duplicate keys not permitted")
        match += new_key
    return inverted_dict


def favorite_color(faves: dict[str, str]) -> str:
    """Returns the color value counted the most from a passed dict."""
    all_colors: list[str] = []
    best_color: str = ""
    length: int = 0
    # Add all values into a list
    for person in faves:
        all_colors.append(faves[person])
        # we let this loop finish adding all color values into all_colors
    # loop through dictionary again  
    for person in faves: 
        # loop through all_colors list 
        i: int = 0
        color_tally: list[str] = []
        while i < len(all_colors): 
            # add faves[person] to color_tally each time found in all_colors
            if faves[person] == all_colors[i]: 
                color_tally.append(faves[person])
            i += 1
    # let nested loop finish going through all_colors
        # assign faves[person] best_color depending on length of its color_tally

        if len(color_tally) == 1: 
            best_color == faves[person]
            length = len(color_tally)
        if len(color_tally) > length:
            best_color = faves[person]
            length = len(color_tally)
    return best_color


def count(given: list[str]) -> dict[str, int]:
    """Return a dict of each unique element of a given list as its keys, and # of occurence as the values."""
    output: dict[str, int] = {}
    for key in given: 
        if key in output: 
            output[key] += 1
        else: 
            output[key] = 1
    return output

"""Dictionary related utility functions."""

__author__ = "730249754"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table' aka list of disctionaries."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()
    
    return result


def column_values(table: list[dict[str,str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Transform a row orientated table to a column-oriented."""
    result: dict[str, list[str]] = {}
    first_row: dict[str,str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 


def head(given_dict: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for col in given_dict:
        index: int = 0
        values_list: list[str] = []
    
        if len(given_dict[col]) <= num:
            result[col] = given_dict[col]
        else:
            while index < num:
                values_list.append(given_dict[col][index])
                index += 1
            result[col] = values_list
    
    return result


def select(col_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in col_names: 
        if item in col_table: 
            result[item] = col_table[item]
        
    return result 


def concat(dict_a: dict[str, list[str]], dict_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in dict_a:
        result[key] = dict_a[key]
    for key in dict_b:
        if key in result:
            for item in dict_b[key]:
                result[key].append(item)
        else:
            result[key] = dict_b[key]
    
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Given a list of str, this function will produce a dict where each key is a unique value in teh given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in given_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
            
    return result
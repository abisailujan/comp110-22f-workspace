"""Tests for Ex07 Dictionary."""

import pytest

from exercises.ex07.dictionary import invert, favorite_color, count

author: str = "730249754"

with pytest.raises(KeyError):
    full_names = {'abisai': 'lujan', 'john': 'wayne', 'lil': 'wayne'}
    invert(full_names)


def test_invert_letters() -> None:
    """Tests if invert switches key and values of the same string but different lengths from a dict passed."""
    vowels: dict[str, str] = {'aaaa': 'aa', 'bbbb': 'bb', 'cccc': 'cc'}
    assert invert(vowels) == {'aa': 'aaaa', 'bb': 'bbbb', 'cc': 'cccc'}


def test_invert_order() -> None:
    """Tests if invert function reverses key and value order from passed dictionary."""
    test_dict: dict[str, str] = {'1': 'first', '2': 'second', '3': 'third'}
    assert invert(test_dict) == {'first': '1', 'second': '2', 'third': '3'}


def test_invert_empty_key() -> None:
    """Tests if invert switches key and values in dict if one key is empty string."""
    lost_key_dict: dict[str, str] = {'': 'full', 'hollow': 'whole', 'starving': 'stuffed'}
    assert invert(lost_key_dict) == {'full': '', 'whole': 'hollow', 'stuffed': 'starving'}


def test_favorite_color_empty_values() -> None:
    """Tests if favorite_color function returns an empty string, give a dict with empty values."""
    no_values: dict[str, str] = {'abisai': '', 'sam': '', 'ben': ''}
    assert favorite_color(no_values) == ""


def test_favorite_color_uniq_vals() -> None:
    """Tests if favorite_color function returns first value of given dictionary with all unique values."""
    uniq_vals: dict[str, str] = {'abisai': 'yellow', 'alyx': 'green', 'ben': 'blue'}
    assert favorite_color(uniq_vals) == "yellow"


def test_favorite_color_pop() -> None:
    """Tests if favorite_color returns the value with most duplicates from a given dictionary."""
    test: dict[str, str] = {'abisai': 'green', 'alyx': 'yellow', 'dan': 'yellow', 'bob': 'green', 'beth': 'yellow', 'hank': 'red'}
    assert favorite_color(test) == "yellow"


def test_count_empty() -> None:
    """Tests if count function returns an empty string key and its # of occurance as value from given list of empty strings."""
    empty_vals: list[str] = ['', '', '']
    assert count(empty_vals) == {'': 3}


def test_count_uniq_vals() -> None:
    """Tests if count function returns a dict of unique keys and 1 as values from a list of unique strings."""
    uniq_vals: list[str] = ['abisai', 'ben', 'alt']
    assert count(uniq_vals) == {'abisai': 1, 'ben': 1, 'alt': 1}


def test_count_dupl_vals() -> None:
    """Tests if count function returns unique keys and count their duplicates as values from list with duplicate strings."""
    dupl_vals: list[str] = ['the', 'hat', 'the', 'we']
    assert count(dupl_vals) == {'the': 2, 'hat': 1, 'we': 1}
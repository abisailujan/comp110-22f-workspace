"""Unit Tests for EX05."""

from exercises.ex05.utils import only_evens, sub, concat

author: str = "730249754"


def test_only_evens_empty() -> None:
    """Tests the only_evens function with an empty list parameter."""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []


def test_only_evens_all_odd() -> None:
    """Tests that only_evens returns an empty list when given an list of all odd ints."""
    odd_list: list[int] = [1, 1, 1]
    assert only_evens(odd_list) == []


def test_only_evens_mixed_ints() -> None:
    """Tests that only_evens is able to return only even values from a list of both odd and even ints."""
    mixed_list: list[int] = [6, 2, 3]
    assert only_evens(mixed_list) == [6, 2]


def test_concat_empty_list() -> None:
    """Tests if concat function returns an empty list when given two empty lists."""
    empty_a: list[int] = []
    empty_b: list[int] = []
    assert concat(empty_a, empty_b) == []


def test_concat_one_empty() -> None:
    """Tests to see if given one empty and one full list, concat returns only the full list's values."""
    list_a: list[int] = [1, 2, 3]
    empty_list: list[int] = []
    assert concat(list_a, empty_list) == [1, 2, 3]


def test_concat_b_after_a() -> None:
    """Tests that concat returns b's elements after a's elements in new string."""
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [4, 5, 6]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 6]


def test_sub_empty_list() -> None:
    """Tests if sub function returns an empty list when given an empty list but valid start and end indicies."""
    input_list: list[int] = []
    input_start: int = 1
    input_end: int = 3
    assert sub(input_list, input_start, input_end) == []


def test_sub_neg_start() -> None:
    """Tests if the returned list begins with the original first index if the start parameter is negative."""
    input_list: list[int] = [15, 25, 35, 45]
    input_start: int = -3
    input_end: int = 3
    assert sub(input_list, input_start, input_end) == [15, 25, 35]


def test_sub_end_is_last_index() -> None:
    """Tests if the end of the sub list is the end of the original list, given a inputed end that is longer than original list length."""
    input_list: list[int] = [15, 25, 35, 45]
    input_start: int = 2
    input_end: int = 6
    assert sub(input_list, input_start, input_end) == [35, 45]
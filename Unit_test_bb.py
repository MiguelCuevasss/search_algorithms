import pytest
from searching import binary_search


def test_binary_search_finds_first_element():
    assert binary_search([10, 20, 30, 40, 50], 10) == 0


def test_binary_search_finds_middle_element():
    assert binary_search([10, 20, 30, 40, 50], 30) == 2


def test_binary_search_finds_last_element():
    assert binary_search([10, 20, 30, 40, 50], 50) == 4


def test_binary_search_returns_minus_one_when_not_found():
    assert binary_search([10, 20, 30, 40, 50], 99) == -1

def test_binary_search_empty_list():
    assert binary_search([], 10) == -1
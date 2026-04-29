import pytest
from searching import linear_search


def test_linear_search_finds_first_element():
    assert linear_search([10, 20, 30, 40], 10) == 0


def test_linear_search_finds_middle_element():
    assert linear_search([10, 20, 30, 40], 30) == 2
    
def test_linear_search_finds_last_element():
    assert linear_search([10, 20, 30, 40], 40) == 3


def test_linear_search_returns_minus_one_when_not_found():
    assert linear_search([10, 20, 30, 40], 99) == -1


def test_linear_search_empty_list():
    assert linear_search([], 10) == -1
import pytest
from programs import list_of_squares

def test_list_of_squares_one():
    assert list_of_squares.list_of_squares(1) == {1: 1}

def test_list_of_squares_two():
    assert list_of_squares.list_of_squares(2) == {1: 1, 2: 4}

def test_list_of_squares_five():
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
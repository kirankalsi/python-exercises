import pytest
from programs import debugging_ex2

def test_product_one_in_list():
    assert debugging_ex2.product([4]) == 4

def test_product_two_in_list():
    assert debugging_ex2.product([7,8]) == 56
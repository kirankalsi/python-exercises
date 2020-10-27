import pytest
from programs import factorial

def test_fact_two():
    assert factorial.fact(2) == 2

def test_fact_three():
    assert factorial.fact(3) == 6

def test_fact_four():
    assert factorial.fact(4) == 24

def test_fact_five():
    assert factorial.fact(5) == 120
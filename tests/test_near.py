import pytest
from programs import near

def test_near_true():
    assert near.near("reset", "rest") == True

def test_near_false():
    assert near.near("eave", "leave") == False
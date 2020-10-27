import pytest
from programs import debugging_ex3

def test_is_prime_less_than_2():
    assert debugging_ex3.is_prime(0) == False

def test_is_prime_more_than_2():
    assert debugging_ex3.is_prime(13) == True

def test_is_not_prime():
    assert debugging_ex3.is_prime(6) == False
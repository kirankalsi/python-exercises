import pytest
from programs import vowels

def test_vowels_none():
    assert vowels.vowels('rhythm') == 0

def test_vowels_single():
    assert vowels.vowels('me') == 1

def test_vowels_seven():
    assert vowels.vowels('absolutely amazing') == 7

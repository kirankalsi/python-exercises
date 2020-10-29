import pytest
from programs import best_conjugation

def test_best_conjugation():
    assert best_conjugation.best_conjugation('awesomeness') == "14 Subwords found which are: ['awe', 'en', 'ene', 'es', 'me', 'men', 'mene', 'ne', 'ness', 'om', 'omen', 'so', 'some', 'we']"
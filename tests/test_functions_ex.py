import pytest
from programs import functions_ex

def test_grade_calculator_full_marks():
    assert functions_ex.grade_calculator(25, 50, 100) == 100

def test_grade_calculator_full_marks():
    assert functions_ex.grade_calculator(55, 50, 60) == False

#pytest -s
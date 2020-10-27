import pytest
from programs import functions_ex

def test_grade_calculator_full_marks():
    assert functions_ex.grade_calculator(25, 50, 100) == 100

def test_grade_calculator_invalid_input():
    assert functions_ex.grade_calculator(55, 50, 60) == False

def test_grade_calculator_invalid_input():
    assert functions_ex.grade_calculator(-5, 50, 60) == False

def test_grade_boundary_Astar():
    assert functions_ex.grade_boundary(90) == 'A*'

def test_grade_boundary_A():
    assert functions_ex.grade_boundary(88) == 'A'

def test_grade_boundary_B():
    assert functions_ex.grade_boundary(72) == 'B'

def test_grade_boundary_C():
    assert functions_ex.grade_boundary(65) == 'C'

def test_grade_boundary_D():
    assert functions_ex.grade_boundary(56) == 'D'

def test_grade_boundary_F():
    assert functions_ex.grade_boundary(37) == 'F'

#pytest -s
import pytest
from programs.functions_ex import grade_calculator, grade_boundary

def test_grade_calculator_full_marks():
    assert grade_calculator(25, 50, 100) == 100

def test_grade_calculator_invalid_input():
    assert grade_calculator(55, 50, 60) == False

def test_grade_calculator_invalid_input():
    assert grade_calculator(-5, 50, 60) == False

def test_grade_boundary_Astar():
    assert grade_boundary(90) == 'A*'

def test_grade_boundary_A():
    assert grade_boundary(88) == 'A'

def test_grade_boundary_B():
    assert grade_boundary(72) == 'B'

def test_grade_boundary_C():
    assert grade_boundary(65) == 'C'

def test_grade_boundary_D():
    assert grade_boundary(56) == 'D'

def test_grade_boundary_F():
    assert grade_boundary(37) == 'F'

#pytest -s
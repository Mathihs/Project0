import calculator
import math
import pytest

@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), 3], [(1, -2), -1], [(0.1, 0.2), 0.3]]
)
def test_add(arg, expected_output):
    tol = 1e-10
    assert calculator.add(arg[0], arg[1]) <= expected_output + tol
    x,y = "Hello ","World"
    assert calculator.add(x,y) == "Hello World"

@pytest.mark.parametrize(
    "arg, expected_output", [[4, 24]]
)
def test_factorial(arg, expected_output):
    assert calculator.factorial(arg) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output", [[0, 0], [3.14/2, 1], [3.14/4, math.sqrt(2)/2], [3.14, 0]]
)
def test_sin(arg, expected_output):
    tol = 1e-2; N = 10
    assert calculator.sin(arg, N) <= expected_output + tol

@pytest.mark.parametrize(
    "arg, expected_output", [[(4, 2), 2], [(2, -1), -2], [(-5, -2), 2.5], [(0.4, 0.2), 2]]
)
def test_divide(arg, expected_output):
    tol = 1e-10
    assert calculator.divide(arg[0], arg[1]) <= expected_output + tol

@pytest.mark.parametrize(
    "arg, expected_output", [[(4, 2), 8], [(2, -1), -2], [(-5, -2), 10], [(0.4, 0.2), 0.08]]
)
def test_multiply(arg, expected_output):
    tol = 1e-10
    assert calculator.multiply(arg[0], arg[1]) <= expected_output + tol

@pytest.mark.parametrize(
    "arg, expected_output", [[0, 1], [3.14/2, 0], [3.14/4, math.sqrt(2)/2], [3.14, 1]]
)
def test_cos(arg, expected_output):
    tol = 1e-2; N = 10
    assert calculator.cos(arg, N) <= expected_output + tol

@pytest.mark.parametrize(
    "arg, expected_output", [[(1, "Hello"), TypeError]]
)
def test_if_add_raises_TypeError(arg, expected_output):
    with pytest.raises(expected_output):
        calculator.add(arg[0], arg[1])

@pytest.mark.parametrize(
    "arg, expected_output", [[(4, 0), ZeroDivisionError]]
)
def test_if_divide_raises_ZeroDivisionError(arg, expected_output):
    with pytest.raises(expected_output):
        calculator.divide(arg[0], arg[1])
import calculator
import math
import pytest

def test_add():
    tol = 1e-10
    assert calculator.add(0.1, 0.2) <= 0.3 + tol
    x,y = "Hello ","World"
    assert calculator.add(x,y) == "Hello World"

def test_factorial():
    assert calculator.factorial(4) == 24

def test_sin():
    tol = 1e-10
    x = 3.14/4; N = 10
    assert calculator.sin(x,N) <= math.sqrt(2)/2 + tol

def test_divide():
    tol = 1e-10
    x,y = 3012387, 412381297948
    assert calculator.divide(x,y) <= 7.30485843e-6 + tol

def test_multiply():
    tol = 1e-10
    x,y = 4, 1.54
    assert calculator.multiply(x,y) <= 6.16 + tol

def test_cos():
    tol = 1e-10
    x = 3.14; N = 10
    assert calculator.cos(x,N) <= 1 + tol

def test_to_float_gives_correct_instance():
    assert isinstance(calculator.to_float(1), float)

def test_to_float_return_correct_value():
    x = 1
    assert abs(calculator.to_float(x) - x) < 1e-12

def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError):
        calculator.to_float("Hello")

def test_if_add_raises_TypeError():
    with pytest.raises(TypeError):
        calculator.add(3, "Hello")

def test_if_divide_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(4, 0)
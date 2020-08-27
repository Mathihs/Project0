import calculator
import math

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
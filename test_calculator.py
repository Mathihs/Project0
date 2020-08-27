import calculator

def test_add():
    tol = 1e-10
    assert calculator.add(0.1, 0.2) <= 0.3 + tol
    x,y = "Hello ","World"
    assert calculator.add(x,y) == "Hello World"
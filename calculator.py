import math

def add(x,y):
    return x + y

def factorial(x):
    ans = 1
    for i in range(1,x+1):
        ans *= i 
    print(f"My implementation: {ans} | Built in: {math.factorial(x)}")
    return ans

def sin(x,N):
    ans = 0
    for n in range(N+1):
        ans += ((-1)**n*x**(2*n+1))/factorial(2*n+1)
    return ans

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

def cos(x,N):
    ans = 0
    for n in range(N+1):
        ans += ((-1)**n*x**(2*n))/factorial(2*n)
    return ans

def to_float(x):
    return float(x)
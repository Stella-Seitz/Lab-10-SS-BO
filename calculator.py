import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0 when 'a' is 0")
    return b / a
def log(a, b):
    if a <=0 or a==1:
        raise ValueError("Logarithm base 'a' must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm value 'b' must be greater than 0")
    return math.log(b, a)
def exp(a, b):
    return a ** b


#calculator.py
#- Defines functions used to create a simple calculator

#One function per operation, in order.
# First example
#def add(a, b):
    pass
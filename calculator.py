import math
def add(a, b):
    return a + b
def subtract (a,b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0 when 'a' is 0")
    return b / a
def logarithm(a,b):
    math.log(a,b)
def exp(a, b):
    return a ** b


#calculator.py
#- Defines functions used to create a simple calculator

#One function per operation, in order.
# First example
#def add(a, b):
    pass
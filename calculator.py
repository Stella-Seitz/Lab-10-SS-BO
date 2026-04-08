"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example
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
    math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)





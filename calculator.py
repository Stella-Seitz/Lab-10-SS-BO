#https://github.com/Stella-Seitz/Lab-10-SS-BO/blob/main/test_calculator.py
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
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def hypotenuse(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.hypot(a,b)




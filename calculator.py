"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    if a < 0: raise ValueError
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b): 
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if a == 0: raise ZeroDivisionError
    return b/a
def logarithm(a,b):
    if a >= 0 or a == 1 or b <= 0: raise ValueError
    return math.loga(b)
def exponent(a,b):
    math.pow(a,b)



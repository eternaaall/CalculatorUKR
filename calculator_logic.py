import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль")
    return a / b

def power(a, b):
    return a ** b

def root(a):
    if a < 0:
        raise ValueError("Корінь з від'ємного числа")
    return math.sqrt(a)

def sin_deg(a):
    return math.sin(math.radians(a))

def cos_deg(a):
    return math.cos(math.radians(a))

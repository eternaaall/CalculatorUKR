import pytest
from calculator_logic import add, subtract, multiply, divide, power, root, sin_deg, cos_deg

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Ділення на нуль"

def test_root_negative():
    try:
        root(-4)
    except ValueError as e:
        assert str(e) == "Корінь з від'ємного числа"

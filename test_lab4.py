import pytest

class Calculator():
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")


def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)

    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)

    assert True


def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)

    assert True

calc = Calculator("Calc name")

def test_subtract():
    assert calc.subtract(3, 1) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(1, 3) == 2
    assert calc.subtract(-3, -2) == -1

def test_multiply():
    assert calc.multiply(3, 1) == 3
    assert calc.multiply(1, 0) == 0
    assert calc.multiply(-1, 3) == 3
    assert calc.multiply(-3, -2) == -6


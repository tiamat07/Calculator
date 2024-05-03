import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 12, 3) == 36

    def test_division_success(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 9, 3) == 6

    def test_adding_success(self):
        assert self.calc.adding(self, 3, 1) == 4

    def teardown(self):
        print('Выполнение метода terdown')

import sys
import unittest

path = r'C:\Users\Michal\PycharmProjects\Python_unittest_course\07_test_class_method'
sys.path.append(path)

from calculator.calc_math import MathCalculator


class TestMathCalculator(unittest.TestCase):

    def test_add(self):
        calc = MathCalculator()
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        calc = MathCalculator()
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        calc = MathCalculator()
        self.assertEqual(calc.mul(3, 4), 12)


# py -m unittest tests/calc_math_test.py -v

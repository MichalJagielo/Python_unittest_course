import unittest
from parameterized import parameterized
from calculator.calc_math import MathCalculator


class TestMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = MathCalculator()

    @parameterized.expand([
        ('negative', -3, -2, -5),
        ('first_negative', -3, 2, -1),
        ('second_negative', 3, -2, 1),
        ('positive', 3, 2, 5)
    ])
    def test_add(self, name, x ,y, result):
        self.assertEqual(self.calc.add(x, y), result)



# py -m unittest tests/calc_math_test.py -v

import unittest
from calculator.calc_math import MathCalculator


def setUpModule():
    print("setting up ----> module calculator")
    global calc
    calc = MathCalculator()

def tearDownModule():
    print('tearing down...')
    #global calc
    #del calc


class TestMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 4), 12)
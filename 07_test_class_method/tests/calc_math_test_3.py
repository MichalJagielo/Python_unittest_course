import unittest
from calculator.calc_math import MathCalculator


class TestMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class add.....')
        cls.calc = MathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('tearing down...')
        del cls.calc

    def test_add_int(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_float(self):
        self.assertEqual(self.calc.add(3.0, 4.0), 7.0)

    def test_add_both_negative(self):
        self.assertEqual(self.calc.add(-3, -4), -7)


class TestMathCalculatorSub(unittest.TestCase):

    def test_sub_int(self):
        calc = MathCalculator()
        self.assertEqual(calc.sub(3, 4), -1)

    def test_sub_float(self):
        calc = MathCalculator()
        self.assertEqual(calc.sub(3.0, 4.0), -1.0)
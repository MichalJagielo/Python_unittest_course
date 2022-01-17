
import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_ten_pct(self):
        self.assertAlmostEqual(10, calc_tax(100, 0.1))

    def test_calc_tax_with_fourteen_pct_almost(self):
        self.assertAlmostEqual(14, calc_tax(100, 0.14))

    def test_calc_tax_wrong_amount_type(self):
        self.assertRaises(TypeError, calc_tax, 'two', 0.12)

    def test_calc_tax_wrong_tax_rate_type(self):
        self.assertRaises(TypeError, calc_tax, 132, 4)

    def test_calc_tax_wrong_amount_value(self):
        self.assertRaises(ValueError, calc_tax, -120, 0.12)

    def test_calc_tax_wrong_tax_rate_value(self):
        self.assertRaises(ValueError, calc_tax, 100, 1.1)

    # def test_calc_tax_with_fourteen_pct(self):
    #     self.assertEqual(14, calc_tax(100, 14))



import unittest
from tax_age import calc_tax


class TestCalcTax(unittest.TestCase):

    # def test_calc_tax_with_ten_pct(self):
    #     self.assertAlmostEqual(10, calc_tax(100, 0.1, 18))
    #
    # def test_calc_tax_with_fourteen_pct_almost(self):
    #     self.assertAlmostEqual(14, calc_tax(100, 0.14, 18))
    #
    # def test_calc_tax_wrong_amount_type(self):
    #     self.assertRaises(TypeError, calc_tax, 'two', 0.12)
    #
    # def test_calc_tax_wrong_tax_rate_type(self):
    #     self.assertRaises(TypeError, calc_tax, 132, 4)
    #
    # def test_calc_tax_wrong_amount_value(self):
    #     self.assertRaises(ValueError, calc_tax, -120, 0.12, 18)
    #
    # def test_calc_tax_wrong_tax_rate_value(self):
    #     self.assertRaises(ValueError, calc_tax, 100, 1.1, 18)

    def test_calc_tax_wrong_age_type(self):
        self.assertRaises(TypeError, calc_tax, 60000, 0.20, '18')

    def test_calc_tax_wrong_age_value(self):
        self.assertRaises(ValueError, calc_tax, 60000, 0.20, 0)

    def test_calc_tax_with_age_eighteen(self):
        self.assertAlmostEqual(calc_tax(60000, 0.20, 18), 5000)

    def test_calc_tax_with_age_twenty(self):
        self.assertAlmostEqual(calc_tax(60000, 0.20, 20), 12000)

    def test_calc_tax_with_age_sixty_five(self):
        self.assertAlmostEqual(calc_tax(60000, 0.20, 65), 12000)

    def test_calc_tax_with_age_sixty_six(self):
        self.assertAlmostEqual(calc_tax(60000, 0.20, 66), 8000)


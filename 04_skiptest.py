
import unittest
from datetime import date
import sys


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('google'.upper(), 'GOOGLE')

    @unittest.skipUnless(sys.platform.startswith('win'), reason='Test available only on Windows')
    def test_case_2(self):
        self.assertEqual('google'.upper(), 'GOOGLE')

    @unittest.skipUnless(sys.platform.startswith('linux'), reason='Test available only on Linux')
    def test_case_3(self):
        self.assertEqual('google'.upper(), 'GOOGLE')

    @unittest.skipIf(date.today().day % 2 != 0, reason='Skip on odd days')
    def test_case_4(self):
        self.assertEqual('google'.upper(), 'GOOGLE')

    @unittest.skipIf(date.today().day % 2 == 0, reason='Skip on even days')
    def test_case_5(self):
        self.assertEqual('google'.upper(), 'GOOGLE')

    @unittest.skip('Always True')
    def test_case_6(self):
        self.assertEqual('google'.upper(), 'GOOGLE')


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
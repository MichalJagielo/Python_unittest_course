
# 3.1 Unittest framework
import unittest


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue('google'.islower())


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('Ala ma kota'.split(), ['Ala', 'ma', 'kota'])

    def test_case_2(self):
        self.assertIn('123', '66612.23666')


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('444.55'.split('.'), ['444', '555'])


class TestClass4(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('#'.join(['John', 'Travolta']), 'John#Travolta')


class TestClass5(unittest.TestCase):

    def test_case_1(self):
        self.assertCountEqual((1, 1, 0), (1, 1, 0))



# py -m unittest 02_unittest_class_order.TestClass1 -v
# py -m unittest 02_unittest_class_order.TestClass1.test_case_2 -v

# py -m unittest 02_unittest_class_order -v -f --> """to first failure"""


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
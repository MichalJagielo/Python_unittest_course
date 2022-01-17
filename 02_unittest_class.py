
# 3 Unittest framework
import unittest


class TestClass(unittest.TestCase):

    def test_case_4(self):
        self.assertTrue('google'.islower())

    def test_case_1(self):
        self.assertEqual('Ala ma kota'.split(), ['Ala', 'ma', 'kota'])

    def test_case_2(self):
        self.assertEqual('444.555'.split('.'), ['444', '555'])

    def test_case_3(self):
        self.assertEqual('#'.join(['John', 'Travolta']), 'John#Travolta')

    def test_case_5(self):
        self.assertCountEqual((1, 1, 0), (1, 1, 0))




# if __name__ == '__main__':
#     unittest.main(verbosity=2)




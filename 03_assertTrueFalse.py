import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance('google', str))

    def test_case_2(self):
        self.assertTrue(isinstance('google', int))

    def test_case_4(self):
        self.assertFalse(isinstance('aws', str))

    def test_case_5(self):
        self.assertFalse(isinstance(5, str))




# if __name__ == '__main__':
#     unittest.main(verbosity=2)
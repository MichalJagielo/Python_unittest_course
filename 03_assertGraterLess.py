import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertGreater(10, 6)

    def test_case_2(self):
        self.assertGreaterEqual(5, 5)

    def test_case_3(self):
        self.assertLess(3, 6)

    def test_case_4(self):
        self.assertLessEqual(5, 6)




# if __name__ == '__main__':
#     unittest.main(verbosity=2)
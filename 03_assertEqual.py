import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    # def test_case_1(self):
    #     self.assertEqual('aws'.upper(), 'aws')

    def test_case_3(self):
        self.assertEqual('3.1.2.4'.split('.'), ['3', '1', '2', '4'])

    def test_case_4(self):
        self.assertEqual(tuple('3.1.2.4'.split('.')), ('3', '1', '2', '4'))

    def test_case_5(self):
        self.assertEqual({1, 2}, {2, 1})

    def test_case_6(self):
        self.assertNotEqual({-8, 2}, {2, 6})

# if __name__ == '__main__':
#   unittest.main(verbosity=2)
import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertIn('@', 'test@test.com')

    def test_case_2(self):
        test_list = ['john', 'travolta', 'is', 'funny', 'guy']
        self.assertIn('is', test_list)

    def test_case_3(self):
        test_list = ['john', 'travolta', 'is', 'funny', 'guy']
        self.assertIn('is not', test_list)

    def test_case_4(self):
        test_dict = {'john': 'travolta', 'is': 'is not', 'guy': 'funny'}
        self.assertIn('john', test_dict)

    def test_case_5(self):
        test_dict = {'john': 'travolta', 'is': 'is not', 'guy': 'funny'}
        self.assertNotIn('johnny', test_dict)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
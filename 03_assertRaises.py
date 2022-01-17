import unittest


def get_value(index, box):
    return box[index]


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertRaises(IndexError, get_value, 8, 'google')

    def test_case_2(self):
        self.assertRaises(Exception, get_value, 8, 'google')

    def test_case_3(self):
        with self.assertRaises(IndexError):
            get_value(8, 'google')


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
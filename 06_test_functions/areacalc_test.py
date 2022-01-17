import unittest
from areacalc import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'Error')

    def test_area_incorrect_type(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, 'five')

    def test_area_negative_value(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)


class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18, 'Error')

    def test_perimeter_incorrect_type(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 4, 'five')

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, perimeter, -4, 5)
        self.assertRaises(ValueError, perimeter, 4, -5)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
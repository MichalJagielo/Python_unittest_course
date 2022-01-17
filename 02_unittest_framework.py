# 2 Unittest framework
import unittest


def area(width, height):

    # width = float(input("Enter width of rectangle - ..."))
    # height = float(input("Enter height of rectangle - ..."))

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError("Wrong type of enter values: int or float required.")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return width * height


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'Error')

    def test_area_incorrect_type(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, 'five')

    def test_area_negative_value(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
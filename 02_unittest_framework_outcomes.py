
# 2.1 Unittest framework
import unittest


def area(width, height):

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError("Wrong type of enter values: int or float required.")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return width * height


class TestArea(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_2(self):
        self.assertEqual(area(4, 5), 22)

    def test_area_3(self):
        raise AssertionError("Error message: raise assertion error")

    def test_area_4(self):
        raise TypeError("Error message: raise type error")


if __name__ == '__main__':
    unittest.main(verbosity=2)
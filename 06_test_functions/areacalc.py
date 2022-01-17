
def area(width, height):

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError("Wrong type of enter values: int or float required.")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return width * height


def perimeter(width, height):

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError("Wrong type of enter values: int or float required.")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return 2 * width + 2 * height
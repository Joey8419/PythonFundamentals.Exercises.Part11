class Rectangle:

    def __init__(self, length, width):
        # Initialize a Rectangle object with given length and width
        self.length = length
        self.width = width

    def area(self):
        # Area of a rectangle is calculated by multiplying the length * width
        return self.length * self.width

    def perimeter(self):
        # Perimeter of a rectangle is calculated by adding twice the length and twice the width
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length_of_sides):
        # Call the __init__ method of the base class (Rectangle) with equal length and width
        super().__init__(length_of_sides, length_of_sides)

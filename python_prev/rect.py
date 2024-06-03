class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def is_square(self):
        return self.width == self.height

# Example usage:
rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 7)

print(f"Rectangle 1: width={rect1.get_width()}, height={rect1.get_height()}")
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")
print(f"Is square: {rect1.is_square()}")

print()

print(f"Rectangle 2: width={rect2.get_width()}, height={rect2.get_height()}")
print(f"Area: {rect2.area()}")
print(f"Perimeter: {rect2.perimeter()}")
print(f"Is square: {rect2.is_square()}")

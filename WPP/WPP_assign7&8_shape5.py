'''Create a base class "Shape" with methods to calculate the area and perimeter. Implement
derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
and perimeter calculations.
'''

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

def create_shape():
    shape_type = input("Enter shape: ").strip().lower()

    if shape_type == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return Rectangle(length, width)
    elif shape_type == "circle":
        radius = float(input("Enter the radius of the circle: "))
        return Circle(radius)
    else:
        print("Invalid shape type")
        return None

def main():
    shapes = []

    while True:
        print("\nCreate a new shape:")
        shape = create_shape()
        if shape:
            shapes.append(shape)
        
        another = input("New shape? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    for shape in shapes:
        print(f"\nShape: {shape.__class__.__name__}")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    main()

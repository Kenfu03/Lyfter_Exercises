import math

class Circle:
    def __init__(self, radius):
        print(f"Circle with radius {radius} created")
        self.radius = radius

    def get_area(self):
        print(f"The circle area is {math.pi*self.radius**2}cm^2")


my_circle = Circle(3)
my_circle.get_area()

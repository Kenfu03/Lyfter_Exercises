from abc import abstractmethod
from abc import ABC
from math import pi

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    def calculate_area(self):
        return pi * (self.radio**2)


    def calculate_perimeter(self):
        return 2 *  pi * self.radio 
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height= height

    def calculate_area(self):
        return self.width * self.height


    def calculate_perimeter(self):
        return 2 *  (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


    def calculate_perimeter(self):
        return 4 * self.side


circle = Circle(4)
square = Square(5)
rectangle = Rectangle(2, 4)
print(f"The area of circle is: {circle.calculate_area()}, the perimeter is: {circle.calculate_perimeter()}")
print(f"The area of square is: {square.calculate_area()}, the perimeter is: {square.calculate_perimeter()}")
print(f"The area of rectangle is: {rectangle.calculate_area()}, the perimeter is: {rectangle.calculate_perimeter()}")


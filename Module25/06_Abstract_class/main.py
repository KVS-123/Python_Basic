from abc import ABC, abstractmethod
from math import  pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return round(self.width * self.length, 2)


class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return round(self.height * self.length * 0.5, 2)


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)

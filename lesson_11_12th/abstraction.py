from abc import ABC, abstractmethod

# Advanced
class Shape(ABC): # abstact class

    @abstractmethod
    def area(self):
        pass

# Test, Design Pattern

class Rectangle(Shape):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14 # Hard Coded



rectangle = Rectangle(10, 12)
circle = Circle(8)

shapes = [rectangle, circle]

# for shape in shapes:
#     if isinstance(shape, Circle):
#         print(shape.area_circle())
#     elif isinstance(shape, Rectangle):
#         print(shape.area2())

for shape in shapes:
    print(shape.area())

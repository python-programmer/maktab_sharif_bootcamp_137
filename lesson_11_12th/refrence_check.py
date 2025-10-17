
class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, value):
        if isinstance(value, Rectangle):
            return self.x == value.x and self.y == value.y
        return False

    def __str__(self):
        return f"Rectangle({self.x}, {self.y})"

    def __add__(self, value):
        return Rectangle(self.x + value.x, self.y + value.y)


rectangle_1 = Rectangle(10, 12)

rectangle_2 = Rectangle(10, 12)

print(rectangle_1 == rectangle_2)

print(rectangle_1 + rectangle_2)

print(rectangle_1)


def change_values(rect: Rectangle):
    rect.x = 111


change_values(rectangle_1)
print(rectangle_1.x)
# Composition


# class Wheel:
#     def show_wheels(self):
#         print("4 wheels")


# class Seat:
#     def show_seats(self):
#         print("8 seats")


# class Car:
#     def __init__(self):
#         self.wheel = Wheel() # composite
#         self.seat = Seat() # composite
    
#     def show_info(self):
#         print("this vehicle is great: 1165")


# car = Car()

# print(car.wheel.show_wheels())
# print(car.wheel)

# Dependency Injection


class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(B, A):
    pass


c = C()

# print(C.__mro__)

# c.method() # B

print(isinstance(c, C))
print(isinstance(c, B))
print(isinstance(c, A))

print(issubclass(C, B))
print(issubclass(B, A))
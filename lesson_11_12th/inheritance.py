
# class Animal:
#     def __init__(self):
#         self.legs = 4

#     def show_info(self):
#         print("Yes we're happy")


# class Cat(Animal):
#     def show_cat_speak(self):
#         print("Meow")


# class Dog(Animal):
#     def show_dog_speak(self):
#         print("Woof")


# cat = Cat()
# cat.show_cat_speak()
# cat.show_info()
# print(cat.legs)

# dog = Dog()
# dog.show_dog_speak()
# print(dog.legs)



### Parents

# class Animal: # Parent
#     def __init__(self, name):
#         self.name = name

#     def walking(self):
#         step = 20
#         step += 1
#         return step


# class Panther(Animal): # Child
#     def __init__(self, name: str): # overriding
#         super().__init__(name)
#         # self.name = name

#     def show(self):
#         print(f"{self.name} {self.family_name}")

#     def walking(self): # method overriding
#         step = super().walking()
#         step = step + 10
#         print(f"{self.name} is walking {step}")

#     def fight():
#         pass


# class Cat(Animal): # Child
#     def __init__(self, name: str): # overriding
#         super().__init__(name)
#         # self.name = name

#     def show(self):
#         print(f"{self.name} {self.family_name}")

#     def walking(self): # method overriding
#         step = super().walking()
#         step = step + 1
#         print(f"{self.name} is walking {step}")


# john = Cat("John")
# john.show()
# john.walking()



# class Father:
#     def __init__(self, family_name: str):
#         self.family_name = family_name

#     def walking(self):
#         print("Father is walking")


# class Mohter:
#     def __init__(self):
#         self.hair_color = "Brown"

#     def dancing(self):
#         print("Mother dancing")

#     def walking(self):
#         print("Mother is walking")


# class Child(Mohter, Father): # mro, Method resultion order
#     def __init__(self, name,  family_name):
#         Mohter.__init__(self)
#         Father.__init__(self, family_name)
#         self.name = name

#     def show_info(self):
#         print(f"{self.name} {self.family_name}")


# hadi = Child("Hadi", "Farhadi")
# hadi.show_info()
# hadi.walking()
# hadi.walking()



# class Animal:
#     def __init__(self, name: str):
#         self.name = name

#     def eating(self):
#         print("eating like an animal")

#     # SOLID principles OOP
#     # def show_fingers(self): 
#     #     print("fingers")

# class CatType(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def fight_for_food(self):
#         print("let fight for ourslef")


# class Tiger(CatType):
#     def __init__(self, name):
#         super().__init__(name)

#     def show_proud(self):
#         print(f"I'm a {self.name} tiger")

#     def show_fingers(self): 
#         print("fingers")


# tiger = Tiger("Allen")
# tiger.show_proud()
# tiger.fight_for_food()



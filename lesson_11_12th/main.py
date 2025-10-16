# full_name = "Brad Pitt"
# age = 61
# skin_color = "White"
# height = 180
# weight = 75
# mood = "Relax"

# def eating():
#     print("I pickup my fork and eating")

# def walking(full_name: str, step: int):
#     print(f"{full_name} walking ... {step} steps")

# def show_info(full_name, age, skin_color, height, weight, mood):
#     print(f"{full_name}: {age} years old, {skin_color} skin, {height} cm, {weight} kg, {mood}")


# show_info(full_name, age, skin_color, height, weight, mood)
# eating()
# walking(full_name, 30)



# full_name = "Rahim Sterling"
# age = 36
# skin_color = "Black"
# height = 180
# weight = 75
# mood = "Angry"

# def eating():
#     print("I pickup my fork and eating")

# def walking(full_name: str, step: int):
#     print(f"{full_name} walking ... {step} steps")

# def show_info(full_name, age, skin_color, height, weight, mood):
#     print(f"{full_name}: {age} years old, {skin_color} skin, {height} cm, {weight} kg, {mood}")


# show_info(full_name, age, skin_color, height, weight, mood)
# eating()
# walking(full_name, 200)


# class Person:
#     def __init__(self, full_name: str, age: int, skin_color: str, height: int, weight: int, mood: str): # constructor
#         self.full_name = full_name
#         self.age = age
#         self.skin_color = skin_color
#         self.height = height
#         self.weight = weight
#         self.mood = mood


# class Person:
#     def __init__(self, full_name: str, age: int, skin_color: str, height: int, weight: int, mood: str):
#         self.full_name = full_name
#         self.age = age
#         self.skin_color = skin_color
#         self.height = height
#         self.weight = weight
#         self.mood = mood

#     def show_info(self):
#         print(f"{self.full_name}: {self.age} years old, {self.skin_color} skin color, {self.height} cm, {self.weight} kg, {self.mood} mood")


# number_list = list() # []
# number_list.append(12)

# number_set = set() # {1, 2}

# number_set.add(13)


# # brad_pit = Person("Brad Pitt", 61, "White", 180, 75, "Relax") # instance

# # # person_list = [(1, "Brad", "M", 32), (2, "Rahim", "F")]

# # print(brad_pit.full_name)

# rahim_sterling = Person("Rahim Sterling", 32, "Black", 175, 68, "Happy") # instance, object
# rahim_sterling.show_info()


# def show(full_name: str, age: int, skin_color: str, height: int, weight: int, mood: str):
#     print(f"{full_name}: {age} years old, {skin_color} skin color, {height} cm, {weight} kg, {mood} mood")


# show("Rahim Sterling", 32, "Black", 175, 68, "Happy")

### Bad attribute intialzer

class Person:
    def __init__(self, full_name: str):
        # self.full_name = "" # bad pattern
        self.full_name = full_name

    def show(self):
        print(self.full_name)


yamal = Person("Lamine Yamal")
# yamal.full_name = "Lamine Yamal" # Bad Pattern
yamal.show()

### Naming

# the name is Bad
class user_name:
    pass

# the name is Ok
class UserName:
    pass

# the name is Ok
class Person:
    pass
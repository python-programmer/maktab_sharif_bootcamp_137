class Person:
    item = 10 # class attribute

    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.age}"

    def show_info(self): # instance method
        print(f"{self.id}\t{self.name}\t{self.age}")

    @staticmethod
    def show_data(value: str): # staticmethod
        print("People are very good")
        return value.upper()

    @classmethod
    def create_person_from_str(cls, info: str): # class method
        data = info.split(" ")
        return cls(data[0], data[1], data[2]) # hard coded




brad = Person(1, "Brad", 61)

brad.show_info()

# Person.show_data()
print("Class Variable".center(50, "-"))
print(Person.item)
print(brad.item)

# print(brad) __str__

print("Changing Class Variable through Class".center(50, "-"))
Person.item += 12
print(Person.item)
print(brad.item)

print("Changing Class Variable through object".center(50, "-"))
brad.item += 32
print(Person.item)
print(brad.item)



person_str = "1 Hadi 38"
hadi = Person.create_person_from_str(person_str)

print(hadi)

data = Person.show_data("python")
print(data)





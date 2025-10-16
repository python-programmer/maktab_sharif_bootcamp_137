# id, full_name, sex, age
user_tuple_list = [(1, "Brad Pitt", "M", 61), (2, "Rahim Sterling", "M", 32), (3, "Kim Kardashin", "F", 63), (4, "Tressa Mother", "F", 88)]

# user_list = [1, 2, 3]


class Person:
    def __init__(self, id: int, full_name: str, sex: str, age: int):
        self.id = id
        self.full_name = full_name
        self.sex = sex
        self.age = age

    def show_info(self):
        print(f"{self.full_name}: {self.age} years old")


user_object_list = list()

for user in user_tuple_list:
    user_object = Person(user[0], user[1], user[2], user[3])
    # user_dict = {"id": user[0], "full_name": user[1]}
    user_object_list.append(user_object)


for user in user_object_list:
    # print(user.items)
    user.show_info()
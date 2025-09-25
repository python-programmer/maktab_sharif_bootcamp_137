
# username: str = "hadi_main_py"

# for letter in username:
#     print(letter)


# print(f"size of {username} is {len(username)}")

# print(f"{username.capitalize()} {username.upper()} {username.lower()}")

# print(f"{username[0:5]}")

# message_str: str = "\tHadi Farhadi   \n"
# print(f"'{message_str}' '{message_str.strip()}'")



# message_list: str = ["message_1", "message_2", "message_3"]

# message: str = ''

# for text in message_list:
#     message += text + " "

# print(f"'{message}'")


# message_with_join = " ".join(message_list)
# print(message_with_join)

# print(message[0:len(message) - 1] == message_with_join)

# message = "Hello {0} how are you today? your code is {code}"

# print(message.format("Ali", code="3256"))


# name = "Hadi Farhadi Yes   "
# count = 0


# for letter in name:
#     if letter == " ":
#         count += 1

# print(f"space count of {name} = {count}")


# name_list = name.split(" ")
# print(name_list, len(name_list))


# Constant
USERS = ((1, "Nima Rabbani", "Male", 32), (2, "Fatemeh Rajabi", "Female", 28),
 (3, "Hanieh Bahrami", "Female", 35), (4, "Rashed Ragheb", "Male", 42))


input_user = [3, "Hanieh Bahrami", "Female", 35]

# if USERS[2] == input_user:
#     print("Yes, they're equal")
# else:
#     print("No")

# if USERS[2] == tuple(input_user):
#     print("Yes, they're equal")
# else:
#     print("No")

# input_user_tuple = tuple(input_user)

# if input_user_tuple in USERS:
#     print("Yes")
# else:
#     print("No")



# def sort_users(user_tupe):

#     sorted_user = sorted(user_tupe, key=lambda user: user[2])
#     print(type(sorted_user))
#     return sorted_user


# print(USERS)

# print("Sorted users".center(50, '-'))

# sorted_user = sort_users(USERS)

# print(sorted_user)


# first_tuple = (1, "Hello", True)
# second_tuple = (1, "Hallo", True)
# if first_tuple >= second_tuple:
#     print("First tuple >= second tuple")

# print(ord('e'), ord('a'))

# numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# square_tuple = tuple((number, number ** 2) for number in numbers)

# for (number, pow_number) in square_tuple:
#     print(f"{number}: {pow_number}")

# person: dict[str, any] = {
#  "name": "Ali",
#  "age": 30,
#  "city": "Tehran"
# }

# print(person)
# print(person["name"], person.get("name"))

# # print(person["Country"])

# print(person.get("country", "Italy"))

# person["country"] = "Iran"

# del person["name"]

# print(person)

# user: dict = {
#  "username": "ali_azimi",
#  "email": "ali_azimi@example.com",
#  "password": "123456",
#  "profile": {
#         "first_name": "Ali",
#         "last_name": "Azimi",
#         "age": 33,
#         "sex": "male",
#     }
# }

# print(user["email"])
# print(user["profile"]["first_name"])

# for key in user:
#     print(key, user[key])

# for key, value in user.items():
#     print(key, value)

# print("Counting letters in a string".center(50, "-"))
# input_str: str = input("Enter a string: ")

# letter_count_dict = {}

# # letter: 0
# # e: 2
# # input_str = Hello how are you?
# # ouput: {'H': 1, 'e': 2, 'l': 2, 'o': 3, ' ': 3, 'h': 1, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 1, '?': 1}

# for letter in input_str:
#     letter_count_dict[letter] = letter_count_dict.get(letter, 0) + 1

# print("Letter counts".center(50, '-'))

# print(letter_count_dict)

# for (key, value) in letter_count_dict.items():
#     print(f"{key}: {value}")

# number_list = [1,2,3,4,5,6,7,8,9]

# squre_dict = {number: number ** 2 for number in number_list}

# print(squre_dict)

# Gold forex data (Open, Close, Low, High)
gold_data = [
 [1954.32, 1956.78, 1953.15, 1957.24],
 [1956.78, 1958.45, 1955.62, 1959.83],
 [1958.45, 1957.23, 1956.11, 1959.02],
 [1957.23, 1955.67, 1954.89, 1958.15],
 [1955.67, 1953.42, 1952.18, 1956.34],
 [1953.42, 1956.89, 1952.75, 1957.45],
 [1956.89, 1959.34, 1955.92, 1960.27]
]

# open_list = [row[0] for row in gold_data]

# for price in open_list:
#     print(f"{price:.1f} {price:.3f}")

# for row in gold_data:
#     for price in row:
#         print(f"{price:.1f}")


# first_name_list = ["Hadi", "Mahdi", "Hamid", "Sara", "Shahla", "Roya"]
# last_name_list = ["Farhadi", "Rajabi", "Sadri", "Sorian", "Ahmadi", "Dehghan"]


# full_name_list: list = [" ".join([first_name, last_name]) for first_name, last_name in zip(first_name_list, last_name_list)]

# print(full_name_list)

# numbers_set:set = {1, 2, 3, 4, 6, 3, 5}

# print(numbers_set)

# number_set_1 = {1, 2, 3}
# number_set_2 = {1, 2, 3}

# print(number_set_1 == number_set_2 )

# number_set_3 = {3, 2, 1}

# print(number_set_1 == number_set_3)

# # number_list_1 = [1, 2, 3]
# # number_list_2 = [3, 2, 1]

# # print(number_list_1 == number_list_2)

# for item in number_set_1:
#     print(item)

# number_set_1.add(4)
# print(number_set_1)

# number_list: list = [1, 3, 3, 8, 9, 4, 5, 7, 4, 3]

# number_set = set(number_list)

# number_list = list(number_set)

# print(number_list)

# first_number_set: set = {1, 2, 3}
# second_number_set: set = {3, 4, 5}
# print(f"first_number_set: {first_number_set}")
# print(f"second_number_set: {second_number_set}")

# print("Union".center(50, "-"))
# print(first_number_set | second_number_set)

# print("Intersections".center(50, "-"))
# print(first_number_set & second_number_set)

# print("Difference".center(50, "-"))
# print(first_number_set - second_number_set)


# name_set: set = set()
# name_set.add("John")
# name_set.add("Erfan")
# name_set.add("Leila")
# name_set.add("Ali")
# name_set.add("Vahid")
# name_set.add("Karin")

# print("Names".center(50, "-"))
# for (index, name) in enumerate(name_set, start=1):
#     print(f"{index} {name}")

# print("in operator".center(50, "-"))
# if "Hadi" in name_set:
#     print(f"Where are you now, Hadi?")

# student_set: set = {"Erfan", "Leila", "Vahid"}
# print("Subset".center(50, "-"))

# print(f"{student_set.issubset(name_set)}")

# print("Remove".center(50, "-"))
# # name_set.remove("Hadi")
# print(name_set)
# print("Index".center(50, "-"))
# print(name_set[0]) # Error

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result: set[int] = {number**2 for number in numbers if number % 2 != 0}
# print("Set comprehension".center(50, "-"))
# print(result) # output: {1, 9, 25, 49, 81}


# print(f"{all(numbers)}")

# print("any function".center(50, "-"))
# number_list: list = [0, 1, 2, 3, 4]
# print(any(number_list)) # output: True
# message_seen_list: list = [False, False, False, False]
# print(any(message_seen_list)) # output: True

# point_list = [5, 2, 8, 1, 9, 3]
# result = list(reversed(sorted(point_list)))[:3]
# print(result) # [9, 8, 5]

# first_number = 28

# print(id(first_number))

# first_number += 3

# print(id(first_number))

# number_list = [1, 2, 3]

# print(id(number_list))

# number_list.append(24)
# print(id(number_list))


# def change_values(number: int, item_list: list):
#     number += 3
#     item_list.append(124)
#     return number

# print(first_number)
# print(number_list)

# first_number = change_values(first_number, number_list)

# print(first_number)
# print(number_list)


# first_number = 10
# second_number = 10

# print(first_number is second_number)

# first_number_list = [1, 2, 3]
# second_number_list = [1, 2, 3]

# print(first_number_list == second_number_list)
# print(first_number_list is second_number_list, id(first_number_list), id(second_number_list))

# third_number = first_number

# third_number += 3

# print(first_number, third_number)


# third_number_list = first_number_list

# third_number_list.append(55)

# print(first_number_list)
# print(third_number_list)

# forth_number_list = first_number_list[:]

# forth_number_list.append(64)

# print(first_number_list)
# print(forth_number_list)

# print(hash(first_number), hash("first_name"))

import copy

numbers: list = [1, 2, 3, [4, 5, 6]]
print("numbers".center(30, "-"))
print(numbers)
numbers_copy: list = numbers
print("numbers_copy".center(30, "-"))
print(numbers_copy)
print("Copy a list with assignment".center(50, '-'))
numbers_copy.append((1, True))
print(numbers)
print(numbers_copy)

print("Copy a list with copy method".center(50, '-'))
numbers_copy_with_copy_method: list = numbers.copy()
# numbers_copy_with_slicing: list = numbers[:]
# numbers_copy_with_copy_module: list = copy.copy(numbers)
numbers_copy_with_copy_method.append("Thank you")
print(numbers)
print(numbers_copy_with_copy_method)

numbers_copy_with_copy_method[3].append(66)

print(numbers)
print(numbers_copy_with_copy_method)

numbers_copy_with_deepcopy = copy.deepcopy(numbers)

numbers_copy_with_deepcopy.append("Thank you")
print(numbers)
print(numbers_copy_with_deepcopy)

numbers_copy_with_deepcopy[3].append(88)

print(numbers)
print(numbers_copy_with_deepcopy)


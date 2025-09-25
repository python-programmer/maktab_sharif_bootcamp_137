# import math_operation
# from math_operation import add, subract as diff

# import math

# import sys

from person.data import person, set_person

# def add(first_number, second_number):
#     """
#     sum of two number
#     Args:
#         first_number: int, an int number
#         second_number: int, another number
#     Returns:
#         int, sum first_number and second_number
#     """
#     result = first_number + second_number
#     return result


# result = add(12, 13)

# number_list = [1, 2, 3]

# sum_list = sum(number_list)

# print(result, sum_list)

# print(add.__doc__)



# def print_info(name, message):
#     print(f"{message} {name}")


# print_info("hadi", "hello")
# print_info("hello", "hadi")
# print_info("hadi")

# print_info(message="Hello", name="Hadi")


# def power(number: int, pow: int = 2) -> int:
#     result = number ** pow
#     return result


# result = power(10)
# print(result)

# result = power(10, 3)
# print(result)

# numbers: tuple = (23, 48, (1, 3), [1, 2])

# print(numbers)

# print(numbers[1])


# numbers[0] = 24

# def sum_tuple_sequence(numbers):
#     return sum(numbers)


# input = (1, 2, 3, 4, 5)
# result = sum_tuple_sequence(input)

# print(result)

# def sum_tuple_with_args(*args):
#     print(type(args))
#     return sum(args)


# result_with_args = sum_tuple_with_args(1, 2, 3, 4, 5, 7, 8, 32)
# print(result_with_args)

# print(input[2:4])

# person: dict = {
#     "name": "Ali",
#     "age": 23,
#     "city": "Tehran"
# }

# print(person)

# print(person["name"])

# print("dictonary".center(50, '-'))
# for item in person:
#     print(item, person[item])

# print("dictonary with items".center(50, '-'))
# for (key, value) in person.items():
#     print(key, value)

# print("dictonary keys".center(50, '-'))
# print(person.keys())

# print("dictonary values".center(50, '-'))
# print(person.values())

# person.update({'country': 'Iran', 'age': 64})

# print("dictonary update".center(50, '-'))
# print(person)

# print("dictonary item types".center(50, '-'))

# person.update({(1, 2): [752, 423]})
# print(person)

# # Error
# # person.update({[1, 2, 3]: 'Hello'})

# # Error
# # print(person['sex'])

# print("dictonary get".center(50, '-'))

# print(person.get('sex', 0))
# print(person.get('country', 'US'))


# def show_features(**kwargs):
#     print(type(kwargs))
#     for (key, value) in kwargs.items():
#         print(key, value)


# show_features(age=23, height=180, skin_color="white")

# print('kwargs'.center(50, '-'))
# def show_items(value, item=2, *args, **kwargs):
#     print('value is ', value)
#     print('default value is ', item)
#     for item in args:
#         print('args items ', item)
    
#     for (key, value) in kwargs.items():
#         print(key, value)


# show_items(12, 3, 1, 2, 3, 4, 5, items=2, rng=23, name='hello')


# print('kwargs'.center(50, '-'))
# def show_items(value, *args, item=2, **kwargs):
#     print('value is ', value)
#     print('default value is ', item)
#     for item in args:
#         print('args items ', item)
    
#     for (key, value) in kwargs.items():
#         print(key, value)


# show_items(12, 3, 1, 2, 3, 4, 5, items=2, rng=23, name='hello')


# def check_age(age):
#     if age < 18:
#         return 0

#     days = age * 365
#     print(days)

#     return days
#     print("age", age)

# result = check_age(18)
# print(result)

# def print_info(name):
#     print(f"hello {name}")

# result = print_info('Ali')
# print(result, type(result))

# def return_two_values(item_1, item_2):
#     return item_2, item_1


# item_1, item_2 = return_two_values(1, 2)

# print(item_1)
# print(item_2)

# items: tuple = (66, 88)

# item_1, item_2 = items

# print(item_1)
# print(item_2)

# item_1 = 3
# item_2 = 5

# print("item-1", item_1)
# print("item-2", item_2)
# def change_values(first_item, second_item):
#     return second_item, first_item

# item_1, item_2 = change_values(item_1, item_2)

# print("item-1", item_1)
# print("item-2", item_2)


# index = 2

# def increment(count, index_in_func):
#     counter = count

#     index_in_func *= 2

#     print(counter)

#     return index_in_func


# index = increment(10, index)
# print(counter, index)

# numbers = [1, 2, 3]

# squred = []

# for number in numbers:
#     squred.append(number ** 2)


# print(numbers)
# print(squred)

# numbers = [1, 2, 3]

# squred = [number ** 2 for number in numbers]


# print(numbers)
# print(squred)

# print(number)


# numbers = [1, 2, 3]

# message: str = ''

# for number in numbers:
#     message = f"hello {number}"


# print(message)
# print(number)


# number_1 = 12
# number_2 = 48

# result = add(number_1, number_2)

# print(result)

# diff_result = diff(number_1, number_2)
# print(diff_result)

# number = 25

# sqrt = math.sqrt(number)


# print(f"{number} sqrt is {sqrt}")

# print(sys.path)

# print(person)

# first_number = int(input("First Number:"))
# second_number = int(input("Second Number:"))

# result = 0

# try:
#     result = first_number / second_number
#     is_success = True
# except ZeroDivisionError:
#     print("Please don't use zero for second number")
#     is_success = False
# finally:
#     print(f"operation finished {'successfully' if is_success else 'failed'}")

# print(f"{first_number} / {second_number} = {result}")


# def operate():
#     try:
#         first_number = int(input("Enter first number: "))
#         second_number = int(input("Enter second number: "))
#         result: int = first_number / second_number
#         return result
#     except ZeroDivisionError:
#         print("Division by zero")
#     except TypeError as error:
#         print(f"TypeError: {error}")
#     else: # execution ?
#         print("Operation successful")
#     finally:
#         print("End") # execution ?

# result = operate()
# print(result)


# data: dict[str, any] = {
#     "name": "Alex",
#     "age": 22,
#     "city": "San Jose"
# }
# print("Person".center(50, "-"))

# set_person(data)

# print(person)

# data = (1, 2, 3)
# print("Person".center(50, "-"))

# set_person(data)

# print(person)

# file_path = 'users.txt'
# file = open(file_path, 'r', encoding='utf-8')

# for line in file:
#     print(line)

# file.close()

# Copying a file
# source_file = None
# dest_file = None
# try:
#     source_file = open('users.txt', 'r', encoding='utf-8')
#     dest_file = open('copy.txt', 'w', encoding='utf-8')
#     source_file.
#     content = source_file.read()
#     dest_file.write(content)
#     print('copying done')
# except FileNotFoundError:
#     print('The source file was not found.') # TWO ++ gift: why do we only show this error for source file
# except IOError as e:
#     print(f'I/O Error: {e}')
# finally:
#     if source_file:
#         source_file.close()
#     if dest_file:
#         dest_file.close()


# import datetime

# file = None
# try:
#     file = open('03.Files & Exceptions.pdf', 'a', encoding='utf-8')
#     now = datetime.datetime.now()
#     file.write(f'login time: {now}\n')
#     print('Your login time store successfully!')
# except IOError as e:
#     print(f'writing to file error: {e}')
# finally:
#     if file:
#         file.close()


try:
    with open('users.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")


# divide_by = requests()

# try:
#     result = 10 / divide_by
# except ZeroDivisionError:
#     print("zero division")

# age ino goft, manam no

# if he_said == "don't":
#     print("no")

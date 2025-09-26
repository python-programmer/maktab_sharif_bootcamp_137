
# bank_gatway = {
#     "saman": pay_saman,
#     "ayandeh": pay_ayandeh
# }

# design patterns, factory method
# def pay(bank_gatway, name):
#     bank_gatway[name]()


# def add(first_number, second_number):
#     return first_number + second_number


# def add_and_print(func, first_number, second_number):
#     result = add(first_number, second_number)
#     print(f"{first_number} + {second_number} = {result}")


# add_function = add
# add_and_print(add_function, 5, 6)
# result = add(5, 6)
# print(result)


# add = lambda first_number, second_number: first_number + second_number

# print(add(10, 12))

# show = lambda first_number: print(first_number)

# show(12)

numbers = [1, 2, 3, 4, 5, 6]

# square_numbers = list(map(lambda number: number ** 2, numbers))

# print(numbers)
# print(square_numbers)


# def square_number(number):
#     return number ** 2

# square_number = list(map(square_number, numbers))

# print(numbers)
# print(square_number)


# char_list: list[str] = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

# ordinal_char_number: list[int] = list(map(ord, char_list))

# print(char_list)
# print(ordinal_char_number)

# for (letter, ordintal) in zip(char_list, ordinal_char_number):
#      print(f"{letter}: {ordintal}")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # even_numbers = list(filter(lambda number: not number % 2, numbers))

# # print(even_numbers)

# square_list = list(map(lambda number: number ** 2, filter(lambda item: item % 2, numbers)))

# print(numbers)
# print(square_list)

from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# # 1 + 2 = 3
# # 3 + 3 = 6
# # 6 + 4 = 10
# # 10 + 5 = 15

# total = reduce(lambda first_number, second_number: first_number + second_number, numbers)

# print(total)

# 6! = 6 * 5 * 4 * 3 * 2 * 1

# number: int = 6

# number_placeholder = number

# multiply = 1

# while number > 0:
#     multiply *= number
#     number -= 1

# print(f"{number_placeholder}! = {multiply}")

# number_fact_list = range(1, number_placeholder + 1) 

# factorial_result = reduce(lambda first_number, second_number: first_number * second_number, number_fact_list, 1)

# print(f"{number_placeholder}! = {multiply}")


add = lambda first_number, second_number: first_number + second_number

# def add(first_number, second_number):
#     return first_number + second_number

# print(f"{12} + {14} = {add(12, 14)}")

# words = ["apple", "kiwi", "banana", "orange"]

# word_length_list = list(map(lambda fruit: len(fruit), words))

# print(word_length_list)

# word_size_length = []
# for word in words:
#     word_size_length.append(len(word))

# print(word_size_length)


# number_tuple = ([1, 2], [3, 4], [5, 6])

# print(hash(number_tuple))

# number_tuple[0].append(15)

# sorted_tuple = sorted(number_tuple, key=lambda number: number[1], reverse=True)

# print(sorted_tuple)

# print(number_tuple)

# number_list = [1, 2, 3, 4, 6]

# square_list = list(map(lambda number: number ** 2, number_list))

# # number_str = "645"
# # number_int = int(number_str)

# for number, pow_number in zip(number_list, square_list):
#     print(f"{number}**2: {pow_number}")


# age = 18
# yaraneh_level = 5

# if age >= 18 and yaraneh_level < 3:
#     print(f"you get 400$")

# if yaraneh_level > 4 and yaraneh_level < 7:
#     print("you'll get 300$")
# else:
#     print("you're not elligable")


# add = lambda first_number: first_number ** 3 if first_number % 3 == 0 else first_number ** 4


# number_list = [5, 10, 15, 20, 35, 40, 45, 50]

# divide_by_2_list = filter(lambda number: 10 <= number <= 40 and number % 2 == 0, number_list)

# memory management
# number_list_divide_by_2_1 = list(divide_by_2_list)
# number_list_divide_by_2_2 = list(divide_by_2_list)

# print(number_list_divide_by_2_1)
# print(number_list_divide_by_2_2)

# number = 12

# if number % 2:
#     pass

# from functools import reduce

# number_list = [1, 2, 3, 4, 5]
# # 6 + 0 = 6
# # 6 * 1 = 6

# # 3
# # 6
# # 10
# # 15

# sum_of_numbers = reduce(lambda first_item, second_item: first_item + second_item, number_list, 10)

# print(f"Sum of {number_list} = {sum_of_numbers}")

# print(sum(number_list))


# numbers = (number ** 2 for number in range(10))

# print(f"First hit".center(50, '-'))
# for number in numbers:
#     print(number)

# print(f"Second hit".center(50, '-'))
# for number in numbers:
#     print(number)


# pagination
# def read_users(file_name, size = 2):
#     try:
#         with open(file_name, 'r') as file:
#             count = 1
#             result = file.readline()
#             while result:
#                 result += file.readline()
#                 count += 1

#                 if count == size:
#                     yield result
#                     count = 1
#                     result = file.readline()

#     except FileNotFoundError:
#         print(f"{file_name} does not exists")


# fatemi
# def read_users(file_name, size=2):
#     with open(file_name, 'r') as file:
#         result = ""
#         for line in range(size):
#             result += file.readline()
#             if result == "":
#                 break
#         yield result


# file_name = "users.txt"

# for lines in read_users(file_name):
#     print(lines)



# sentence = "Hadi farhadi is here"
# output = ["Hadi"]

# word_cache = {}

# def cache(function):
#     def wrapper(*args, **kwargs):
#         word_cache[] = []
#         result = function(*args, **kwargs)
#         return result
#     return wrapper

# @cache
# def find_number_of_occurance(word_list, sentence):
#     # sentence.lower()

#     for word in word_list:
#         if word.lower() in sentence.split(" "):
#             pass

# def remove_punction(sentence): # fix me: need imporment
#     pass

# sentence = remove_punction(sentence)
# find_number_of_occurance()


numbers_cache = {}


def cache_numbers(function):
    def wrapper(*args, **kwargs):
        result = numbers_cache.get((args[0], args[1]))
        if result:
            pass
        else:
            result = function(*args, **kwargs)
            numbers_cache[(args[0], args[1])] = result
        return result
    return wrapper


@cache_numbers
def add(first_number, second_number):
    print("I met here")
    return first_number + second_number

print(add(12, 13))
print(add(12, 13))
print(add(12, 13))
print(add(12, 13))

print(add(13, 12))

# number_list = [1, 2, 3, 4, 5]


# def get_number(numbers):
#     index = 0
#     number = numbers[index]
#     index += 1
#     return number


# print(get_number(number_list))
# print(get_number(number_list))
# print(get_number(number_list))
# print(get_number(number_list))


# # def get_number_with_generator(numbers):
# #     index = 0
# #     number = numbers[index]
# #     index += 1
# #     yield number
# #     number = numbers[index]
# #     index += 1
# #     yield number
# #     number = numbers[index]
# #     index += 1
# #     yield number

# # def get_number_with_generator(numbers):
# #     for number in numbers:
# #         yield number


# number_generator = get_number_with_generator(number_list)

# # print(next(number_generator))
# # print(next(number_generator))
# # print(next(number_generator))

# # print("List with generator".center(50, '-'))
# # for number in get_number_with_generator(number_list):
# #     print(number)

# # print("List".center(50, '-'))
# # for number in number_list:
# #     print(number)


# # def indefinite_generator():
# #     index = 0
# #     while True:
# #         index += 1
# #         yield index


# # print("Inf generator".center(50, '-'))
# # inf_generator = indefinite_generator()
# # for index in range(10):
# #     print(next(inf_generator))

# import time

# def get_numbers(size:int):
#     number: int = 0
#     while number < size:
#         yield number
#         number += 1

# start_time = time.time()
# for number in get_numbers(10):
#     print(number)
# end_time = time.time()


# print("Generation time".center(50, '-'))
# print(end_time - start_time)


# start_time = time.time()
# for number in range(10):
#     print(number)
# end_time = time.time()
# print("List time".center(50, '-'))
# print(end_time - start_time)


# def simple_decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
    
#     return wrapper


# def add():
#     print(f"add")


# add()

# decorator_result = simple_decorator(add)

# decorator_result()

# @simple_decorator
# def add():
#     print(f"add")

# add()


# def first_decorator(number: int):
#     def calculator(func):
#         def warpper(*args, **kwargs):
#             print(args)
#             print(kwargs)
#             result = func(*args, **kwargs)

#             return result * number
#         return warpper
#     return calculator


# @first_decorator(3)
# def add(first_number, second_number):
#     return first_number + second_number

# print(add(1, 2))


# import time


# def time_calculator(function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = function(*args, **kwargs)
#         end_time = time.time()
#         print(f"{function.__name__} execution time: {end_time - start_time}")
#         return result
#     return wrapper

# @time_calculator
# def get_numbers(size:int):
#     number: int = 0
#     while number < size:
#         yield number
#         number += 1

# start_time = time.time()
# for number in get_numbers(10):
#     print(number)
# end_time = time.time()


# print("Generation time".center(50, '-'))
# print(end_time - start_time)


# start_time = time.time()
# for number in range(10):
#     print(number)
# end_time = time.time()
# print("List time".center(50, '-'))
# print(end_time - start_time)

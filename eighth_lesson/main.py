
# def factorial(number: int):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)


# number = 1001
# # 6 * 5 * 4 * 3 * 2 * 1

# reuslt = factorial(number)

# print(f"{number}! = {reuslt}")

# # 1 5 6 8

# record a
def fib(number: int):
    if number <= 1:
        return number
    else:
        return fib(number-1) + fib(number-2)

number = 6

result = fib(number)
print(f"fib({number}) = {result}")
# end record a

# record b
for index in range(1, number + 1):
    print(fib(index), end=", ")

# end record b


# number = 1 + 2 - 3 * (8 + 5)
# stack list, append(), pop()


def check_age_1(age: int):
    if age < 18:
        return False
    else:
        return True

def check_age_2(age: int):
    if age < 18:
        return False
    return True
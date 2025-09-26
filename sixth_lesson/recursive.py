
def factorial(number: int):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Additional LIFO - Stack

# 1, 2, 3

number = 1001

result = factorial(number)

print(f"{number}! {result}")

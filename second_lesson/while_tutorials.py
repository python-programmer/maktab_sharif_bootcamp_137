count: int = 5

while count > 0:
    print(count)

    if count < 3:
        break

    count -= 1

    print("Done")

else:
    print("item")


fruits: list = ["apple", "banana", "kiwi", "orange"]

index: int = 0

print(len(fruits))

while index < len(fruits):
    print(fruits[index])
    index += 1

print("throw it")

for fruit in fruits:
    print(fruit)

# for i in range(10):
#     print(i)

for i in range(1, 10):
    print(i)

print(fruits[0:2])

float_numbers: list = [1.2, 3.4, 5.6, [25, 48], [True, False], 'str', ['Ali', 23, 12.5]]

for number in float_numbers:
    print(number)


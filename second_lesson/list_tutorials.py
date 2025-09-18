numbers: list = [1, 2, 8, 3, 4, 8]

print(numbers[185])

numbers[1] = 198

print(numbers)

numbers.append(33)

print(numbers)

if 3 not in numbers:
    print("We're happy")


numbers.remove(3)

print(numbers)

index: int = numbers.index(8)

print(index)

number_count: int = numbers.count(8)

print(number_count)

del numbers[1]

print(numbers)

result: int = sum(numbers)
print("sum numbers", result)

max_item: int = max(numbers)
print("max numbers", max_item)

sorted_list: list = sorted(numbers)
print(sorted_list)

print("the gold medal ", sorted_list[-1])

sorted_list_desc: list = sorted(numbers, reverse=True)

print(sorted_list_desc)

print("the gold medal ", sorted_list_desc[0])

numbers[1] = 1024

numbers.insert(1, 1024)

print(numbers)

fruits: list = ['banana', 'kiwi', 'apple']

fruits.sort()

print(fruits)

print(len(fruits))
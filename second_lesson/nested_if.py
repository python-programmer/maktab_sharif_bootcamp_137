age: int = 32
name: str = "Ali "

if age > 18:
    name += "S"
    if len(name) > 4:
        print("It's good")
    else:
        print("No we dont need you")
else:
    print("No we cant find the best things")

if age > 18:
    if len(name) > 4:
        print("Yes")
    else:
        print("No")
else:
    print("No")


# if age > 18 and len(name) > 4:
#     print("Yes")
# else:
#     print("No")

# result = 0.1 + 0.2
# print("result ", result == 0.1 + 0.2)
# if result == 0.3:
#     print("Equal")
# else:
#     print("Not equal")

result: int = 25

if result >= 26:
    pass
else:
    print("hello")
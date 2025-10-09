import stack
import list_type

first_number = 10

second_number = 12

# a = > b, c => a , b => a

print(f"first_number = {first_number}, second_number = {second_number}")


# temp = first_number

# first_number = second_number

# second_number = temp

# print(f"first_number = {first_number}, second_number = {second_number}")

first_number, second_number = second_number, first_number


print(f"first_number = {first_number}, second_number = {second_number}")


# age = 18

# if age >= 18:
#     print("You can watch this video")
# elif age >= 15:
#     print("You can watch first 10 mins")
# else:
#     print("You can't watch this video")


# username = input("Username:")
# password = input("Password:")
# verification_code = input("Code:")

# if username == "hadi" and password == "123456":
#     print("You logged in successfully")
# else:
#     print("Username or password is invalid")


# if username == "hadi":
#     if password == "123456":
#         if verification_code == "1234":
#             print("You logged in successfully")
#         else:
#             print("verification code is invalid")
#     else:
#         print("User not found")
# else:
#     print("User not found")

# is_authenticated = False

# if username == "hadi" and password == "123456" and verification_code == "1234":
#     is_authenticated = True
#     print("You logged in successfully")
# else:
#     print("user not found")


# if is_authenticated:
#     print("you can check out your basket")
# else:
#     print("You can't access this resource")



# user_roles = ["Admin", "User", "Moderator"]
# user_age = 18


# if "Admin" in user_roles:
#     print("Yes, I'm God")
# else:
#     print("No, You don't have this permission")

# if user_age >= 18:
#     user_roles.append("Super Hero")

# print(user_roles)
# print(f"length of user_roles is {len(user_roles)}")

# sorted_roles = sorted(user_roles)

# print(sorted_roles)
# print(sorted_roles[1])
# print(sorted_roles[1:3])
# print(sorted_roles[5:6])

# print(sorted_roles[1:-1])


# is_authenticated = True

# if is_authenticated:
#     user_roles.extend(["Gamers", "Players"])

# print(user_roles)

# print(user_roles + ["IsOK", "Gods"])

# user_roles.reverse()

# roles = list(reversed(user_roles))

# print(user_roles)
# print(roles)

# print("Stack".center(50, '-'))
# stack.push(11)
# stack.push(12)
# stack.push(13)
# stack.push(14)
# stack.push(15)
# stack.show()

# result = stack.pop()

# print(result)

# stack.show()

# print("List".center(50, '-'))
# list_type.set_item(10)
# list_type.set_item(12)
# list_type.set_item(13)
# list_type.set_item(14)
# list_type.set_item(15)

# list_type.show()

# print(list_type.get_item())
# list_type.show()


# is_authenticated = False
# access_token = ""

# while not is_authenticated:
#     username = input("Username:")
#     password = input("Password:")

#     if username == "parsa" and password == "123456":
#         is_authenticated = True
#         access_token = "afdfsafsafdhsafasfsa.dfasfafsafafd.dfasfsafsa"
#         print("You logged in successfully")
#     else:
#         print("User not found")

# print(access_token)

# numbers = [1, 2, 3, 4, 5, 6]
# counter = 0
# total = 0

# while counter < len(numbers):
    
#     print(numbers[counter])
#     if numbers[counter] % 2 == 0:
#         counter += 1
#         break
#     else:
#         counter += 1
#         continue

#     print(f"Yes, we found a even number {numbers[counter]}")

# import random


# print("Welcome".center(100 , "-"))


# print("Rock Paper Scissors".center(100, "-"))

# while True:


#     choices = ["rock", "paper", "scissors"]

#     computer = random.choice(choices)

#     player = input("choose rock, paper, or scissors: ")
#     player = player.lower()

#     print("your choice : " ,player)

#     print("computer choice :" ,computer)

#     if player not in choices:

#         continue


#     if computer == player:

#         print(" ha ha a tie!")


#     elif computer == "scissors":

#         if player == "rock":

#             print("you win")


#     elif computer == "rock":

#         if player == "scissors":

#             print("you lost")


#     elif computer == "scissors":

#         if player == "paper":

#             print("you lost")


#     elif computer == "paper":

#         if player == "scissors":

#             print("you win")


#     elif computer == "paper":

#         if player == "rock":

#             print("you lost")


#     elif computer == "rock":

#         if player == "paper":

#             print("you win !")


#     play_again = input("Do you want to play again? (y/n): " ).lower()

#     if play_again != "y":

#         break

# print("written by PARSA")


# counter = 0
# indexer = 0

# is_ended = False

# while counter < 5:
#     while indexer < 5:
#         print("Start")

#         if counter == 3 or indexer == 4:
#             is_ended = True
#             break

#         indexer += 1
#     counter += 1
#     indexer = 0
#     print("I'm here")
#     if is_ended:
#         break

# print("finished")

numbers = [1, 2, 3, 4, 5, 6]

# for number in numbers:
#     print(number)


# for number in range(1, 7):
#     print(number)

# for number in range(6): [0, 1, 2, 3, 4, 5]
#     if number % 2 == 0:
#         print(number)
#         break


# for number in range(1, 10):
#     for index in range(1, 10):
#         print(f"{number} * {index} = {index * number}")


# radar 12421

input_str = input("Enter A Word:")

index = 0
counter = -1

is_palindrome = True

while index < len(input_str) / 2:
    if input_str[index] != input_str[counter]:
        is_palindrome = False
        break

    index += 1
    counter -= 1

print(f"{input_str} is Palindrome {is_palindrome}")


reversed_input = ''.join(list(reversed(input_str)))

print(reversed_input == input_str)

print(input_str[::-1] == input_str)
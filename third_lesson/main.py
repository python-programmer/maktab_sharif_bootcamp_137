# import user_handler
from data_handler import get_user_data, get_user_dict_data
from user_handler import print_users as show_users, grouping

# id, full_name, sex, age
USERS: tuple = ((1, "Hadi Farhadi", "M", 38), (2, "Yasin Alvi", "M", 28),
                (3, "Mahnaz Afshar", "F", 45), (4, "Zahra Ahmadi", "F", 19), )

# print(USERS[0][1])

# print("id\tfull name\tsex\tage")

# for user in USERS:
#     print(user[0], user[1], user[2], user[3], sep="\t")


# def print_users(first_user, second_user, is_admin=True):
#     """
#     It joins all users

#     Args:
#         first_user: tuple the first user'

#     Returns
#         int: count of users
#     """
#     print("it's a placeholder", is_admin)
#     return f'{first_user[1]} {second_user[1]}' 


# result: str = print_users(USERS[0], USERS[1])
# print('result is ', result)

# print(print_users.__doc__)


# def print_users(user_list):
#     """
#     It shows all users

#     Args:
#         first_user: tuple the first user'

#     Returns
#         int: count of users
#     """
#     print("id\tfull name\tsex\tage")

#     for user in user_list:
#         print(user[0], user[1], user[2], user[3], sep="\t")

# user_data = get_user_data()
# show_users(user_data)

# get_user_dict_data()

numbers: dict = {
    'item1': 3,
    'item2': 45,
    'item3': True,
    'item4': {'name': 'Hello'},
    'item5': [1, 3, 'yes']
}

# print(numbers['item5'].sort())

# for item in numbers:
#     print(item, numbers[item])


users = get_user_dict_data()

print(users[1]['age'])

groups: tuple = ('Barcellona', 'Real Madrid')
group_size = 2

grouping(users, groups, group_size)

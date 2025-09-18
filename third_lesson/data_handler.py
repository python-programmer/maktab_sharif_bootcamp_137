# id, full_name, sex, age
USERS: tuple = ((1, "Hadi Farhadi", "M", 38), (2, "Yasin Alvi", "M", 28),
                (3, "Mahnaz Afshar", "F", 45), (4, "Zahra Ahmadi", "F", 19), )


def get_user_data():
    return USERS


def get_user_dict_data():
    users: dict = {}

    user_list = get_user_data()

    for user in user_list:
        users[user[0]] = {
            'full name': user[1],
            'sex': user[2],
            'age': user[3]
        }

    return users



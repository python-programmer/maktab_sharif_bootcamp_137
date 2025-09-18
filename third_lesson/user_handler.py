import datetime
import random

# from datetime.datetime import now

def print_users(user_list):
    """
    It shows all users

    Args:
        first_user: tuple the first user'

    Returns
        int: count of users
    """
    print(f"Report date: {datetime.datetime.now()}")
    print("id\tfull name\tsex\tage")

    for user in user_list:
        print(user[0], user[1], user[2], user[3], sep="\t")


def grouping(user_data, group_list, size = 2):
    groups = {}

    for group in group_list:
        groups[group] = []

    # print(groups)

    count = 0

    while count < len(user_data):
        random_group = random.randint(0, len(group_list) - 1)

        if len(groups[group_list[random_group]]) >= size:
            continue

        # FIXME: use get insead of these code
        groups[group_list[random_group]].append(user_data[count + 1])

        # FIXME: insert only two user in each groups

        count += 1


    print(groups)

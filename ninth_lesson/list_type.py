

list_item = []

# List 1, 2, 3, 4, 5


def get_item(index = 0):
    return list_item.pop(index)


def set_item(item):
    list_item.append(item)


def show():
    print(list_item)
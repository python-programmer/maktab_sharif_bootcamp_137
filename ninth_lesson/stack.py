

# Stack = 1, 2, 3, 4, 5, 6

# طراحی الگوریتم و ساختمان داده

stack = []

from new_feature.abcd import show as show_abcd

def push(item):
    stack.append(item)


def pop(index = -1):
    return stack.pop(index)


def show():
    show_abcd()
    print(stack)

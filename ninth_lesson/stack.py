

# Stack = 1, 2, 3, 4, 5, 6

# طراحی الگوریتم و ساختمان داده

stack = []

def push(item):
    stack.append(item)


def pop(index = -1):
    return stack.pop(index)


def show():
    print(stack)

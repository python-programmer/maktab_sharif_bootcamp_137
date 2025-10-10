def add(first_number, second_number):
    if not isinstance(first_number, int):
        raise ValueError(f"{first_number} must be an int")
    if not isinstance(second_number, int):
        raise ValueError(f"{second_number} must be an int")
    return first_number + second_number

def subtract(first_number, second_number):
    assert isinstance(first_number, int)
    assert isinstance(second_number, int)
    return first_number - second_number

def mutiply(first_number, second_number):
    assert isinstance(first_number, int)
    assert isinstance(second_number, int)
    return first_number * second_number

def divide(first_number, second_number):
    assert isinstance(first_number, int)
    assert isinstance(second_number, int)
    return first_number / second_number

def divide_whole(first_number, second_number):
    assert isinstance(first_number, int)
    assert isinstance(second_number, int)
    return first_number // second_number

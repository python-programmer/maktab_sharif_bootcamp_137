def sort_by(numbers, sort_by_func, reverse = False):
    return sorted(numbers, key=sort_by_func, reverse=reverse)
def great(name: str, message: str) -> None:
    print(f"{name}: {message}")


great("Hasan", "Explain Contiue")

array = [1, -1, 5, -5, 0, 8]

def get_sum_of_values(number_list):
    if not isinstance(number_list, list):
        return None

    else:
        return sum(number_list)


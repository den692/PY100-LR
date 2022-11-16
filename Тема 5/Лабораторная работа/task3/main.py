def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел

from random import shuffle


def get_list_unique_numbers() -> list[int]:
    numbers = list(range(-10, 11))
    shuffle(numbers)
    return numbers[: 15]


get_list_unique_numbers = get_list_unique_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) ==len(set(list_unique_numbers)))

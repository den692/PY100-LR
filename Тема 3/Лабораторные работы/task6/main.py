list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
list_numbers = [1, 3, 5, 7, 2, 3, 4]

max_number = max(list_numbers)
index_max = list_numbers.index(max_number)
list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)

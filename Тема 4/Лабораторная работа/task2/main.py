def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_count_char(s: str) -> dict [str, int]:
    counts: dict[str, int] = dict()
    s = s.lower()
    alphabet = set([char for char in s if char.isalpha()])
    for char in alphabet:
        counts[chat] = s.count(char)

        return counts
def get frequence_char(count_char: dect[str, int]) -> dict[str, float]:
    freguency: dict[str, float]
    all_count = sum(count_ char.values())

    for char, count in count_char.items():
        freguency[char] = count / all_count

        return freguency


main_str = "TEst text. It is very simple Example"
counts = get_count_char(main_str)
print(counts)
print(get_count_char(main_str))

def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
from random import sample
from string import ascii_lowercase, ascii_uppercase, digits

def get_random_password(length: int = 8) ->str:
    return ''. join(sample(ascii_uppercase + ascii_lowercase + digits, length))


print(get_random_password())

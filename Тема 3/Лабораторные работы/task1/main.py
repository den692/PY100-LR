src = not False and True or False and not True

# TODO расписать упрощение выражения

result =not False and True or False and not True
result = False and True or False and True
result = True or False
result = True
print(src == result)

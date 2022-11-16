salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def calculate_need_money(salary=salary, spend=spend, increase=increase,months=months) -> int:
need_money = 0
for i in range(months):
    need_money = need_money + salary - spend
    spend *= 1 + increase
    need_money = abs(need_money)
    if need_money - int (need_money) == 0:
        return int (need_money)
    else:
        return int (need_money) + 1

need_money = calculate_need_money()
print(need_money)

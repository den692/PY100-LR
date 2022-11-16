money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
def calculate_month(capital=money_capital, salary=salary, spend=spend, increase=increase) -> int:
    month = 0
    while capital >= 0:
        capital = capital + salary - spend
        spend *= 1 + increase
        month += 1

    return month - 1


month = calculate_month()
print(month)

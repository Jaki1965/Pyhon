# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.

revenue = float(input('Введите цифрами (положительное число) объем выручки фирмы: ' ))
cost = float(input('Введите цифрами (положительное число) объем издержек фирмы за тот же период: '))
profit = revenue - cost
if profit > 0:
    profitability = (profit / revenue)*100
    profitability = round(profitability, 2)
    print(f'Прибыль фирмы ссотавила {profit} денежных единиц')
    print(f'Рентабельность деятельности фирмы составила {profitability}%')
    employees = int(input('Пожплуйста, введите количство сотрудников фирмы: '))
    profit_employee = profitability / employees
    profit_employee = round(profit_employee, 2)
    print(f'Прибыль на одного сотрудника составила {profit_employee} денежных единиц')

elif profit < 0:
    profit = profit*-1
    print(f'Убытки фирмы ссотавили {profit} денежных единиц')
else:
    print(f'Результат деятельности фирмы {profit} денежных единиц')

# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введите целое число: '))
number_1 = user_number
number_2 = int(f'{user_number}{user_number}')
number_3 = int(f'{user_number}{user_number}{user_number}')
result = number_1 + number_2 + number_3
print(result)
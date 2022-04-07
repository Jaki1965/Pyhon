# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input('Bведите целое положительное число: '))
remains = number % 10
number = number // 10
while number > 0:
    if number % 10 > remains:
        remains = number % 10
    number = number // 10
print(remains)



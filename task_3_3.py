# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    lis_1 = [x, y, z]
    lis_1.sort()
    result = sum(lis_1[-2:])
    return result

print(my_func(22, 11, 5))


# Вариант пользовательского ввода

x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
z = float(input('Введите третье число: '))
print(my_func(x, y, z))
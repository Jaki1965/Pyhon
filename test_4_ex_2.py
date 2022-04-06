# Заняте 4 ФУНКЦИИ
# Homework 2
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
def max_3():
    numbers = []
    for number in range (3):
        number = int(input('Введите любое число: '))
        numbers.append(number)
        print(numbers)
        print(max(numbers))

max_3()

# Как решено у мудаков

def get_max(a, b, c):
    result = max([a, b, c])
    return result



i = get_max(22, 55, 78)
print(i)
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Mistake(Exception):
    def __init__(self, txt):
        self.txt = txt

class Complex_number:
    def __init__(self, number):
        self.number = number
        try:
            if type(self.number) != complex:
                raise TypeError(f'Формат введенного аргумента не комплексное число\n'
                                f'Пожалуйста введите комплексное число вида (r+nj. Напиример (5+2j)')
        except TypeError as err:
            print(err)

    def __add__(self, other):
        return f'{self.number + other.number}'


    def __mul__(self, other):
        return f'{self.number*other.number}'


a = Complex_number(4+2j)
b = Complex_number(3+2j)
print(a + b)
print(a*b)

# Проверка результата
x = complex(4,2)
y = complex(3,2)
m = x + y
print(m)
k = x*y
print(k)


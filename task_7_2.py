# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Atelier(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def print_color(self, color):
        print(f'Цвет выбранного изделия {self.color}')


class Clothes(Atelier):

    def __init__(self, color):
        self.color = color
        self.__name = 'Брюки'

    def get_clothes_name(self):
        return self.__name

    def set_clothes_name(self):
        self.__name = 'Штаны'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def info_clothes(self):
        print(f'Вы интересовались одежой {self.__name}\nЦвет: {self.color}')


    def print_color(self, color):
        print(f'Цвет выбранного изделия {self.color}')


class Coat(Clothes):

    def __init__(self, color, size):
        Clothes.__init__(self, color)
        self.size = size

    def print_color(self, color):
        print(f'Цвет выбранного пальто {self.color}')

    def get_cost(self):
        self.cost_fabric = self.size * 2.0 + 0.3
        print(f'Расход ткани на ваше пальто:\nЦвет: {self.color}\nСоставил - {self.cost_fabric}')

    def __str__(self):
        return f'Цвет {self.color}, Размер {self.size}'



class Suit(Clothes):
    def __init__(self, color, height):
        Clothes.__init__(self, color)
        self.height = height

    def print_color(self, color):
        print(f'Цвет выбранного костюма {self.color}')

    def get_cost(self):
        self.cost_fabric = self.height * 6.5 + 0.5
        print(f'Расход ткани на ваш костюм:\nЦвет: {self.color}\nСоставил - {self.cost_fabric}')

    def __str__(self):
        return f'Цвет {self.color}, Рост {self.height}'
    pass

my_coat = Coat('blue', 43)
print(my_coat)
my_coat.get_cost()
my_suit = Suit('black', 18)
print(my_suit)
my_suit.get_cost()
my_cloth_name = Clothes('green')
#print(my_cloth_name.__name) Не будет работать, выдаст ошибку: 'Clothes' object has no attribute 'name'
# Так как атрибут класса __name = 'Брюки' ПРИВАТНЫЙ
print(my_cloth_name.get_clothes_name()) # через метод вернет
my_cloth_name.set_clothes_name() # метод присвения нового значения приватному атрибуту
print(my_cloth_name.get_clothes_name()) # метод получения значения приватного атрибута
my_cloth_name.info_clothes() # отдельным методом получаем информацию об одежде
my_cloth_name.name = 'Штанищи' # через setter (@name.setter) меняем название одежды на Штанищи
my_cloth_name.info_clothes() # получаем измененное значение приватного атрибута
print(my_cloth_name.name) # через getter (@property) получем измененнеое название одежды на Штанищи
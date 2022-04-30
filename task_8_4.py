# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod

class Stosk(ABC):
    def __init__(self):
        self.type_stock = type_stock

    @abstractmethod
    def get_at_stock(self, type, amount): # Обязательный метод получение товара
        self.type = type
        self.amount = amount

    @abstractmethod
    def transfer_from_stock(self, type, amount): # Обязательный метод списание товара
        self.type = type
        self.amount = amount

# Сооздаем базовый класс. Идея в том, чтобы в базовом классе (типа центрального склада)
# отражались все изменения сделаные на локальных складах

class Office_eq(Stosk):
    stock = {'Принтер': 10,
             'Сканер': 7,
             'Ксерокс': 12,
                  }
    def __init__(self):
        self.stock = Office_eq.stock
        print(f'Всего на складах:')
        for k, v in self.stock.items():
            print(f'{k} {v} шт.')


    def get_at_stock(self, type, amount):
        self.type = type
        self.amount = amount

    def transfer_from_stock(self, type, amount):
        self.type = type
        self.amount = amount

    @staticmethod
    def info_stock():
        for k, v in Office_eq.stock.items():
            print(f'{k} {v} шт.')


# Сооздаем класс - наследник. Идея в том, чтобы был внутри статистический метод
# с помощью котрого из любого экземпляра класса можно было получить информацию о состоянии
# базового класса - центрального склада.
# уникальным параметром для каждого класса наследника является название типа оборудования
# self.name = 'Принтеры'
# self.name = 'Сканеры'
# self.name = 'Ксероксы'

class Printer(Office_eq):
    def __init__(self):
        self.name = 'Принтеры'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] + self.amount
        self.total_p = Office_eq.stock['Принтер']
        print(f'Поступило принтеров: {self.amount}')
        print(f'С учетом поступления, на складах принтеров всего: {self.total_p}')

    def transfer_from_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] - self.amount
        self.total_p = Office_eq.stock['Принтер']
        print(f'Выдано принтеров со склада: {self.amount}')
        print(f'С учетом списания, на складах принтеров всего: {self.total_p}')


class Scaner(Office_eq):
    def __init__(self):
        self.name = 'Сканеры'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] + self.amount
        self.total_p = Office_eq.stock['Сканер']
        print(f'Поступило сканеров: {self.amount}')
        print(f'С учетом поступления, на складах сканеров всего: {self.total_p}')

    def transfer_from_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] - self.amount
        self.total_p = Office_eq.stock['Сканер']
        print(f'Выдано сканеров со склада: {self.amount}')
        print(f'С учетом списания, на складах сканеров всего: {self.total_p}')


class Xerox(Office_eq):
    def __init__(self):
        self.name = 'Ксероксы'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] + self.amount
        self.total_p = Office_eq.stock['Ксерокс']
        print(f'Поступило ксероксов: {self.amount}')
        print(f'С учетом поступления, на складах ксероксов всего: {self.total_p}')

    def transfer_from_stock(self, type, amount):
        self.type = type
        self.amount = amount
        Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] - self.amount
        self.total_p = Office_eq.stock['Ксерокс']
        print(f'Выдано ксероксов со склада: {self.amount}')
        print(f'С учетом списания, на складах ксероксов всего: {self.total_p}')



a = Office_eq()
b = Printer()
b.get_at_stock('Принтер', 5) # Поступление на склад 5 принтеров изменения должны пройти во всех экземплярах класса.
print(a.stock) # В экземпляре a - изменение отразилось
print(b.stock) # В экземпляре b - изменение отразилось
a.info_stock() # статистическим методом проверяем экземпляры класса
b.info_stock() # статистическим методом проверяем экземпляры класса
b.transfer_from_stock('Принтер', 7) # Списание со склада 7 принтеров изменения должны пройти во всех экземплярах класса.
a.info_stock() # Прверил все ок отразился и приход и списание
b.info_stock() # Прверил все ок отразился и приход и списание
c = Scaner()
c.info_stock()
c.transfer_from_stock('Сканер', 6)
c.get_at_stock('Сканер', 17)
a.info_stock()
b.info_stock()
c.info_stock() # все отразилось во всех экземплярах и в базовом классе. Общий склад ведет сябя правильно
d = Xerox()
d.info_stock()
d.transfer_from_stock('Ксерокс', 4)
c.get_at_stock('Сканер', 12)
a.info_stock()
b.info_stock()
c.info_stock()
d.info_stock() # все отразилось во всех экземплярах и в базовом классе. Общий склад ведет сябя правильно






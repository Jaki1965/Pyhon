# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

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

# Сделеал две функции в базовом классе для проверки значений:
# тип оборудования check_type_eq и количество check_amount
#
class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


class Office_eq(Stosk):
    stock = {'Принтер': 10,
             'Сканер': 7,
             'Ксерокс': 12,
                  }
    def __init__(self):
        self.stock = Office_eq.stock
        print(f'Первое сообщение центрального склада - Всего на складах:')
        for k, v in self.stock.items():
            print(f'{k} {v} шт.')

    def check_amount(self, amount):
        self.amount = amount
        try:
            if type(self.amount) != int:
                raise TypeError(f'Введенный параметр не является целым числом\n'
                                f'Исправте, пожалуйста параметр ввода - количество, на целое число.')
        except TypeError as err:
            print(err)
            exit()

    def check_type_eq(self, type_eq):
        self.lst = ['Принтер', 'Сканер', 'Ксерокс']
        try:
            if self.type_eq not in self.lst:
                raise TypeError(f'У нас нет такого оборудования\n'
                                f'Выберите один из вариантов: {self.lst[0]}, {self.lst[1]}, {self.lst[2]}')
        except TypeError as err:
            print(err)
            exit()

    def get_at_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        if self.type_eq == 'Принтер':
            Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] + self.amount
            self.total_p = Office_eq.stock['Принтер']
            print(f'Поступило на ЦЕНТРАЛЬНЫЙ СКЛАД принтеров: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах принтеров всего: {self.total_p}')
        elif self.type_eq == 'Сканер':
            Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] + self.amount
            self.total_p = Office_eq.stock['Сканер']
            print(f'Поступило сканеров на ЦЕНТРАЛЬНЫЙ СКЛАД: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах сканеров всего: {self.total_p}')
        elif self.type_eq == 'Ксерокс':
            Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] + self.amount
            self.total_p = Office_eq.stock['Ксерокс']
            print(f'Поступило ксероксов на ЦЕНТРАЛЬНЫЙ СКЛАД: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах ксероксов всего: {self.total_p}')



    def transfer_from_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        if self.type_eq == 'Принтер':
            Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] - self.amount
            self.total_p = Office_eq.stock['Принтер']
            print(f'Списано с ЦЕНТРАЛЬНОГО СКЛАДА принтеров: {self.amount}')
            print(f'С учетом списания с ЦЕНТРАЛЬНЫОГО СКЛАДА, на складах принтеров всего: {self.total_p}')
        elif self.type_eq == 'Сканер':
            Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] - self.amount
            self.total_p = Office_eq.stock['Сканер']
            print(f'Списано с ЦЕНТРАЛЬНОГО СКЛАДА сканеров: {self.amount}')
            print(f'С учетом списания с ЦЕНТРАЛЬНЫОГО СКЛАДА, на складах сканеров всего: {self.total_p}')
        elif self.type_eq == 'Ксерокс':
            Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] - self.amount
            self.total_p = Office_eq.stock['Ксерокс']
            print(f'Списано с ЦЕНТРАЛЬНОГО СКЛАДА ксероксов: {self.amount}')
            print(f'С учетом списания с ЦЕНТРАЛЬНЫОГО СКЛАДА, на складах ксероксов всего: {self.total_p}')

    @staticmethod
    def info_stock():
        print(f'По запрошенной вами информации:')
        for k, v in Office_eq.stock.items():
            print(f'{k} {v} шт.')


# Через классы наследники как и в перыдущем примере можно принимать или списывать технику
# Сделеал две функции в базовом классе для проверки значений:
# тип оборудования check_type_eq и количество check_amount
# В классах наследниках сделал обращение к функциям проверки из базового класса
# Все отлично работает

class Printer(Office_eq):
    def __init__(self):
        self.name = 'Принтеры'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] + self.amount
        self.total_p = Office_eq.stock['Принтер']
        print(f'Поступило принтеров: {self.amount}')
        print(f'С учетом поступления, на складах принтеров всего: {self.total_p}')

    def transfer_from_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] - self.amount
        self.total_p = Office_eq.stock['Принтер']
        print(f'Выдано принтеров со склада: {self.amount}')
        print(f'С учетом списания, на складах принтеров всего: {self.total_p}')


class Scaner(Office_eq):
    def __init__(self):
        self.name = 'Сканеры'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] + self.amount
        self.total_p = Office_eq.stock['Сканер']
        print(f'Поступило сканеров: {self.amount}')
        print(f'С учетом поступления, на складах сканеров всего: {self.total_p}')

    def transfer_from_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] - self.amount
        self.total_p = Office_eq.stock['Сканер']
        print(f'Выдано сканеров со склада: {self.amount}')
        print(f'С учетом списания, на складах сканеров всего: {self.total_p}')


class Xerox(Office_eq):
    def __init__(self):
        self.name = 'Ксероксы'
        self.stock = Office_eq.stock
        print(f'Это склад - {self.name}')

    def get_at_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] + self.amount
        self.total_p = Office_eq.stock['Ксерокс']
        print(f'Поступило ксероксов: {self.amount}')
        print(f'С учетом поступления, на складах ксероксов всего: {self.total_p}')

    def transfer_from_stock(self, type_eq, amount):
        self.type_eq = type_eq
        self.amount = amount
        Office_eq.check_amount(self, amount)
        Office_eq.check_type_eq(self, type_eq)
        Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] - self.amount
        self.total_p = Office_eq.stock['Ксерокс']
        print(f'Выдано ксероксов со склада: {self.amount}')
        print(f'С учетом списания, на складах ксероксов всего: {self.total_p}')


a = Office_eq()
a.get_at_stock('Принтер', 10)
a.info_stock()
a.get_at_stock('Принтер', 10)
a.transfer_from_stock('Принтер', 5)
#a.get_at_stock('Сканер', 'str') # програмам будет обзываться и выкидывать вас, можно убрать коментарий и проверить
b = Printer()
b.info_stock()
#b.get_at_stock('Прин', 7) # програмам будет обзываться и выкидывать вас, можно убрать коментарий и проверить
#b.transfer_from_stock('Gh', 7) # програмам будет обзываться и выкидывать вас, можно убрать коментарий и проверить
# в классах наследниках все рабоатет.
c = Xerox()
c.transfer_from_stock('Ксерокс', 'strxxx')

# в классах наследниках все рабоатет.









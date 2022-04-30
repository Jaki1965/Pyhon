# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).

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

# Добавил возможность через центральный склад принимать технику и списывать.
# Таким образом, реализована главная идея задачи - сквозной складской учет.
# Теперь принять и списать технику можно, как из центрального склада, так и из любого подразделения
#

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


    def get_at_stock(self, type, amount):
        self.type = type
        self.amount = amount
        if self.type == 'Принтер':
            Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] + self.amount
            self.total_p = Office_eq.stock['Принтер']
            print(f'Поступило на ЦЕНТРАЛЬНЫЙ СКЛАД принтеров: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах принтеров всего: {self.total_p}')
        elif self.type == 'Сканер':
            Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] + self.amount
            self.total_p = Office_eq.stock['Сканер']
            print(f'Поступило сканеров на ЦЕНТРАЛЬНЫЙ СКЛАД: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах сканеров всего: {self.total_p}')
        elif self.type == 'Ксерокс':
            Office_eq.stock['Ксерокс'] = Office_eq.stock['Ксерокс'] + self.amount
            self.total_p = Office_eq.stock['Ксерокс']
            print(f'Поступило ксероксов на ЦЕНТРАЛЬНЫЙ СКЛАД: {self.amount}')
            print(f'С учетом поступления на ЦЕНТРАЛЬНЫЙ СКЛАД, на складах ксероксов всего: {self.total_p}')



    def transfer_from_stock(self, type, amount):
        self.type = type
        self.amount = amount
        if self.type == 'Принтер':
            Office_eq.stock['Принтер'] = Office_eq.stock['Принтер'] - self.amount
            self.total_p = Office_eq.stock['Принтер']
            print(f'Списано с ЦЕНТРАЛЬНОГО СКЛАДА принтеров: {self.amount}')
            print(f'С учетом списания с ЦЕНТРАЛЬНЫОГО СКЛАДА, на складах принтеров всего: {self.total_p}')
        elif self.type == 'Сканер':
            Office_eq.stock['Сканер'] = Office_eq.stock['Сканер'] - self.amount
            self.total_p = Office_eq.stock['Сканер']
            print(f'Списано с ЦЕНТРАЛЬНОГО СКЛАДА сканеров: {self.amount}')
            print(f'С учетом списания с ЦЕНТРАЛЬНЫОГО СКЛАДА, на складах сканеров всего: {self.total_p}')
        elif self.type == 'Ксерокс':
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
a.info_stock()
a.get_at_stock('Принтер',12)
b = Printer()
b.info_stock() # Поступление на центральный склад, видят на локальном складе
a.transfer_from_stock('Сканер', 4)
c = Scaner()
c.info_stock() # Списание сканеров через центральный склад отразилось во всех экземплярах
d = Xerox()
d.get_at_stock('Ксерокс', 11)
a.info_stock() # Приход ксероксов через профильный склад отразился в данных о центральном складе

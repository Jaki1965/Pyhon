# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    titel = ''
    def __init__(self, titel):
        self.titel = titel
    print(f'Пожалуйста при указании обязательного атрибута "titel" используйте только один из трех\n'
          f'установленных программой объектов:\n'
          f'pen, pencil или handle.')
    def drow(self):
        print('Запуск отрисовки')
        if self.titel == 'pen':
            print('Вы выбрали ручку. Отлично - будем писать!')
        elif self.titel == 'pencil':
            print('Вы выбрали карандашь. Отлично - будем рисовать!')
        elif self.titel == 'handle':
            print('Вы выбрали маркер. Отлично - будем выделять!')
        else:
            print('Мы просили придерживаться стандарта на указание канц. принадлежности.\nПожалуйтса, начните заново')

class Pen(Stationery):
    def __init__(self, titel):
        Stationery.__init__(self, titel)
        self.color = 0
        if self.titel != 'pen':
            print('Неверно указан первый атрибут - только "pen". Попробуйте заново.')

    def drow(self):
        print('Ручкой не рисуют, а пишут.')


class Pencil(Stationery):
    def __init__(self, titel):
        Stationery.__init__(self, titel)
        self.color = 0
        if self.titel != 'pencil':
            print('Неверно указан первый атрибут - только "pencil". Попробуйте заново.')

    def drow(self):
        print('Карандашем не только русуют, но еще и чертят.')

class Handle(Stationery):
    def __init__(self, titel):
        Stationery.__init__(self, titel)
        self.color = 0
        if self.titel != 'handle':
            print('Неверно указан первый атрибут - только "handle". Попробуйте заново.')

    def drow(self):
        print('Маркером выделяют.')




my_script = Stationery('no')
my_script.drow()
my_script = Stationery('pen')
my_script.drow()
my_script = Stationery('nothing')
my_script.drow()

my_pen = Pen('pencil')
my_pen = Pen('pen')
my_pen.drow()
my_pencil = Pencil('pencil')
my_pencil.drow()
my_handle = Handle('handle')
my_handle.drow()



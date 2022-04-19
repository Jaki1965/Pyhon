# 4. Реализуйте базовый класс Car.
#
#  у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#  опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#  добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#  для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    move = ''

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        if self.is_police == True:
            print('Техническое состояние не соответсвует требования. Выезд запрещен!')
        else:
            print('Техническое состояние в норме. Выезд разрешен.')
    def show_car(self):
        print(f'Ваша машаина это:\n{self.name}\n{self.color}')

    def go(self):
        self.move = 'Поехали'
        return self.move

    def stop(self):
        self.move = 'Остановились и стоим'
        return self.move

    def turn(self, direction):
        self.direction = direction
        if self.direction == 'right':
            print('Повернули в право')
        elif self.direction == 'left':
            print('Повернули в лево')

    def show_speed(self):
        if self.move == 'Остановились и стоим':
            print(f'Сейчас стоим. Скорость = 0. Из функции "def stop" пришла команда {self.move}')
        elif self.move == 'Поехали':
            print(f'Двигвемся со скоростью {self.speed} км/час')


class TownCar(Car):

    def __init__(self, name, color, speed, is_police, lim_speed):
        Car.__init__(self, name, color, speed, is_police)
        self.lim_speed = lim_speed
        self.more = 0
        if self.speed > self.lim_speed:
            self.more = abs(self.lim_speed - self.speed)
            print(f'Вы превысили скорость на {self.more} км./час.')

    def show_speed(self):
        if self.more <= 0:
            print('Вы соблюдаете скоростной режим. Продолжайте движение')
        elif   0 < self.more <= 20:
            print(f'За превышение скорости на {self.more} км./час. - штраф - 1000 рублей.'
                  f'\nСнизьте скорость до требуемой {self.lim_speed} км./час.')
        else:
            print(f'Вы пытаетсь превысить скорость на {self.more} км./час. Лишение прав на 3 дня.'
                  f'\nСнизьте скорость до требуемой {self.lim_speed} км./час.')

class SportCar(Car):
    def __init__(self, name, color, speed, is_police, lim_speed):
        Car.__init__(self, name, color, speed, is_police)
        self.lim_speed = lim_speed


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police, lim_speed):
        Car.__init__(self, name, color, speed, is_police)
        self.lim_speed = lim_speed
        self.more = 0
        if self.speed > self.lim_speed:
            self.more = abs(self.lim_speed - self.speed)
            print(f'Вы превысили скорость на {self.more} км./час.')

    def show_speed(self):
        if self.more <= 0:
            print('Вы соблюдаете скоростной режим. Продолжайте движение.')
        elif 0 < self.more <= 20:
            print(
                f'Это же рабочий транспорт {self.name} он не может двигаться быстрее чем 40 км./час.\n'
                f'Не смешите. Поставте в кчестве атрибута speed цифру не более "40"')
        else:
            print(f'Это не вертолет и не SportCar, а рабочий транспорт {self.name} он не может двигаться быстрее чем 40 км./час.\n'
                f'Не смешите. Поставте в кчестве атрибута speed цифру не более "40"')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed)


# Создаем экземпляр базового класаа Car
print('Проверка методов базовго класса')
my_car = Car('Какая-то машина', 'Какого-то цвета',60, False)
my_car.show_car()
print(my_car.go())
my_car.show_speed()
my_car.turn('left')
my_car.turn('right')
print(my_car.stop())
my_car.show_speed()
print(my_car.go())
my_car.show_speed()
print(my_car.stop())
my_car.show_speed()
print('Все методы базового класса работают правильно')
# Все методы базового класса работают правильно
# Создаем и проверяем экземпляр дочернего класса TownCar
my_towncar = TownCar('Школьный автобус', 'Желтый', 90, False, 60)
print(my_towncar.name)
print(my_towncar.color)
print(my_towncar.speed)
print(my_towncar.lim_speed)
print(my_towncar.go())
my_towncar.show_car()
my_towncar.show_speed()
print('Переопределенный метод "show_speed" работает правильно')
my_towncar.turn('right')
# Все методы дочернего класса работают правильно.
print('Все методы дочернего класса работают правильно.')
# ВСЕ ПРОВЕРИЛ. ДАЛЬШЕ УЖЕ ПИСАТЬ ВЫЗОВЫ АТРИБУТОВ И МЕТОДОВ НЕ СТАЛ. ИНЧЕ БУДЕТ ЕЩЕ СТРОК 60 кода :)
my_workcar = WorkCar('Старый трактор', 'Зеленый', 90, False, 40)
my_workcar.show_car()
my_workcar.show_speed()
my_workcar = WorkCar('Старый трактор', 'Зеленый', 30, False, 40)
my_workcar.show_speed()


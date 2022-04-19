# 3. Реализовать базовый класс Worker (работник).
#
#  определить атрибуты: name, surname, position (должность), income (доход);
#  последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
#  например, {"wage": wage, "bonus": bonus};
#  создать класс Position (должность) на базе класса Worker;
#  в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#  проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#  проверить значения атрибутов,
#  вызвать методы экземпляров.

class Worker:
    name = 'name'
    surename = 'surename'
    position = 'position'
    _income = {'wage': 90000, 'bonus': 30000}

    def get_data_worker(self):
        self.name = input('Введите имя сотрудника: ')
        self.surename = input('Введите фамилию сотрудника: ')
        self.position = input('Введите должность сотрудника: ')
        return self.name, self.surename, self.position, self._income

class Position(Worker):

    def get_full_name(self):
        print(f'Данные сотрудника: \nФамилия - {self.surename}\nИмя - {self.name}\nДолжность - {self.position}')

    def get_total_income(self):
        self.salary = self._income['wage'] + self._income['bonus']
        print(f'Доход сотрудника {self.name} {self.surename}\nДолжность: {self.position}\nСоставляет: {self.salary}')

print('Проверка атрибутов в базовом классе')
print(f'Атрибут - name:',Worker.name)
print(f'Атрибут - surename:',Worker.surename)
print(f'Атрибут - position:', Worker.position)
print(f'Защищенный трибут - _income:', Worker._income)
my_script = Position()
my_script.get_data_worker()

print('Проверка атрибутов в дочернем классе')
print(f'Атрибут - name:',Position.name)
print(f'Атрибут - surename:',Position.surename)
print(f'Атрибут - position:', Position.position)
print(f'Защищенный трибут - _income:', Position._income)

print('Проверка атрибутов в экземпляре класса')
print(f'Атрибут - name:',my_script.name)
print(f'Атрибут - surename:',my_script.surename)
print(f'Атрибут - position:', my_script.position)
print(f'Защищенный трибут - _income:', my_script._income)
my_script.get_full_name()
my_script.get_total_income()
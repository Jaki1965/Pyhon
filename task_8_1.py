# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

data_1 = '10.11.1965'
data_2 = '05_07_1999'
data_3 = '32/07/2022'
data_4 = '05_14_2011' #

class Data:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

        self.mm_dict = {1: 'январь',
                        2: 'февраль',
                        3: 'март',
                        4: 'апрель',
                        5: 'май',
                        6: 'июнь',
                        7: 'июль',
                        8: 'август',
                        9: 'сентябрь',
                        10: 'октябрь',
                        11: 'ноябрь',
                        12: 'декабрь'}
        print(f'Принятая на вход дата:\nЧисло: {self.dd}\nМесяц: {self.mm_dict[self.mm]}\nГод: {self.yy}')


    @classmethod
    def date_processing(cls, user_data):
        dd = int(user_data[:2])
        mm = int(user_data[3:5])
        yy = int(user_data[6:10])
        return cls(dd, mm, yy)

    def info_data(self,check_data):
        dd = int(user_data[:2])
        mm = int(user_data[3:5])
        yy = int(user_data[6:10])
        return dd, mm, yy

    @staticmethod
    def data_check(self):
        dd = int(self[:2])
        mm = int(self[3:5])
        yy = int(self[6:10])
        lst = [2, 4, 6, 9, 11]
        if mm > 12:
            print('НЕТ ТАКОГО МЕСЯЦА в КАЛЕНДАРЕ - ОБЯЗАТЕЛЬНО БУДЕТ СИСТЕМНАЯ ОШИБКА см. ниже!')
        mm_dict = {1: 'январь',
                        2: 'февраль',
                        3: 'март',
                        4: 'апрель',
                        5: 'май',
                        6: 'июнь',
                        7: 'июль',
                        8: 'август',
                        9: 'сентябрь',
                        10: 'октябрь',
                        11: 'ноябрь',
                        12: 'декабрь'}
        print(f'Проверяемый аргумент {self}\n'
              f'Это следующая дата:\n'
              f'Число: {dd}. Месяц: {mm_dict[mm]}. Год: {yy}')


        if mm == 2 and dd > 28:
            print(f'Ошибка месяц - дата:\n'
                  f'В месяце {mm_dict[mm]} не может быть больше 28 дней\n'
                  f'Исправте, пожалуйста, дату')

        elif mm in lst and dd > 30:
            print(f'Ошибка месяц - дата:\n'
                  f'В месяце {mm_dict[mm]} не может быть больше 30 дней\n'
                  f'Исправте, пожалуйста, дату')
        if  dd > 31:
            print(f'Ошибка дата:\n'
                  f'В месяце не может быть больше 31 днея\n'
                  f'Исправте, пожалуйста, дату')




my_data_1 = Data.date_processing(data_1)
my_data_2 = Data.date_processing(data_2)
my_data_my = Data.date_processing('30_11_1920')
my_data_3 = Data.date_processing(data_3)
Data.data_check(data_3)
Data.data_check(data_4)



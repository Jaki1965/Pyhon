# 7 (Дополнительно). Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
a = int(input('Результат первого дня спортсемена а = '))
b = int(input('Результат котрого нужно достич b = '))
# print(f'a = {a}, b = {b}') # не был уверен, что это значения a и b нужно выводить
i = 0
while a < b:
    a = a + a/10
    i = i + 1
print(f'Спортсмен достигнет результата на {i+1} день')


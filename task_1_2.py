# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input('Введите, пожалуйста, время в секудах:   '))
sec = user_time % 60
minute = (user_time // 60) % 60
hour = user_time // 3600
if sec < 10:
    sec = f'0{sec}'
if minute < 10:
    minute = f'0{minute}'
if hour < 10:
    hour = f'0{hour}'

print('Указанное вами время', f'{hour}:{minute}:{sec}')

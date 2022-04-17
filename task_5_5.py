# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def user_words():
    user_list = []
    while True:
        user_text = input('Введите, пожалуйста, числа. Чтобы закончить ввод, ведите пустую строку : ')
        user_list.append(user_text)
        for word in user_list:
            if word == '':
                user_list.remove(user_list[-1])
                print('Выход из ввода данных')
                return user_list

user_list = (user_words())

with open('task_5_5.txt', 'w', encoding='utf-8') as file_in:
    number_write = ' '.join(user_list)
    print(f'Вы ввели следующий набор чисел: {number_write}')
    file_in.write(number_write)
with open('task_5_5.txt', 'r', encoding='utf-8') as file_out:
    lst_num = file_out.read().split()
    sum = 0
    for i in lst_num:
        i = int(i)
        sum += i
    print(f'Сумма введенных вами чисел = {sum}')
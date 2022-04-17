# 1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

def user_words():
    user_list = []
    while True:
        user_text = input('Введите, пожалуйста, слово : ')
        user_list.append(user_text)
        for word in user_list:
            if word == '':
                user_list.remove(user_list[-1])
                print('Внимание указав пустую строку вы реализовали - "Выход из ввода данных"')
                return user_list

user_list = (user_words())
with open('task_5_1.txt', 'w', encoding='utf-8') as file_in:
    for item in user_list:
        file_in.write(item + '\n')








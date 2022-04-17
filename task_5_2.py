# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('task_5_2.txt', 'r', encoding='utf-8') as my_text:
    my_list = my_text.read().split()
    number_st = len(my_list)
    print(my_list)
    print(f'Количество слов в файле:  {number_st}')
    print('Количество букв в словах: ')
    for word in my_list:
        print(word, len(word))
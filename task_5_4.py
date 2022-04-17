# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


translater = {
    'One':'Один',
    'Two':'Два',
    'Three':'Три',
    'Four':'Четыре',
    'Five':'Пять',
    'Six':'Шесть',
    'Seven':'Пять',
    'Eight':'Восемь',
    'Nine':'Девять',
    'Ten':'Десять',
}

with open('task_5_4_read.txt', 'r', encoding='utf-8') as file_from:
    read_list = file_from.read().split()
    for key in translater:
        if key in read_list:
            i = read_list.index(key)
            read_list.insert(i, translater[key])
            read_list.pop(i+1)
    for el in read_list:
        if el == '-':
            read_list.remove(el)
    my_dict = {read_list[i]: read_list[i + 1] for i in range(0, len(read_list), 2)}

with open('task_5_4_write.txt', 'w', encoding='utf-8') as file_in:
    for key in my_dict:
        file_in.write(f'{key} - {my_dict[key]} \n')


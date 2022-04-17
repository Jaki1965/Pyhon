# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open('task_5_3.txt', 'r', encoding='utf-8') as my_text:
    my_list = my_text.read().split()
    i = 0
    for my_list[i] in my_list:
        if i % 2 != 0:
            my_list[i] = float(my_list[i])
        i +=1
    my_dict = {my_list[i]: my_list[i+1] for i in range(0, len(my_list), 2)}
    print('Cотрудники с зарабоной платой меньше 20 000')
    for key in my_dict:
        if my_dict[key] < 20000.00:
           print(key, my_dict[key])
    list_salary = [my_dict[key] for key in my_dict]
    middle_salary = round((sum(list_salary))/len(list_salary), 2)
    print(f'Средняя заработная плата сотрудника: {middle_salary}')


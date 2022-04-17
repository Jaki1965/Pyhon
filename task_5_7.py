# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open('task_5_7_read.txt', 'r', encoding='utf-8') as file_out:
    lst_comp = file_out.readlines()
    lst_comp = list(map(lambda s: s.strip(), lst_comp))  # убирал в конце каждого элемета \n
    lst_1 = []
    lst_2 = []
    for el in lst_comp:
        el = el.split()
        del el[1]
        count_my = [int(x) for x in el[1:]]
        profit = count_my[0] - count_my[1]
        del el[1:]
        el.append(profit)
        for n in el:
            lst_2.append(n)
    dict_end = {lst_2[i]: lst_2[i + 1] for i in range(0, len(lst_2), 2)}
    lst_3 = []
    for k in dict_end:
        if dict_end[k] > 0:
            lst_3.append(dict_end[k])
        average_profit = round((sum(lst_3)/len(lst_3)), 2)
    dict_av_prov = {'average_profit': average_profit}
    lst_end = []
    lst_end.append(dict_end)
    lst_end.append(dict_av_prov)
    print(lst_end)
with open('task_5_7_write.json', 'w', encoding='utf 8') as file_in:
    json.dump(lst_end, file_in)
# Проверка сделана как чтение из файла
with open('task_5_7_write.json', 'r', encoding='utf 8') as file_out_json:
    result = json.load(file_out_json)
    print(f'Прверка чтения из файла json\n{result}')

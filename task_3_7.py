# 7. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(word):
    word = str(word).lower().title() # на всякий случай, сначала lower. вдруг неяаянно набрали, что-то большими буквами
    print(word)

words = input('Введите несколько слов на латинском. Все маленькими буквами, через пробел: ')

int_func(words)






# C3.3. Работа с импортом
# Импорт происходит с помощью зарезервированного слова import название модуля.
import os
import sys
import time


print(os.getcwd())  # получить текущую директорию
print(os.listdir())  # получить список файлов текущей директории

# Для того, чтобы получить документацию на тот или иной модуль, можно воспользоваться командой help.
# help(os)
# Не следует импортировать модули в одну строку, каждый отдельный модуль должен импортировать на отдельной строке:
# # правильно
# import os
# import sys
#
# # неправильно
# import os, sys

# Но если вы хотите импортировать, например, несколько функций из одного модуля, можно перечислить их через запятую:
# from subprocess import Popen, PIPE

# ***** Как правильно составить модуль? *****
# Для этого были сформированы следующие правила.
# 1. Вся основная логика модуля заключена в отдельные функции или классы.
#    На глобальном уровне могут быть объявлены только константы или необходимые для инициализации модуля операции.
# 2. Если вы планируете, что модуль могут запускать как самостоятельный скрипт –
#    используйте следующую инструкцию: if __name__ == '__main__':.
# 3. Хорошая структура модуля выглядит следующим образом:
#      Docstring (описание) модуля.
#      Область импорта:
#        импорты системных библиотек;
#        импорты стандартных пакетов (из PyPI);
#        импорты ваших модулей (локальных).
#      Область объявление глобальных констант.
#      Инициализация модуля.
#      Область определения функций и классов.
#      Функции.
#      if __name__ == '__main__' (метод main) по желанию
#      (это одни из немногих нюансов при работе с собственными модулями).

# ВАЖНО: Чтобы модули заработали правильно, их нужно хранить в той же папке,
# в которой вы запускаете главный скрипт, иначе Python не найдёт ваш модуль!

# А теперь давайте вернёмся к нашей задаче:
#
# function.py
#
# def hello():
#     print('Hello world')
#
# main.py
#
# from function import hello
#
# hello()  # вызвали импортированную функцию
#
# В данном случае у нас есть два файла function.py и main.py.
# В первом объявлена функция, а во втором мы уже непосредственно вызываем её выполнение.
print("***** Задание 3.3.5 *****")
print(time.time())
print(time.ctime())
print(time.strftime('%X', time.localtime()))
print(time.strftime('%M', time.localtime()))
print(time.strftime('%x', time.localtime()))
print(time.strftime('%m', time.localtime()))
print()

print("Убывающий таймер")
i = 10
while i != 0:
    print(i)
    time.sleep(1)
    i -= 1
print("Время вышло")

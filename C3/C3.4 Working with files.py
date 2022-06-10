# ***** Работа с файлами *****

# *** Путь к файлу ***
import os

print("Путь к файлу")
# Существует два типа пути:
#    абсолютный,
#    относительный.

# Абсолютный путь — это путь, который указывает на одно и то же место в файловой системе,
# вне зависимости от текущего рабочего каталога или других обстоятельств. Его ещё называют полным.

# Относительный путь — это путь по отношению к текущему рабочему каталогу пользователя.

# Чтобы поработать с путями есть модуль os. Функция os.chdir() позволяет нам изменить директорию,
# которую мы в данный момент используем.
# Если вам нужно знать, какой путь вы в данный момент используете, для этого нужно вызвать os.getcwd().

start_path = os.getcwd()
print(start_path)

os.chdir("..")
print(os.getcwd())

os.chdir(start_path)
print(os.getcwd())

# С помощью функции os.listdir() можно получить весь список файлов, находящихся в директории.
# Если не указать никаких аргументов, то будет взята текущая директория.

print(os.listdir())
if 'tmp.py' not in os.listdir():
    print("Файл не найден")

# Для того, чтобы склеивать пути с учётом особенностей ОС, следует использовать функцию os.path.join().
print(start_path)
print(os.path.join(start_path, 'test'))
print()

print('Задание 3.4.3')


# Сделайте функцию, которая принимает от пользователя путь и выводит всю информацию о содержимом этой папки.
# Для реализации используйте функцию встроенного модуля os.walk().
# Если путь не указан, то сравнение начинается с текущей директории.


def dict_info(path=None):
    cur_dict = os.getcwd()
    if not path:
        tree = os.walk(cur_dict)
    else:
        tree = os.walk(path)

    for i in tree:
        print(i)


dict_info()


def walk_desc(path=None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл ", os.path.join(root, f))
        for d in dirs:
            print("Папка ", os.path.join(root, d))
        print("===")


walk_desc()
print()

print("Работа с файлами")
# Python «из коробки» располагает достаточно широким набором инструментов для работы с файлами.
# Для того чтобы начать работать с файлом, надо его открыть с помощью команды специальной функции open.
# f = open('path/to/file', 'filemode', encoding='utf8')
# 1. path/to/file — путь к файлу может быть относительным или абсолютным.
#    Можно указывать в Unix-стиле (path/to/file) или в Windows-стиле (path\to\file).
#
# 2. filemode — режим, в котором файл нужно открывать.
#    Записывается в виде строки, состоит из следующих букв:
#         r — открыть на чтение (по умолчанию);
#         w — перезаписать и открыть на запись (если файла нет, то он создастся);
#         x — создать и открыть на запись (если уже есть — исключение);
#         a — открыть на дозапись (указатель будет поставлен в конец);
#         t — открыть в текстовом виде (по умолчанию);
#         b — открыть в бинарном виде.
# 3. encoding — указание, в какой кодировке файл записан (utf8, cp1251 и т. д.) По умолчанию стоит utf-8.
# Открытие файла на запись является блокирующей операцией,
# то есть она останавливает работу нашей программы до того, пока файл не откроется.
f = open('test.txt', 'w', encoding='utf8')
f.write("This is a test string\n")
f.write("This is a new string\n")
f.close()

f = open('test.txt', 'r', encoding='utf8')
# После того, как файл открыт для чтения, мы можем читать из него данные.
# f.read(n) — операция, читающая с текущего места n символов, если файл открыт в t режиме,
# или n байт, если файл открыт в b режиме, и возвращающая прочитанную информацию.
print(f.read(10))
# После прочтения указатель на содержимое остается на той позиции, где чтение закончилось.
# Если n не указать, будет прочитано «от печки», т. е. от текущего места указателя и до самого конца файла.
print(f.read())
f.close()

# *** Чтение и запись построчно ***
print("Чтение и запись построчно")
# Зачастую с файлами удобнее работать построчно, поэтому для этого есть отдельные методы:
#         writelines — записывает список строк в файл;
#         readline — считывает из файла одну строку и возвращает её;
#         readlines — считывает из файла все строки в список и возвращает их.
# Метод f.writelines(sequence) не будет сам за вас дописывать символ конца строки (‘\n’).
# Поэтому при необходимости его нужно прописать вручную.

f = open('test.txt', 'a', encoding='utf8')
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)
f.close()
# Попробуем теперь построчно считать файл с помощью readlines:
f = open('test.txt', 'r', encoding='utf8')
print(f.readlines())
f.close()
# Метод f.readline() возвращает строку (символы от текущей позиции до символа переноса строки):
f = open('test.txt', 'r', encoding='utf8')

print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string

f.close()

print("Файл как итератор")
# Итераторы представляют собой такой объект, который вычисляет какие-то действия на каждом шаге, а не все сразу.
# На примере файла это выглядит, примерно, так.
# Предположим, у вас есть огромный текстовый файл, который весит несколько гигабайт.
# Если попытаться разом считать его полностью с помощью f.readlines(), то он будет загружен в вашу программу,
# в то время как переменная, в которую будет записан файл, станет весить так же, как и объём считанного файла.

# Не стоит считывать файл полностью, в большинстве задач с обработкой текста весь файл разом читать не требуется.
# В таком случае с файлом работают построчно.
f = open("test.txt")
for line in f:
    print(line, end='')
f.close()

# Для явного указания места работы с файлом, а также чтобы не забывать закрывать файл после обработки,
# существует менеджер контекста with.

with open("test.txt", "rb") as f:
    a = f.read(10)
    b = f.read(23)
print(a, b)
# f.read(3)  # ошибка, так как файл уже закрыт
print()
print("Задание 3.4.4")
# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
file_input = open("input.txt", "w", encoding="utf8")
lines = ['string_1\n', 'string_2\n', 'string_3']
file_input.writelines(lines)
file_input.close()
f = open("input.txt")
temp = []
for line in f:
    temp.append(line)
f.close()
f = open("output.txt", "w", encoding="utf8")
for line in temp:
    f.writelines(line)
f.close()

# а можно и так
# with open('input.txt', 'r') as input_file:
#    with open('output.txt', 'w') as output_file:
#        for line in input_file:
#            output_file.write(line)
print()

print("Задание 3.4.5")
# Дан файл numbers.txt, компоненты которого являются действительными числами
# (файл создайте самостоятельно и заполните любыми числам, в одной строке одно число).
# Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.
temp1 = []
with open('numbers.txt', 'r') as numbers_file:
    with open('output.txt', 'w') as output_file:
        for number in numbers_file:
            temp1.append(int(number))
        print(temp1)
        summ = min(temp1) + max(temp1)
        output_file.write(str(summ))
print()
# filename = 'numbers.txt'
# output = 'output.txt'
#
# with open(filename) as f:
#    min_ = max_ = float(f.readline())  # считали первое число
#    for line in f:
#        num =  float(line)
#        if num > max_:
#            max_ = num
#        elif num < min_:
#            min_ = num
#
#    sum_ = min_ + max_
#
# with open(output, 'w') as f:
#    f.write(str(sum_))
#    f.write('\n')

print("Задание 3.4.6")
# В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
# Выведите на экран всех учащихся, чья оценка меньше 3 баллов.
# Cодержание файла:
# Иванов О. 4
# Петров И. 3
# Дмитриев Н. 2
# Смирнова О. 4
# Керченских В. 5
# Котов Д. 2
# Бирюкова Н. 1
# Данилов П. 3
# Аранских В. 5
# Лемонов Ю. 2
# Олегова К. 4
# file_name = "class.txt"
# with open(file_name) as f:
#     for string in f:
#         if int(string[-2]) < 3:
#             print(string)

# with open('input.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)
print()

print("Задание 3.4.7")
# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
file_name = "class.txt"
temp_list = []
with open(file_name) as f:
    print("normal")
    for string in f:
        print(string)
        temp_list.append(string)
revers_list = temp_list[::-1]
print("revers")
for i in revers_list:
    print(i)

# with open('input.txt', 'r') as input_file:
#    with open('output.txt', 'w') as output_file:
#        for line in reversed(input_file.readlines()):
#            output_file.write(line)

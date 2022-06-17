# Связный список

class Node:
    def __init__(self, cargo=None, next_=None, back=None):
        self.cargo = cargo
        self.next_ = next_
        self.back = back

    def __str__(self):
        return str(self.cargo)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
print(node1)
node1.next_ = node2
node2.next_ = node3
print(node1.next_)
print()

# Очередь
# есть класс deque в модуле collections
# from collections import
# а можно самому создать очередь и наполнить ее методами и атрибутами
# да и любую структуру данных можно реализовать через ООП

# *** Алгоритм ***
import timeit
print("Алгоритм Евклида")
# Поиск наибольшего общего делителя(НОДа)
# Алгоритм Евклида
# задаем верные входные данные (то есть числа)
a = 50
b = 130
# пока а и б не равны нулю
while a != 0 and b != 0:
    # если я больше б
    if a > b:
        # присваеваем а остаток от деления а на б
        a = a % b
    # иначе
    else:
        # записываем в б остаток от деления б на а
        b = b % a
# то есть, мы делим а на б или б на а, пока оба не равны нулю
# как только появляется ноль, мы нашли НОД
print(a + b)
print()

# Алгоритм бинарного поиска
# Поиск числа в упорядоченном (отсортированном) списке.
print("Алгоритм бинарного поиска")

arr = [10, 20, 30, 40, 50]


def binary_search(array, value):
    first = 0
    last = len(array) - 1
    index = -1
    if len(array) == 1:
        return array[0]
    while (first <= last) and (index == -1):
        middle = (first + last) // 2
        if array[middle] == value:
            index = middle
        else:
            if value < array[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return index


print(binary_search(arr, 20))
print(timeit.timeit("binary_search([10, 20, 30, 40, 50], 20)", setup="from __main__ import binary_search", number=1))
print()

print("Алгоритм бинарного поиска (рекурсивный)")


def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            return recursive_binary_search(arr[mid:], target) + mid
        else:
            return recursive_binary_search(arr[:mid], target)


print(recursive_binary_search(arr, 20))
print(timeit.timeit("recursive_binary_search([10, 20, 30, 40, 50], 20)", setup="from __main__ import recursive_binary_search", number=1))
print()

print("Алгоритм сортировки подсчетом")
arr = [3, 5, 7, 1, 3, 6, 2, 1, 10]


def simple_counting_sort(array):
    scope = max(array) + 1  # определяем длину нулевого списка
    count = [0] * scope  # создаем список с подсчетом элементов
    for i in array:  # каждый элемент входного списка
        count[i] += 1  # используем как индекс для элемента нулевого списка и инкриментируем его
    array[:] = []  # обнуляем входной список
    print(count)
    for number in range(scope):  # берем индекс от нуля до самого большого числа
        array += [number] * count[number]  # добавляем в список столько раз, сколько он встречался в исходном списке
        print(array)
    return array


print(simple_counting_sort(arr))

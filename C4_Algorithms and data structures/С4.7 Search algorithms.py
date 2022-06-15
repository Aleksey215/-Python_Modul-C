# ***** Алгоритмы поиска *****
# На текущий момент мы познакомились со всеми основными структурами данных и даже научились создавать собственные.
# Это победа!
#
# Однако эти структуры существуют для какой-то цели.
# Одна из самых распространенных — поиск элемента в структуре.
# В этой части модуля мы рассмотрим базовые алгоритмы поиска в различных структурах.

# *** Линейный поиск ***
# Алгоритм линейного поиска определяется на таких структурах данных
# как массивы, списки и надстройки над ними — очередь и стек.

# Такой алгоритм является «решением в лоб» и сводится к перебору одного элемента за другим
# и операции сравнения на каждом.
# Как правило, линейный поиск применяется к неотсортированным структурам.

# Пусть на вход программы поступает массив из произвольного количества целых чисел и еще одно целое число,
# которое будем проверять на вхождение в этот массив.
# Задача состоит в том, чтобы вернуть индекс первого вхождения элемента,
# если он входит в него, и False, если не входит.

print("Алгоритм линейного поиска")


def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
# В худшем случае этот алгоритм работает за O(n),
# потому что, если элемент не входит в массив, придется провести n сравнений.
# Все они не увенчаются успехом.

# Линейный алгоритм поиска может применяться для следующих целей:
#         Нахождение минимального/максимального элемента.
#         Поиск элемента с определенным значением.
#         Количество вхождений элемента в массив.
#         Количество элементов больше заданного.
print()

print("Задание 4.7.1")
# Напишите функцию count, которая возвращает количество вхождений элемента в массив
array = list(map(int, input("enter array: ").split()))
element = int(input("enter element: "))


def count(arr, elem):
    cnt = 0
    for i, a in enumerate(arr):
        if a == elem:
            cnt += 1
    return cnt


print(count(array, element))
print()

# *** Двоичный поиск ***
# Алгоритм двоичного поиска является более совершенным, чем линейный поиск,
# однако он накладывает на структуру сильное ограничение — она должна быть отсортирована.

# Допустим, что у нас стоит такая же задача — найти индекс определенного элемента в массиве.
# В связи с тем, что алгоритм может искать только в отсортированном массиве,
# используем генератор последовательных чисел range.
# Суть двоичного поиска сводится к тому, что на каждой итерации размер исследуемого массива уменьшается в 2 раза.

print("Алгоритм двоичного поиска")


def binary_search(arr, elem, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if arr[middle] == elem:
        return middle
    elif elem < arr[middle]:
        return binary_search(arr, elem, left, middle - 1)
    else:
        return binary_search(arr, elem, middle + 1, right)


element = int(input("Enter element: "))
array = [i for i in range(1, 100)]
print(binary_search(array, element, 0, 98))


# Математически доказывается, что сложность такого алгоритма O(log(n)),
# а как вы должны помнить из начала этого модуля — логарифмическая сложность намного лучше, чем линейная.
# Ура! Мы получили очень эффективный алгоритм поиска. Только вот сортировать нужно…

# *** Двоичное дерево поиска ***
# Не всякое двоичное дерево является двоичным деревом поиска.
# Оно должно обладать некоторыми свойствами:
#     1. Оба поддерева каждого узла являются двоичными деревьями поиска
#     2. Для узла с ключом X все узлы левого поддерева должны быть строго меньше X
#     3. Аналогично, для узла с ключом X все узлы правого поддерева должны быть строго больше X


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):  # печать с помощью обхода в ширину
        queue = [self]  # создаем очередь
        values = []  # значения в порядке обхода в ширину
        while queue:  # пока она не пустая
            last = queue.pop(0)  # извлекаем из начала
            if last is not None:  # если не None
                values.append("%d" % last.value)  # добавляем значение
                queue.append(last.left_child)  # добавляем левого потомка
                queue.append(last.right_child)  # добавляем правого потомка
        return ' '.join(values)

    # Какие методы должен реализовать этот класс?
    # 1. Поиск элемента
    # 2. Поиск минимума/максимума
    # 3. Поиск следующего элемента
    # 4. Вставка элемента
    # 5. Удаление элемента
    # 6. Построение дерева по массиву

    def search(self, x):  # 1. Поиск элемента
        if self.value == x:
            return self
        elif self.value > x:
            return self.left_child.search(x)
        elif self.value < x:
            return self.right_child.search(x)
        else:
            return False

    def minimum(self):  # 2. поиск минимума
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()

    def maximum(self):  # 2. поиск максимума (задание 1)
        if self.right_child is None:
            return self
        else:
            return self.right_child.maximum()

    def next_value(self, x):  # 3. поиск следующего элемента
        current = self
        successor = None
        while current is not None:
            if current.value > x:
                successor = current
                current = current.left_child
            else:
                current = current.right_child
        return successor

    def previous_value(self, x):  # поиск предыдущего значения (задание 2)
        current = self
        successor = None
        while current is not None:
            if current.value < x:
                successor = current
                current = current.right_child
            else:
                current = current.left_child
        return successor

    def insert(self, x):
        if x > self.value:  # идем в правое поддерево
            if self.right_child is not None:  # если оно существует,
                self.right_child.insert(x)  # делаем рекурсивный вызов
            else:  # иначе создаем правого потомка
                self.right_child = BinarySearchTree(x)
        else:  # иначе в левое поддерево и делаем аналогичные действия
            if self.left_child is not None:
                self.left_child.insert(x)
            else:
                self.left_child = BinarySearchTree(x)
        return self  # возвращаем корень

    def delete(self, x):
        """
        Алгоритм действительно непростой, поэтому разберем его еще раз по шагам:
            1. С помощью цикла while ищем узел node, подлежащий удалению, а также его предка parent
            2. Если найденный узел является листом, то удаляем его, присваивая значение
               None соответствующему левому (правому) поддереву предка.
            3. Если найденный узел имеет одного потомка, то устанавливаем связь между ним
               и предком удаляемого узла. Этот единственный потомок становится на место
               удаленного узла.
            4. Если найденный узел имеет сразу обоих потомков, то находим следующее
               значение за удаляемым и сохраняем его. Это значение становится на место удаленного.
               После чего, во избежание дублирования, нужно рекурсивно удалить новое значение.
               Элемент, стоящий на месте удаленного узла, является следующим, т.е.
               больше исходного, поэтому всегда находится в правом дереве.
               И именно для правого дерева мы запускаем эту же самую функцию
        """
        parent = self
        node = self
        if not self.search(x):
            return self
        while node.value != x:
            parent = node
            if parent.left_child is not None and x < parent.value:
                node = parent.left_child
            elif parent.right_child is not None and x > parent.value:
                node = parent.right_child
        # по завершении в node хранится искомый узел

        # первый случай - если лист
        if node.left_child is None and node.right_child is None:
            if parent.left_child is node:
                parent.left_child = None
            if parent.right_child is node:
                parent.right_child = None
            if parent.value == x:
                # если нет листов и parent==node до сих пор,
                # значит, нужно вернуть None для корректной работы рекурсии
                return None

        # второй случай - имеет одного потомка
        elif node.left_child is None or node.right_child is None:
            if node.left_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.left_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
            if node.right_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.right_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
        else:  # третий случай - имеет двух потомков
            next_ = node.next_value(x).value  # ищем следующее значение
            node.value = next_  # и меняем на него
            # # делаем рекурсивный вызов
            node.right_child = node.right_child.delete(next_)
        return self


BinSTree_1 = BinarySearchTree(25)
BinSTree_1.left_child = BinarySearchTree(10)
BinSTree_1.right_child = BinarySearchTree(37)
BinSTree_1.left_child.right_child = BinarySearchTree(15)
BinSTree_1.right_child.left_child = BinarySearchTree(30)
BinSTree_1.right_child.right_child = BinarySearchTree(65)

BinSTree_1.delete(37)
BinSTree_1.delete(25)

print(BinSTree_1)


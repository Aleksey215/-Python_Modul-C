# ***** Статические методы *****
# Статические методы — это методы, которые относятся сразу ко всем объектам класса,
# и могут вызываться вне конкретного объекта, обращаясь к классу напрямую.

# Например, нам надо вывести какую-то информацию или выполнить действие, которое не зависит от какого-либо объекта.
# Допустим, это действие для всех объектов абсолютно одинаково и не зависит от значения полей.
# В этом случае мы можем использовать статические методы.

# Пример:
print("Статический метод пример")


class StaticClass:

    @staticmethod  # помечаем метод который мы хотим сделать статичным декоратором @staticmethod
    def bar():
        print("bar")


print("вызов статического метода от класса")
StaticClass.bar()

# Почему вызывается метод без объекта, где self?
# Статические методы не принимают первым аргументом - self.
# Их основной принцип - их выполнение не зависит от состояния конкретного объекта.

# С одной стороны, мы можем быстро и удобно вызывать какие-то общие методы,
# но с другой — получить информацию о состоянии объекта не получится,
# даже если мы будем вызывать статический метод через объект, а не через прямое обращение к классу,
# а так делать тоже можно.

print("вызов статического метода от объекта")
f = StaticClass()
f.bar()
print()
# Вызов статического метода через объекты не возбраняется, но считается не очень хорошим тоном.

# В каких случаях стоит использовать статические методы?
# Статические методы надо использовать, когда мы должны выполнить какое-то действие,
# которое не зависит от состояния объекта.
# Например, прочитать какой-нибудь файл или вывести на экран какую-либо информацию.
# Иногда через статические методы удобно хранить константы.

# class StaticClass:
#
#     @staticmethod
#     def GET_BAR():  # вспоминаем, что константа пишется со всеми заглавными буквами (в простонародье - капсом)
#         return "bar"
#
#
# print(StaticClass.GET_BAR())

# Хотя тут можно было бы обойтись и полями.
# Да и по правде признаться, для хранения констант лучше всего, конечно же,
# использовать поля, чтобы не смущать своих коллег.
# Используйте статические методы в основном для работы с внешними ресурсами (API, файлы и т. д.).

print("Задание 2.2.4")
# Напишите класс SquareFactory с одним статическим методом, принимающим единственный аргумент — сторону квадрата.
# Данный метод должен возвращать объект класса Square с переданной стороной.


class Square:
    def __init__(self, side):
        self.side = side


class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sq1 = SquareFactory.create_square(1)
print(sq1.side)
print("Задание 1.10.1")
# Создайте класс одной из геометрических фигур (например, прямоугольника),
# где в конструкторе задаются атрибуты:
# начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).

# Создайте метод, который возвращает атрибуты прямоугольника как строку
# ( постарайтесь применить магический метод __str__).
# Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100
# метод должен вернуть строку Rectangle : 5, 10, 50, 100.


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle: {self.a}, {self.b}, {self.c}"

    def get_area_triangle(self):
        p = (self.a + self.b + self.c)/2
        area = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return f"Area of a triangle: {round(area, 2)}"


triangle_1 = Triangle(12, 13, 14)
print(triangle_1)
print()

print("Задание 1.10.2")
# В классе, написанном в предыдущем задании, создайте метод, который будет рассчитывать площадь фигуры.
# Выведите значение площади на экран.
print(triangle_1.get_area_triangle())
print()

print("Задание 1.10.3")
# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.surname}. \nCity: {self.city}. \nBalance: {self.balance}"

    def get_info(self):
        return f"{self.name, self.surname, self.city}"


ivan = Client('Ivan', 'Ivanov', 'Vladivostok', 150)
petr = Client('Petr', 'Petrov', 'Vladivostok', 100)
elena = Client('Elena', 'Rochina', 'Vladivostok', 200)
print(ivan)
print()

print("Задание 1.10.4")
# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.

# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

guests_list = [ivan, petr, elena]
for guest in guests_list:
    print(guest.get_info())
print()
# ***** Классы *****
# Класс — это заготовка для создания объектов.
# После того как вы описали свой класс, вы сможете создавать любое количество объектов класса,
# которые будут устроены единообразно.
# Такие объекты называются экземплярами.

class User:
    pass


peter = User()  # создаем экземпляр peter класса user
peter.name = "Peter Robertson"  # добавляем свойство(атрибут) name

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)

# Мы можем задавать атрибуты, которые будут доступны из любого объекта, причём без дополнительных действий.
# Для этого их надо объявлять прямо внутри класса:


class Human:
    number_of_fingers = 5
    number_of_eyes = 2


lancelot = Human()
print(lancelot.number_of_fingers)
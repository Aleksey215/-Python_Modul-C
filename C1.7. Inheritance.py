# ***** Наследование *****
# объекты, созданные при помощи класса, наследуют атрибуты класса,
# которые объявлены прямо в теле, а не добавлены в конкретный независимый экземпляр.

# Идея наследования класса состоит в том, что новый класс создается не на «пустом месте», а на основе уже существующего.
# В результате наследования все поля и функции из базового класса неявным образом «наследуются» в производном классе.

# При описании производного класса используем шаблон:
# class ПроизводныйКласс (БазовыйКласс):
#     # Тело класса

# Таким образом, классы умеют наследовать друг у друга, причем не только атрибуты, но и методы.

import datetime  # подключение библиотеки


print("Наследование. Пример - 1")
# создаем родительский класс
class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


# создаем производный класс используя наследование
class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


# создаем экземпляр производного класса
eggs = Food(name='eggs', category='food', quantity_in_stock=5)
# выводим атрибут родительского класса для экземпляра дочернего класса
print(eggs.max_quantity)
print(eggs.is_available())
print()

# ***  Конструкция if __name__ == "__main__":. ***
# Данная конструкция позволяет запускать код внутри блока if в зависимости от запущенного файла.
# В переменной __name__ мы храним путь, откуда запущен файл.
# Если мы запустили файл из консоли: python *имя файла*, то в переменной __name__ будет строка "__main__".
# Если мы импортировали файл из другого файла, в переменной __name__ будет просто название самого файла.

# создадим два файла: myclass.py и main.py.
# В файле myclass.py опишем небольшой класс, а также используем предложенную конструкцию.

# Важно, если мы назовем атрибут или метод так же, как он называется в родительском классе, он будет переопределен.
# Рассмотрим на примере:
print("Наследование. Пример - 2")


# Создание родительского класса с методами
class Event:
    def __init__(self, timestamp=0, event_type='', session_id=''):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


# Создание дочернего класса
class ItemViewEvent(Event):
    # Переопределение атрибута
    type = "ItemViewEvent"

    # Переопределение родительского метода инициализации
    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    # Переопределение родительского метода вывода описания
    def show_description(self):
        print("This event means someone has browsed an item")


if __name__ == "__main__":
    # Создание экземпляра дочернего класса
    test_view_event = ItemViewEvent(timestamp=1549461608000,
                                    session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    # вызов переопределенного метода описания
    test_view_event.show_description()
    # вывод переопределенного атрибута
    print(test_view_event.type)
print()
# Итог:
#     1. Переопределили конструктор класса.
#        Теперь мы используем не родительский, а свой, и передаём в него другой набор аргументов.
#        Так у нас получился кастомизированный набор атрибутов: у родительского класса нет атрибута number_of_views.
#     2. Переопределили значение атрибута type с помощью атрибута класса.
#        Теперь при вызове type от экземпляра нашего дочернего класса мы получим значение атрибута type
#        нашего класса ItemViewEvent.
#     3. Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.

# *** Проверка типа объекта ***
print("Проверка типа данных")
# В некотором смысле, определяя новый класс, вы создаете новый тип данных.
# Базовые типы данных, предоставляемые Python, так же являются классами — иначе откуда у них методы.
# убедимся в этом с помощью функции isintance.

# Все просто: вы передаете в нее объект и тип (класс), а функция возвращает логическое значение результата проверки.
# То есть говорит вам, является ли объект объектом нужного вам типа (класса).
print("Использование функции - isinstance()")
print(isinstance("foo", str))
print(isinstance(test_view_event, ItemViewEvent))

# Но у этого метода есть загвоздка:
print(isinstance(test_view_event, Event))
# Мы видим, что для родительского класса функция также вернёт True.
# На самом деле, по этой и ряду других причин не всегда хорошо завязывать логику на проверку типа через isinstance.

# Мы уже говорили о том, что в некотором смысле в Python всё — объект.
# Это означает, что «под капотом» все классы и типы в Python наследуются от object.

print(isinstance("foo", object))
print()

# *** Более сложное наследование ***
print("Сложное наследование")
# Классы в Python поддерживают множественное наследование:
# это значит, что при объявлении класса вы можете через запятую в качестве нескольких аргументов
# перечислить несколько классов.
# При этом порядок перечисления важен, так как от этого будет зависеть,
# в каком порядке Python будет искать одноименные атрибуты и методы, определяя, какой будет кем переопределен.

# Рассмотрим множественное наследование на примере отдельных комнат и квартиры.


class Room1:
    def get_room(self):
        print('room_1')


class Room2:
    def get_room(self):
        print('room_2')

    def get_room_2(self):
        print('room 2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room1, Room2):
    pass


f = Flat()
f.get_kitchen()
f.get_room()
f.get_room_2()

print()
# Класс Flat наследует классы отдельных комнат в следующем порядке: Kitchen, Room1, Room2.
# Это значит, что поиск методов при их вызове (f.get_kitchen() и др.)
# сначала будет осуществляться в классе Kitchen, затем,
# если s метод не найден, в классе Room1, и только затем Room2.
# Это хорошо видно на примере вызова метода get_room().

# В более сложных случаях наследования, например, когда несколько родительских классов сами имеют родительский класс,
# порядок использования методов определяется специальными алгоритмами поиска
# Рассмотрим небольшой пример:
class Room:
    def get_room(self):
        print('room')

class Room1(Room):
    def get_room(self):
        print('room1')

class Room2(Room):
    def get_room(self):
        print('room2')

class Flat(Room1, Room2):
    pass

print(Flat.mro())  # метод класса, который показывает порядок наследования
f = Flat()
f.get_room()
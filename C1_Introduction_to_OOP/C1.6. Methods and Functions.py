# ***** Методы и функции *****
# Метод — это всего лишь функция, реализованная внутри класса, и первым аргументом принимающая self:
class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


# Здесь и __init__, и is_available — это методы.
# По умолчанию первым аргументом во все методы класса подается self
# При этом, чтобы вызвать исполнение метода, передавать self уже не нужно:
eggs = Product('eggs', 'food', 5)
print(eggs.is_available())

# Для вызова метода, как и для вызова функции, используются круглые скобки.
# Разница между методом и функцией только в том, что метод вызывается от конкретного объекта
# и реализован внутри класса, а функция работает сама по себе.

# Пусть мы хотим обрабатывать некоторые события из уже известных нам логов событий.
# Создадим класс с конструктором:


class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id


# Допустим, мы уже распарсили наши логи и получили список словарей вроде такого:
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]
# Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора, как мы уже делали.
# А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:
for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.type)

# Здесь мы использовали метод словаря .get(), который возвращает значение ключа и не вызывает ошибку,
# если такого ключа в словаре нет.


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")


# После этого мы скрыли реализацию логики от пользователя — то есть нам уже неважно,
# как это работает, мы знаем, что можем подать на вход словарь с нужными ключами, и всё будет работать само.
for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

# Методы облегчают работу с объектами класса, предоставляя готовую и удобную логику.

# Пример правильного кода с соблюдением инкапсуляции, то есть когда воздействовать на атрибуты класса
# можно только через его методы:


# Пример неправильного кода
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age


h = Human()
h.age = 15  # (Так делать лучше не стоит, если вы хотите когда-нибудь найти работу)
print(h.age)  # и так тоже

# при таком подходе, оставляя поля класса открытыми, вы оставляете их абсолютно беззащитными
# перед внешним воздействием. За этим и нужна инкапсуляция.
# Она говорит нам, что мы должны беречь наши классы и обрабатывать каждое обращение к его полям.
# Сейчас вы увидите, что нужно исправить, пока ещё не поздно.


# Более правильный пример
class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age, int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h1 = Human()
h1.set_age(35)
print(h1.get_age())
# Здесь мы уже контролируем обращение к полям класса. Мы добавили специальные методы: геттеры и сеттеры.
# Геттеры — пишется так: get_<имя поля>.
# Геттер просто возвращает значение поля и не принимает никаких аргументов.

# Сеттер — пишется так: set_<имя поля>.
# Сеттер принимает один аргумент — значение, которое он должен установить в поле.

# классы — это связка между определенной структурой данных, хранящихся в атрибутах,
# и логикой, которая непосредственно относится к ним.
# Плюс ко всему мы познакомились с нашей первой концепцией ООП — инкапсуляцией,
# которая говорит нам, что поля класса должны обрабатываться только через специальные методы — геттеры и сеттеры.
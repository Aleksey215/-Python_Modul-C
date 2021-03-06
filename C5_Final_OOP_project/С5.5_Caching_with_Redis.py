# ***** Кэширование с помощью Redis *****

# Кэширование — это временное сохранение данных для дальнейшего доступа к ним.
# Например, Redis отлично может хранить недавние действия пользователя на вашем сайте,
# какие-то сообщения из онлайн-чата и так далее.
# Первое, что вам надо будет сделать — это поставить себе Redis.

# Это можно сделать несколькими способами.
# Наиболее удобный, на наш взгляд, — воспользоваться облачным сервисом от Redis Labs и хранить ваши данные в облаке.

# Для работы с Redis в Python нужно установить специальную библиотеку:
# pip3 install redis.

# Теперь давайте попробуем всё же написать код подключения к нашей базе данных:
import redis
import json

red = redis.Redis(
    host='localhost',  # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost.
    port=6379  # порт подключения. На локальной машине это должно быть 6379.
)

# Теперь давайте попробуем записать данные в кэш.
# Для этого используется метод: .set(<название переменной для хеширования>, <значение переменной в виде строки>).
# red.set('var1', 'value1')  # записываем в кэш строку "value1"
print(red.get('var1'))  # считываем из кэша данные

# Но на этом ещё не всё.
# Вся загвоздка здесь в том, что данные нами записанные, не зависят от текущей сессии.
# Они не стираются после того, как скрипт закончит работу.

# Давайте теперь удалим некоторые строчки и убедимся, что данные,
#

# Как видим, строки хранятся отлично.
# И получать их можно оттуда так же легко.
# Давайте теперь попробуем записать в кэш что-нибудь посложнее, например, словарь.

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные,
# полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание

# Наконец, давайте научимся удалять данные из кэша по ключу. Это делается совсем просто.
red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))
print()

# Вот и всё.
# В этом юните мы научились устанавливать Redis, записывать и хранить в нём данные, а также считывать и удалять их.

# Redis — это довольно мощный инструмент.
# Его, конечно же, не желательно использовать как основную базу данных
# для каких-либо более или менее серьёзных проектов.
# Дело в том, что сам по себе он крайне не структурирован,
# и чем пытаться закопать в кэш какую-либо определённую структуру всех хранимых объектов,
# легче воспользоваться готовыми СУБД, например, PostgreSQL

# Однако в Redis отлично хранятся данные,
# которые по своей структуре не похожи ни на одну таблицу или же которые
# надо будет просто периодически считывать и забывать про них.
# Инструмент очень полезный и необычный. Лучше во всяком случае, чем хранить данные в файле.

print("Задание 5.5.4")


# Напишите программу, которая будет записывать и кэшировать номера телефонов ваших друзей.
# Программа должна уметь воспринимать несколько команд:
#         записать номер;
#         показать номер друга в консоли при вводе имени;
#         удалить номер друга по имени.
# Кэширование надо производить с помощью Redis.
# Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).


def save_phone_numbers():
    contacts = redis.Redis(host='localhost', port=6379)
    print("""Commands: 1) "add" 2) "get" 3) "delete" 4) "get_all" 5) "exit_" """)
    names = []
    exit_ = False
    while not exit_:
        cmd = input("Enter command: ")
        if cmd == 'add':
            phone_num = input("Enter phone number: ")
            contact_name = input("Enter name: ")
            names.append(contact_name)
            contacts.set(contact_name, phone_num)
            print("Contact added")
            print()
            continue
        elif cmd == 'get':
            contact_name = input("Enter contact name: ")
            if contact_name in contacts:
                num = contacts.get(contact_name)
                print("Your contact: ", int(num))
            else:
                print("Contact not found")
                print()
            continue
        elif cmd == 'get_all':
            for name in names:
                print(contacts.get(name))
                print()
            continue
        elif cmd == 'delete':
            contact_name = input("Enter contact name: ")
            contacts.delete(contact_name)
            print("contact was deleted")
            print()
            continue
        elif cmd == 'exit_':
            print("program completed")
            exit_ = True
            continue


save_phone_numbers()

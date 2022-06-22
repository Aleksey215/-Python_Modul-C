# Парсинг сайтов на примере Python.org

# Парсеры — это специальные программы, которые позволяют собирать информацию с веб-сайтов,
# не заходя на них через браузер.

# Теперь давайте для начала установим саму библиотеку:
# pip3 install lxml.
import requests
import lxml.html
from lxml import etree

# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head>,
# который лежит в свою очередь внутри тега <html>
# (в этом невидимом теге <head> у нас хранится основная информация о страничке.
# Её название и инструкции по отображению в браузере.
#
# print(title)  # выводим полученный заголовок страницы


# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
# попытаемся спарсить наш файл с помощью html-парсера.
# Сам html - это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')
# помещаем в аргумент метода findall скопированный xpath.
# Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости.
    # У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать,
    # чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст, это и будет нашим названием


# Обратите внимание, что в скопированном из браузера xpath надо внести изменения.
# А конкретно: мы удалили начальный тег /HTML из поиска.
# В основном методы find и findall работают так же, как и функция xpath, но всё же есть отличия.
# Как вы догадались, findall возвращает список многих подходящих элементов,
# в то время как метод find возвращает только первый подходящий элемент.
# Также второй аргумент в функции .parse() обязательный.
# Без него мы парсить не сможем, потому как для восприятия парсером
# переданного в IDE HTML-текста, а не какого-либо ещё, нужно передать объект класса HTMLParser.


print("Задание 5.4.4")
# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
# <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
html = '''
<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>'''
tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')
tag2 = tree.xpath('/html/body/tag1/tag2/text()')
print(title)
print(tag2)
print()


# создание класса "Прямоугольник"
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

# Выполним импорт из основного файла класса, где описан прямоугольник (Rectangle),
# «возьмем» оттуда все свойства, такие как width (ширина) и height (высота) и создадим «псевдо» прямоугольник r1.
from rectangle_c1_9 import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
rect_3 = Rectangle(3, 4)

print(rect_1.get_area())
print(rect_2.get_area())
print(rect_3 == rect_1)
print(rect_3 == rect_2)
print()

square_1 = Square(5)
square_2 = Square(12)
print(square_1.get_area_square())
print(square_2.get_area_square())
print()

# Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию.
# Назовем фигуры (figures).
# Коллекция содержит список, в который и помещаем наш первый прямоугольник, квадрат и т. д.
figures = [rect_1, rect_2, square_1, square_2]
# Далее пройдемся по циклу for:
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle_1 = Circle(3)
print(circle_1.get_area_circle())
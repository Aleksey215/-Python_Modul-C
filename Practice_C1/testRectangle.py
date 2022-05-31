from rectangle import Rectangle  # импорт класса прямоугольник из другого файла

# создание экземпляра класса Прямоугольник
r1 = Rectangle(10, 5)

# обращение ко всем атрибутам и методам класса "Прямоугольник"
print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())
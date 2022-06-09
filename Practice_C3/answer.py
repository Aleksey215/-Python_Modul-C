from functions import circle_area, rectangle_area


r = int(input("Enter r: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if circle_area(r) > rectangle_area(a, b):
    print("Circle is bigger than square")
else:
    print("Square is bigger then circle")
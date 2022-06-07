import random


class FieldException(Exception):
    pass


class FieldOutException(FieldException):
    def __str__(self):
        return "Координаты вашего выстрела за пределами поля"


class RepeatFieldException(FieldException):
    def __str__(self):
        return "Данная точка занята, введите другие координаты"


class Dot:
    """
    Класс - "Точка". Принимает два параметра:
    координату - х и координату у.
    Имеет перегруженный метод __eq__, для сравнения
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot{self.x, self.y}"


d = Dot(1, 3)
print(d)


class Ship:
    def __init__(self, bow, ship_len, horizontally):
        self.bow = bow
        self.ship_len = ship_len
        self.horizontally = horizontally
        self.hit_point = ship_len

    @property
    def dots(self):
        ship_points = []
        if self.horizontally:
            ship_points = [Dot(self.bow.x, self.bow.y+i) for i in range(self.ship_len)]
        else:
            ship_points = [Dot(self.bow.x+i, self.bow.y) for i in range(self.ship_len)]

        return ship_points


ship1 = Ship(d, 3, True)
print(ship1.dots)


class Field:
    def __init__(self, hid=False):
        self.hid = hid
        self.field = [[' ' for i in range(7)] for j in range(7)]
        self.ship_list = []
        self.live_ship_list = []
        self.busy = []

    def show(self):
        if self.hid:
            print("------Поле компьютера------")
        else:
            print("-----Поле пользователя-----")
        for i in range(7):
            for j in range(7):
                if i == 0:
                    print(f"{j} ", end="  ")
                elif j == 0:
                    print(f"{i} ", end="|")
                else:
                    print(f" {self.field[i][j]} ", end="|")
            print()
        print("---------------------------")

    def add_ship(self, ship):
        self.ship_list.append(ship)
        for ship in self.ship_list:
            for dot in ship:
                self.busy.append(dot)
                if not self.hid:
                    self.field[dot.x][dot.y] = '■'
        
    def out(self, dot):
        if dot.x > 6 or dot.y > 6:
            return True
        else:
            return False

    def shot(self, dot):
        if (dot.x, dot.y) not in self.busy:
            if 1 <= dot.x <= 6 and 1 <= dot.y <= 6:
                self.field[dot.x][dot.y] = "*"
                self.busy.append(dot)
            else:
                raise FieldOutException
        else:
            raise RepeatFieldException

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        for dot in ship.dots:
            for dot_x, dot_y in near:
                cur = Dot(dot.x + dot_x, dot_y + dot_y)
                if not self.out(cur):
                    if verb:
                        self.field[cur.x][cur.y] = "*"


field = Field(False)
field.add_ship(ship1.dots)
field.show()
print(field.ship_list)

print()

ai_field = Field(True)
ship2 = Ship(d, 2, False)
ai_field.add_ship(ship2.dots)
ai_field.show()
print(ai_field.ship_list)

d1 = Dot(6, 3)
print(ai_field.out(d1))

us_shot = Dot(6, 6)
ai_field.shot(us_shot)
ai_field.show()
print(ai_field.out(us_shot))
print(ai_field.busy)

print(us_shot in ai_field.busy)

class Player:
    def __init__(self):
        self.my_field = Field(False)
        self.enemy_field = Field(True)

    def ask(self):
        pass

    def move(self):
        self.ask()
        Field.shot()


class User(Player):

    def ask(self):
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        return Dot(x, y)


class AI(Player):

    def ask(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return Dot(x, y)


class Game:

    def __init__(self, user, user_field, computer, computer_field):
        self.user = user
        self.user_field = user_field
        self.computer = computer
        self.computer_field = computer_field

    # def random_board(self):
    #     while True:


    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass





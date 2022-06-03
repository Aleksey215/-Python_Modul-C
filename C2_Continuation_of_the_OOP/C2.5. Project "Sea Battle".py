# Итоговое практическое задание "Морской бой"
# 1. Суть написанного приложения — игра «Морской бой».
# 2. Интерфейс приложения должен представлять из себя консольное окно с двумя полями 6х6 вида:
#
#     | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | О | О | О | О | О | О |
# 2 | О | О | О | О | О | О |
# 3 | О | О | О | О | О | О |
# 4 | О | О | О | О | О | О |
# 5 | О | О | О | О | О | О |
# 6 | О | О | О | О | О | О |
#
# 3. Игрок играет с компьютером. Компьютер делает ходы наугад,
#    но не ходит по тем клеткам, в которые он уже сходил.
# 4. Для представления корабля на игровой доске напишите класс Ship
#    (в конструктор передаём информацию о его положении на доске).
# 5. Опишите класс доски, на которую будут размещаться корабли.
# 6. Корабли должны находится на расстоянии минимум одна клетка друг от друга.
# 7. Корабли на доске должны отображаться следующим образом (пример):
#    | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | ■ | ■ | ■ | О | О | О |
# 2 | О | О | О | О | ■ | ■ |
# 3 | О | О | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |

# 8. На каждой доске (у ИИ и у игрока) должно находится следующее количество кораблей:
#    1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.
# 9. Запретите игроку стрелять в одну и ту же клетку несколько раз.
#    При ошибках хода игрока должно возникать исключение.
#
#    | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | X | X| X | О | О | О |
# 2 | О | О | О | О| X | X |
# 3 | О | T | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |

# 10. В случае, если возникают непредвиденные ситуации, выбрасывать и обрабатывать исключения.
#     Буквой X помечаются подбитые корабли, буквой T — промахи.
# 11. Побеждает тот, кто быстрее всех разгромит корабли противника.

# class BoardOutException(Exception):
#     print("Вы пытаетесь выстрелить за пределы поля!")
#     print("Координаты вводятся от 1 до 6")


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, ship_len, bow_x, bow_y, horizontally, hit_point):
        self.ship_len = ship_len
        self.bow_x = bow_x
        self.bow_y = bow_y
        self.ship_direction = horizontally
        self.hit_point = hit_point

    def dots(self):
        if self.ship_direction:
            ship_points = [(self.bow_x, self.bow_y+i) for i in range(self.ship_len)]
        else:
            ship_points = [(self.bow_x+i, self.bow_y) for i in range(self.ship_len)]
        return ship_points


class Field:
    def __init__(self, hid):
        self.hid = hid
        self.field = [[' ' for i in range(7)] for j in range(7)]
        self.ship_list = []
        self.live_ship_list = []

    def show(self):
        if not self.hid:
            print("--------Поле игрока--------")
            for ship in self.ship_list:
                for dot in ship:
                    self.field[dot[0]][dot[1]] = '■'
        else:
            print("------Поле компьютера------")
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
        self.live_ship_list.append(ship)

    def shot(self, x, y):
        if 1 <= x <= 6 and 1 <= y <= 6:
            self.field[x][y] = "*"
        # else:
        #     raise BoardOutException

    def contour(self):
        cont = set()
        for ship in self.ship_list:
            print(ship)
        for ship in self.ship_list:
            for dot in ship:
                y_pos = (dot[0], dot[1] + 1)
                x_pos = (dot[0] + 1, dot[1])
                y_neg = (dot[0], dot[1] - 1)
                x_neg = (dot[0] - 1, dot[1])
                xy_pos = (dot[0] + 1, dot[1] + 1)
                xy_neg = (dot[0] - 1, dot[1] - 1)
                x_pos_y_neg = (dot[0] + 1, dot[1] - 1)
                x_neg_y_pos = (dot[0] - 1, dot[1] + 1)
                if y_pos not in ship:
                    cont.add(y_pos)
                if x_pos not in ship:
                    cont.add(x_pos)
                if y_neg not in ship:
                    cont.add(y_neg)
                if x_neg not in ship:
                    cont.add(x_neg)
                if xy_pos not in ship:
                    cont.add(xy_pos)
                if xy_neg not in ship:
                    cont.add(xy_neg)
                if x_pos_y_neg not in ship:
                    cont.add(x_pos_y_neg)
                if x_neg_y_pos not in ship:
                    cont.add(x_neg_y_pos)

    def out(self, x, y):
        if x > 6 or y > 6:
            return True
        else:
            return False


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
        user_shot = Dot(x, y)
        return user_shot


alex = User()
alex.ask()

ship1 = Ship(3, 1, 3, False, 3)
ship2 = Ship(2, 6, 1, True, 2)
pl1 = Player()

pl1.my_field.add_ship(ship1.dots())
pl1.my_field.show()


pl1.enemy_field.add_ship(ship2.dots())
pl1.enemy_field.show()

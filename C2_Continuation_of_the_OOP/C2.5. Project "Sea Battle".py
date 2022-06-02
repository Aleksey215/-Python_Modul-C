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


class Field:
    field = [[' ' for i in range(7)] for j in range(7)]

    def __init__(self, hid):
        self.hid = hid

    def show(self):
        for i in range(7):
            for j in range(7):
                if i == 0:
                    print(f"{j} ", end="  ")
                elif j == 0:
                    print(f"{i} ", end="|")
                else:
                    print(f" {self.field[i][j]} ", end="|")
            print()

    def add_ship(self, ship_dots):
        for dot in ship_dots:
            self.field[dot[0]][dot[1]] = '■'

    def shot(self, x, y):
        self.field[x][y] = "*"


my_field = Field(True)
my_field.show()
print()
my_field.shot(2, 2)
my_field.show()

print()


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


ship1 = Ship(4, 1, 1, False, 4)
print(ship1.dots())
for dot in ship1.dots():
    print(f"x={dot[0]}, y={dot[1]}")

my_field.add_ship(ship1.dots())
my_field.show()


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Player:
    pass


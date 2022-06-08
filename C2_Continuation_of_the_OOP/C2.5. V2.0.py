import random
import time


class BoardException(Exception):
    pass


class OutBoardException(BoardException):
    def __str__(self):
        return "Вы стреляете за пределы поля!"


class RepeatBoardException(BoardException):
    def __str__(self):
        return "Вы стреляете в клетку, в которую уже стреляли!"


class UnableToAddShipBoardException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot{self.x, self.y}"


class Ship:
    def __init__(self, bow, length, horizontally):
        self.bow = bow
        self.length = length
        self.horizontally = horizontally
        self.hp = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            if self.horizontally:
                ship_dots.append(Dot(self.bow.x, self.bow.y + i))
            else:
                ship_dots.append(Dot(self.bow.x + i, self.bow.y))
        return ship_dots


class Board:
    def __init__(self, hid=False):
        self.hid = hid
        self.ships = []
        self.sunk_ships = 0
        self.busy = []
        self.board = [[' '] * 7 for i in range(7)]
        self.shot_list = []

    def show(self):
        if self.hid:
            print("------Поле компьютера------")
            for i in range(7):
                for j in range(7):
                    if self.board[i][j] == '■':
                        self.board[i][j] = ' '
        else:
            print("-----Поле пользователя-----")

        for i in range(7):
            for j in range(7):
                if i == 0:
                    print(f"{j} ", end="  ")
                elif j == 0:
                    print(f"{i} ", end="|")
                else:
                    print(f" {self.board[i][j]} ", end="|")
            print()
        print("---------------------------")

    def out(self, dot):
        if dot.x < 1 or dot.x > 6:
            return True
        elif dot.y < 1 or dot.y > 6:
            return True
        else:
            return False

    def contour(self, ship, display=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        for dot in ship.dots:
            for dx, dy in near:
                cur = Dot(dot.x + dx, dot.y + dy)
                if not self.out(cur) and cur not in self.busy:
                    self.busy.append(cur)
                if display and cur not in ship.dots:
                    self.board[cur.x][cur.y] = '*'

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) and dot in self.busy:
                raise UnableToAddShipBoardException
            else:
                self.busy.append(dot)
                self.board[dot.x][dot.y] = '■'
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(dot):
            raise OutBoardException
        elif dot in self.shot_list:
            raise RepeatBoardException
        elif dot in self.busy:
            for ship in self.ships:
                if dot in ship.dots:
                    print("Попадание!")
                    self.board[dot.x][dot.y] = 'X'
                    ship.hp -= 1
                    self.shot_list.append(dot)
                    if not ship.hp:
                        self.contour(ship, display=True)
                        self.sunk_ships += 1
                        print("Корабль уничтожен!")
                        return True
                    return True
                else:
                    print("Мимо!")
                    self.board[dot.x][dot.y] = '*'
                    self.busy.append(dot)
                    self.shot_list.append(dot)
                    return False
        else:
            print("Мимо!")
            self.board[dot.x][dot.y] = '*'
            self.busy.append(dot)
            self.shot_list.append(dot)
            return False


class Player:
    def __init__(self):
        self.board = Board()
        self.enemy_board = Board(hid=True)

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                # self.enemy_board.shot(self.ask())
                if self.enemy_board.shot(self.ask()):
                    self.board.show()
                    self.enemy_board.show()
                    return True
                else:
                    self.board.show()
                    self.enemy_board.show()
                    return False
            except BoardException as e:
                print(e)
                print("Пожалуйста, в7"
                      "Введите координаты заново!")
                continue


class User(Player):
    def ask(self):
        while True:
            try:
                x = int(input("enter x: "))
                y = int(input("enter y: "))
            except ValueError:
                print("Вводятся только цифры")
                continue
            else:
                return Dot(x, y)


class Ai(Player):
    def ask(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return Dot(x, y)


ai_ship2 = Ship(Dot(1, 1), 2, horizontally=False)
us_ship2 = Ship(Dot(3, 3), 2, horizontally=True)

user_board = Board()
user_board.add_ship(us_ship2)

ai_board = Board(hid=True)
ai_board.add_ship(ai_ship2)

user = User()
ai = Ai()

user.board = user_board
user.enemy_board = ai_board

ai.board = ai_board
ai.enemy_board = user_board

user_board.show()
ai_board.show()
win = False
while not win:
    if user.move():
        while True:
            if len(user.board.ships) == user.board.sunk_ships:
                print(f"Победил компьютер!")
                win = True
                break
            elif len(ai.board.ships) == ai.board.sunk_ships:
                print(f"Победил пользователь!")
                win = True
                break

            if user.move():
                continue
            else:
                break
    if not win:
        time.sleep(3)
        if ai.move():
            while True:
                if len(user.board.ships) == user.board.sunk_ships:
                    print(f"Победил компьютер!")
                    win = True
                    break
                elif len(ai.board.ships) == ai.board.sunk_ships:
                    print(f"Победил пользователь!")
                    win = True
                    break

                if ai.move():
                    continue
                else:
                    break

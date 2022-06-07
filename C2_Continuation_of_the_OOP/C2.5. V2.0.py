class BoardException(Exception):
    pass


class OutBoardException(BoardException):
    def __str__(self):
        return "Вы стреляете за пределы поля!"


class RepeatBoardException(BoardException):
    def __str__(self):
        return "Вы стреляете в клетку, которая уже занята!"


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
        self.busy = []
        self.board = [[' '] * 7 for i in range(7)]

    def show_board(self):
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
                cur = Dot(dot.x+dx, dot.y+dy)
                if not self.out(cur) and cur not in self.busy:
                    if display:
                        self.board[cur.x][cur.y] = '*'
                    self.busy.append(cur)

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
        elif dot in self.busy:
            for ship in self.ships:
                if dot in ship.dots:
                    print("Попадание!")
                    self.board[dot.x][dot.y] = 'X'
                    ship.hp -= 1
                    if ship.hp == 0:
                        self.contour(ship, display=True)
                        print("Корабль уничтожен!")
                else:
                    raise RepeatBoardException
        else:
            print("Мимо!")
            self.board[dot.x][dot.y] = '*'
            self.busy.append(dot)


bow_ = Dot(1, 2)
ship = Ship(bow_, 2, True)
print(ship.dots)


dot = Dot(1, 2)
dot2 = Dot(1, 3)
user_board = Board()
print(user_board.out(dot))
user_board.show_board()
ai_board = Board(True)
ai_board.show_board()
ai_board.add_ship(ship)
ai_board.show_board()

print("busy:", ai_board.busy)

user_board.add_ship(ship)

user_board.shot(dot)
user_board.shot(dot2)
user_board.show_board()

print(user_board.busy)

user_board.show_board()

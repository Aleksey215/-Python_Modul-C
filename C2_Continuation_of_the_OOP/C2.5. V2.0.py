from random import randint
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
            if self.out(dot) or dot in self.busy:
                raise UnableToAddShipBoardException
        for dot in ship.dots:
            self.busy.append(dot)
            self.board[dot.x][dot.y] = '■'
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot):
        if self.out(dot):
            raise OutBoardException

        if dot in self.busy:
            raise RepeatBoardException

        self.busy.append(dot)
        for ship in self.ships:
            if dot in ship.dots:
                ship.hp -= 1
                self.board[dot.x][dot.y] = 'X'
                if not ship.hp:
                    self.sunk_ships += 1
                    self.contour(ship, display=True)
                    print("Корабль уничтожен!")
                    return True
                else:
                    print("Корабль ранен!")
                    return True

        print(f"{dot} Мимо!")
        self.board[dot.x][dot.y] = '*'
        self.busy.append(dot)
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board, enemy_board):
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                if self.enemy_board.shot(target):
                    return True
                else:
                    return False
            except BoardException as e:
                print(e)
                print("Пожалуйста, введите координаты заново!")
                continue


class User(Player):
    def ask(self):
        while True:
            try:
                x = int(input("Введите x: "))
                y = int(input("Введите y: "))
            except ValueError:
                print("Вводятся только цифры")
                continue
            else:
                return Dot(x, y)


class Ai(Player):
    def ask(self):
        x = randint(1, 6)
        y = randint(1, 6)
        return Dot(x, y)


class Game:
    def __init__(self):
        us_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True
        self.user = User(us_board, ai_board)
        self.ai = Ai(ai_board, us_board)

    def try_board(self):
        length_list = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        attempts = 0
        for length in length_list:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship_bow = Dot(randint(1, 6), randint(1, 6))
                ship = Ship(bow=ship_bow, length=length, horizontally=randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("___________________________")
        print("<<<  Добро пожаловать   >>>")
        print("<<<       в игру        >>>")
        print("<<<    Морской бой!     >>>")
        print("___________________________")
        print("<<<   чтобы выстрелить  >>>")
        print("<<<    введите х и у    >>>")
        print("<<<  х - номер строки   >>>")
        print("<<<  у - номер столбца  >>>")
        print()

    # def play(self):
    #     print()
    #     win = False
    #     while not win:
    #         print()
    #         self.user.board.show()
    #         self.ai.board.show()
    #         print("-----Ход пользователя------")
    #         if self.user.move():
    #             while True:
    #                 if len(self.user.board.ships) == self.user.board.sunk_ships:
    #                     print(f"Победил компьютер!")
    #                     win = True
    #                     break
    #                 elif len(self.ai.board.ships) == self.ai.board.sunk_ships:
    #                     print(f"Победил пользователь!")
    #                     win = True
    #                     break
    #
    #                 if self.user.move():
    #                     continue
    #                 else:
    #                     break
    #
    #         if not win:
    #             print()
    #             print("----------Ход ИИ-----------")
    #             time.sleep(3)
    #             if self.ai.move():
    #                 while True:
    #                     if len(self.user.board.ships) == self.user.board.sunk_ships:
    #                         print(f"Победил компьютер!")
    #                         win = True
    #                         break
    #                     elif len(self.ai.board.ships) == self.ai.board.sunk_ships:
    #                         print(f"Победил пользователь!")
    #                         win = True
    #                         break
    #
    #                     if self.ai.move():
    #                         continue
    #                     else:
    #                         break

    def play(self):
        win = False
        move_num = 0
        while not win:
            self.user.board.show()
            self.ai.board.show()

            if len(self.user.board.ships) == self.user.board.sunk_ships:
                print(f"Победил компьютер!")
                win = True
                return win

            if len(self.ai.board.ships) == self.ai.board.sunk_ships:
                print(f"Победил пользователь!")
                win = True
                return win

            if move_num % 2 == 0:
                print()
                print("-----Ход пользователя-----")
                move_num += 1
                if self.user.move():
                    move_num -= 1
                    continue
                else:
                    continue
            else:
                print()
                print("----------Ход ИИ-----------")
                move_num += 1
                time.sleep(3)
                if self.ai.move():
                    move_num -= 1
                    continue

    def start(self):
        self.greet()
        self.play()


g = Game()
g.start()
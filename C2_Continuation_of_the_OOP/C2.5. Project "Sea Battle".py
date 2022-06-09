# C2.5. Итоговое практическое задание
from random import randint

class Dot:
    # Прием параметров х и у для координат точек
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Данный метод сравнивает объекты класса "Dot" и выдает True при равенстве
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Метод для вывода точки в консоль
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

# Создание собственных исключений
# создание класса для доски (Родительский класс - исключение)
class BoardException(Exception):
    pass
# Создание исключения для выстрела за доску
# Это дочерний класс от класса исключение для доски
# Его метод выводит пользователю сообщение о выходе за доску
class OutBoardException(BoardException):
    def __str__(self):
        return "Координаты вашего выстрела за пределами поля"

# Так же дочерний класс для сообщения о повторном выстреле в точку
class RepeatBoardException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

# Класс для внутренней логики при размещении кораблей на доске
class WrongPositionOnBoardException(BoardException):
    pass

class Ship:
    # Инициализация корабля
    # Создание основных атрибутов корабля:
    # bow - задается нос корабля
    # о - положение корабля (Вертикальное/Горизонтальное)
    # l - длина корабля, а длина это еще и жизни
    def __init__(self, bow, o, l):
        self.bow = bow
        self.o = o
        self.l = l
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            # Горизонтальное положение корабля
            if self.o == 0:
                cur_x += i
            # Вертикальное положение корабля
            elif self.o == 1:
                cur_y += i
            # добавление точек в список
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    # Показывает попадание в корабль
    def shooten(self, shot):
        return shot in self.dots

# Создание класса игрового поля (Доска)
class Board:
    # определяется видимость поля и его размер
    def __init__(self, hid = False, size=6):
        # видимость поля
        self.hid = hid
        # размер поля
        self.size = size

        # создание самой игровой сетки
        self.field = [[" "] * size for i in range(size)]

        # кол-во пораженных кораблей
        self.count = 0

        # список кораблей на доске
        self.ships = []

        # хранит точки, которые использованы (выстрелом или кораблем с контуром)
        self.busy = []

    # метод вывода корабля на доску
    def __str__(self):
        # в эту переменную записывается вся доска
        res = ""
        res += "    1   2   3   4   5   6  "
        # формирование внешнего вида строк доски
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        # Если доска скрыта, то меняется символ корабля на символ пустой клетки
        if self.hid:
            res = res.replace("■", " ")
        return res

    # проверка принадлежности точки к доске
    def out(self, d):
        # Если точка не в интервале от 0 до размера доски (по х и по у)
        # то вернется ложь
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    # Создание контура корабля
    # verb - определяет необходимость вывода контура
    def contour(self, ship, verb = False):
        # Создание списка точек, которые занимают все клетки
        # в радиусе 1 от каждой точки корабля.
        # (0, 0) - это точка корабля.
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                # если точка в пределах поля и не в списке занятых
                if not(self.out(cur)) and cur not in self.busy:
                    # и если контур видемый
                    if verb:
                        # то в клетки записывается символ "*"
                        self.field[cur.x][cur.y] = "."
                    # добавление точки в список занятых,
                    # видимость контура не влияет на это условие
                    self.busy.append(cur)

    # Метод добавления корабля на доску
    def add_ship(self, ship):
        # Для точек корабля
        for d in ship.dots:
            # Если точка за пределами доски или занята
            if self.out(d) or d in self.busy:
                # то вылавливается исключение
                raise WrongPositionOnBoardException()
        # Для точек корабля (После проверки на исключение)
        for d in ship.dots:
            # присваивается символ ■
            self.field[d.x][d.y] = "■"
            # и точка добавляется в список занятых
            self.busy.append(d)

        # корабль добавляется в список кораблей на доске
        self.ships.append(ship)
        # и для корабля создается контур
        self.contour(ship)

    # Выстрел
    def shot(self, d):
        # Если введенная точка за полем - активируется исключение
        if self.out(d):
            raise OutBoardException()

        # Если введенная точка входит в список занятых, так же исключение
        if d in self.busy:
            raise RepeatBoardException()
        # Если не возникло исключений то точка добавляется в список занятых
        self.busy.append(d)

        for ship in self.ships:
            # Если точка входит в точки корабля, то это попадание
            if ship.shooten(d):
                # Уменьшается жизнь
                ship.lives -= 1
                # В место попадания ставится "Х"
                self.field[d.x][d.y] = "X"
                # Если жизни кончались
                if ship.lives == 0:
                    # Увеличивается счетчик уничтоженных кораблей
                    self.count += 1
                    # Контур корабля становится видимым для пользователя
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    # Завершение хода
                    return False
                # Если жизни еще есть
                else:
                    # то выводится сообщение
                    print("Корабль ранен!")
                    # и ход продолжается
                    return True
        # Если введенная точка не входит в точки корабля
        # то ставится символ "."
        self.field[d.x][d.y] = "."
        print("Мимо!")
        # и ход заканчивается
        return False
    # Обнуление списка занятых точек перед началом игры
    # данный список использовался для расстановки кораблей
    def begin(self):
         self.busy = []

# Класс игрока (родитель для ИИ и пользователя)
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    # создан для дочерних классов
    def ask(self):
        raise NotImplementedError()

    # Метод хода
    def move(self):
        # В бесконечном цикле
        while True:
            try:
                # запрашиваются координаты
                target = self.ask()
                # и проверяется сделанный выстрел
                repeat = self.enemy.shot(target)
                # если выстрел успешный, то повторяем
                return repeat
            # если нет то срабатывает исключение
            except BoardException as e:
                print(e)

# Класс ИИ дочерний от класса игрок
class Ai(Player):
    # Метод запроса на ввод координат для выстрела
    def ask(self):
        # ввод случайных чисел для координат
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход ИИ: {d.x + 1} {d.y + 1}")
        return d

# Дочерний класс от класса игрок
class User(Player):
    # Запрос на ввод координат
    def ask(self):
        # В бесконечном цикле
        while True:
            cords = input("Ваш ход: ").split()
            if len(cords) != 2:
                print("Введите две координаты!")
                continue

            # через множественное присвоение задаем х и у
            x, y = cords

            # проверка, что введены числа
            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа!")
                continue

            # запись в формате чисел
            x, y = int(x), int(y)

            # возврат готовой точки с поправкой на индекс
            return Dot(x - 1, y - 1)

# класс игра
class Game:
    # создание конструктора
    # размер доски по умолчанию равен 6
    def __init__(self, size = 6):
        self.size = size
        # создание доски для игрока
        pl = self.random_board()
        # создание доски для компьютера
        co = self.random_board()
        # у компьютера доска скрыта
        co.hid = True

        # создание игроков
        self.ai = Ai(co, pl)
        self.us = User(pl, co)

    # метод создания доски с расстановленными кораблями
    def try_board(self):
        # список с длинами кораблей
        lens = [3, 2, 2, 1, 1, 1, 1]
        # создаем доску заданного размера
        board = Board(size=self.size)
        # кол-во попыток
        attempts = 0
        # для каждого корабля l в списке lens
        for l in lens:
            # в бесконечном цикле
            while True:
                # увеличиваем попытки
                attempts += 1
                # если кол-во попыток больше 2000
                if attempts > 2000:
                    # возвращаем пустое поле
                    return None
                # пока кол-во попыток меньше 2000, задаем рандомную точку для носа корабля,
                # случайно определяем положение корабля (вертикальное или горизонтальное),
                # задаем длину корабля
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1), l)
                try:
                    # добавление корабля
                    board.add_ship(ship)
                    break
                except WrongPositionOnBoardException:
                    pass
        # обнуление списка busy
        board.begin()
        # возврат доски
        return board

    # метод гарантированного создания доски
    def random_board(self):
        # создание пустой доски
        board = None
        # пока доска пустая
        while board is None:
            # вызывается метод попытки создания доски
            board = self.try_board()
        # возвращаем доску
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

    # создание игрового цикла
    def loop(self):
        # номер хода
        num = 0
        # в бесконечном цикле
        while True:
            # выводим доски с подписью
            print("-" * 27)
            print("Доска пользователя:")
            print(self.us.board)
            print(self.us.board.busy)
            print("-" * 27)
            print("Доска компьютера:")
            print(self.ai.board)
            print(self.ai.board.busy)
            print("-" * 27)
            # если номер хода четный - ходит игрок
            if num % 2 == 0:
                print("Ходит пользователь!")
                # вызываем метод хода
                repeat = self.us.move()
            else:
                # если номер хода не четный - ходит компьютер
                print("Ходит компьютер!")
                # метод хода
                repeat = self.ai.move()
            # если ход надо повторить
            if repeat:
                # номер хода уменьшается на 1
                # чтобы не увеличить номер хода
                num -= 1

            # если кол-во уничтоженных кораблей
            # на доске компьютера равно 7
            # то победил игрок
            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                # остановка цикла
                break

            # если кол-во уничтоженных кораблей
            # на доске игрока равно 7
            # то победил компьютер
            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            # увеличение номера хода
            num += 1
    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
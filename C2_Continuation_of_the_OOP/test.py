
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
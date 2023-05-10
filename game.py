def hello():
    print("Добро пожаловать в крестики - нолики!")
    print("Чтобы сделать ход, необходимо вводить номер ячейки от 1 до 9.")
    print("Игроки ходят по очереди - сначала крестик, после него нолик.")


board = [i for i in range(1, 10)]

def print_board():
    print("-" * 19)
    for i in range(3):
        print("| ", board[i*3]," | ", board[1 + i*3], " | ", board[2 + i*3], " |")
        print("-" * 19)

def winner():
    win = False
    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # вертикали
        (0, 4, 8), (2, 4, 6)                # диагонали
    )
    for i in win_comb:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            win = board[i[0]]
    return win


def game():
    hello()
    print_board()

    step = 0

    while step < 9 and winner() == False:
        if step % 2 == 0:
            print("~Ходит КРЕСТИК~")
        elif step % 2 != 0:
            print("~Ходит НОЛИК~")


        cell = input("Введите номер ячейки для хода: ")


        if not cell.isdigit():
            print(f"Вы ввели : {cell}.")
            print("Введите число, а не символы. ")
            continue
        elif int(cell) < 1 or int(cell) > 9:
            print(f"Число {cell} вне диапазона (0;9).")
            continue
        elif board[int(cell) - 1] in ("X", "0"):
            print(f"Вы сходили на клетку: {cell}")
            print("Эта клетка уже занята.")
            continue


        if step % 2 == 0:
            char = "X"
        elif step % 2 != 0:
            char = "0"

        print(f"Вы сходили на клетку: {cell}")

        board[int(cell) - 1] = char
        step += 1
        print_board()

    if step == 9 and winner() == False:
        print("У вас ничья!")
    else:
        print("Победитель", winner(), "!!!!")

game()

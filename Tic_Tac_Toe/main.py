# Tic Tac Toe Game  + AI

def print_field(field):
    print("  0  1  2")
    for col in range(0, 3):
        print(col, end="")
        for row in field[col]:
            if row > 1 or row < 0:
                print(" - ", end="")
            if row == 1:
                print(" X ", end="")
            if row == 0:
                print(" O ", end="")
        print()

def check_win(field):
    # check win in row
    for row in range(0, 3):
        win=1
        next_elem = field[row][0]
        for col in range(0,3):
            if next_elem != field[row][col] or field[row][col] == 2:
                win=0
        if win == 1:
            return next_elem
    # chheck win in col
    for col in range(0, 3):
        win = 1
        next_elem = field[0][col]
        for row in range(0,3):
            if next_elem != field[row][col] or field[row][col] == 2:
                win=0
            if col<2:
                next_elem = field[row][col+1]
        if win == 1:
            return next_elem
    # check win on X
    win = 1
    for elem in range(0, 3):
        next_elem = field[0][0]
        if next_elem != field[elem][elem] or field[elem][elem] == 2:
            win = 0
    if win == 1:
        return next_elem
    # check win on reverse X
    win = 1
    for elem in range(2, 0, -1):
        next_elem = field[0][2]
        if next_elem != field[elem][elem] or field[elem][elem] == 2:
            win = 0
    if win == 1:
        return next_elem
    raise ValueError


def win(player):
    # print who wins based on return of check_win functions
    if player == 0:
        print("O Win!")
    if player == 1:
        print("X Win!")


field = [[2, 2, 1], [2, 1, 2], [1, 2, 2]]

print_field(field)
win(check_win((field)))

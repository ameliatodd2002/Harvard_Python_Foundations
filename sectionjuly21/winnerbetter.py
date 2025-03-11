def winner(board):
    x_win = False
    o_win = False

    for row in board:
        if row.count('X'):
            x_win = True
        if row.count('O'):
            o_win = True


def main():
    a = [['X', 'X', 'X'],
         ['X', None, None],
         ['X', 'X', None]]

    winner(a)

main()
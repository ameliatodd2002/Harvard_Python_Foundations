def counter(board):
    for row in board:
        for spot in row:
            if spot == 'X':
                count_x += 1
            elif spot == 'O':
                count_o += 1
        return (count_x == count_o) or (count_x == count_o + 1)

def main():
    a = [[None, 'O', None],
         ['X', 'O', None],
         [None, 'X', 'O']]

    print(counter(a))

main()
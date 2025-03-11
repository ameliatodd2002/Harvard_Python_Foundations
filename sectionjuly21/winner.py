def winner(board):
    x_col = 0
    x_col2 = 0
    x_col3 = 0
    for row in board:
        if row[0] and row[1] and row[2] == 'X':
            print ('X wins!')
        elif row[0] == 'X':
            x_col +=1
        elif row[1] == 'X':
            x_col2 +=1
        elif row[2] == 'X':
            x_col3 +=1
        elif row[0] and row[1] and row[2] == 'O':
            print ('O wins!')
        elif row[0] == 'X':
            x_col +=1
        elif row[1] == 'X':
            x_col2 +=1
        elif row[2] == 'X':
            x_col3 +=1
    if x_col == 3 or x_col2 == 3 or x_col3 == 3:
        print('X wins!')



def main():
    a = [['X', None, 'X'],
         ['X', None, None],
         ['X', 'X', None]]

    winner(a)

main()
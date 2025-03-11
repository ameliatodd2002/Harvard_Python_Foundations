row_char = '*'
col_char = '|'
height = 4
width = 9

def horiz_line():
    for i in range (width):
        print(row_char, end='')
    print ()

def left_only():
    for i in range (height):
        print(col_char)
    print ()

def left_right ():
        for i in range (height):
             print (col_char, end='')
             for j in range (width):
                  space ()
            print (col_char)
        

horiz_line()

left_only()
horiz_line()


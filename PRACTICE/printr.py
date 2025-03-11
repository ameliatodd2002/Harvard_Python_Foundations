def print_range(i,j):
    print (f'[{i},{j}]:', end='')
    s = ''
    if j > i:
        for n in range (i,j+1):
            s += f' {n},'
        print (s[:-1])
    if i > j:
        for n in range (i, j-1, -1):
            s += f' {n},'
        print (s[:-1])
    if i == j:
        print (i)

print_range(5, 5)


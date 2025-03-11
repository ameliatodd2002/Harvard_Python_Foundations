def print_range(i,j):
    print (f' [{i},{j}]:', end="")
    s = ''
    if i <= j:
        for x in range (i,j+1):
            s += f' {x},'
        s = s[:-1]
        print(s)
    if i > j:
        for x in range (i,j-1,-1):
            s += f' {x},'
        s = s[:-1]
        print(s)
    if i == j:
        for x in range (i,j+1):
            print (' ', x)

def main():
    print_range(5,5)

if __name__ == "__main__":
    main()
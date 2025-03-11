def triangle():
    y = int(input("How tall?"))
    for i in range (y):
        print ((" " * i) + ('*' * (y - i)))

triangle()

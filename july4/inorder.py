def in_order(a, b, c):
    if (a <= b and b <= c) or (a >= b and b >= c):
        print ("in order")
    else:
        print("not in order")

in_order(4,3,2)
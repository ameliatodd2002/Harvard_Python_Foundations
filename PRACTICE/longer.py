def print_longer(x, y):
    if len(x) > len(y):
        print (x, "is the longer list and its last element is", x[-1])
    if len(y) > len(x):
        print (y, "is the longer list and its last element is", y[-1])
    if len(x) == len(y):
        print("The lists are the same length!")

print_longer(['chocolate', 'vanilla'], [1, 5, 9, 7])
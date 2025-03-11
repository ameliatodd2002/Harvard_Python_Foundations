def five_digits():
    for i in range (10000,100000):
        if reverse(4 * i) == i:
            print (i)

def reverse(num):
    x = 0
    while num > 0:
        x = (x * 10) + (num % 10)
        num = num // 10
    return(x)


five_digits()
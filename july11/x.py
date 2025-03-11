import random

def sm():
    x = 0
    print(x, end='')
    while x <= 90:
        x = random.randint(1, 100)
        print (x, end ='')
    print()

sm()
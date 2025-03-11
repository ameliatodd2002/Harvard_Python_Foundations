import random

def dice():
    di1 = random.randint(1,6)
    di2 = random.randint(1,6)
    total_rolls = 0
    while di1 != di2:
        total_rolls += 1
        return di1, di2
    if di1 == di2:
        print (f' It took {total_rolls}')
dice()


year = 2000

def print_leap_years():
    for y in range (1990, 2111):
        if (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0):
            print (y)

print_leap_years()
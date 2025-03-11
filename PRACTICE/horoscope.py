def sign(month, day):
    if before(month, day, 1, 19):
        sign = 'Capricorn'
    elif before(month, day, 2, 18):
        sign = 'Aquarius'
    elif before(month, day, 3, 20):
        sign = 'Pisces'
    elif before(month, day, 4, 19):
        sign = 'Aries'
    elif before(month, day, 5, 20):
        sign = 'Taurus'
    elif before(month, day, 6, 20):
        sign = 'Gemini'
    elif before(month, day, 7, 22):
        sign = 'Cancer'
    elif before(month, day, 8, 22):
        sign = 'Leo'
    elif before(month, day, 9, 22):
        sign = 'Virgo'
    elif before(month, day, 10, 22):
        sign = 'Libra'
    elif before(month, day, 11, 21):
        sign = 'Scorpio'
    elif before(month, day, 12, 21):
        sign = 'Saggitarius'
    else:
        sign = 'Capricorn'
    return sign

def before(month1, day1, month2, day2):
    return month1 < month2 or (month1 == month2 and day1 <= day2)

def main():
    month = int(input("Write your birth month as a number"))
    day = int(input("Write your birth day as a number"))
    asign = sign(month, day)
    print (f'Your astrological sign is {asign}')

main()
def before(month1, day1, month2, day2):
    if month1 != 12:
        if month1 + 1 == month2:
            return True
    if month1 == 12:
        if month2 == 1:
            return True
    elif month1 == month2 and day1 < day2:
        return True
    else:
        return False

def sign(month, day):
    list31 = [1, 3, 5, 7, 8, 10, 12]
    list30 = [4, 6, 9, 11]
    list29 = [2]

    if month in list31:
        if not (1 <= day <= 31):
            return "INVALID_DATE"
    elif month in list30:
        if not (1 <= day <= 30):
            return "INVALID_DATE"
    elif month in list29:
        if not (1 <= day <= 29):
            return "INVALID_DATE"

    if before (month, day, 4, 20):
        return ("Aries")
    elif before (month, day, 5, 21):
        return ("Taurus")
    elif before (month, day, 6, 21):
        return ("Gemini")
    elif before (month, day, 7, 23):
        return ("Cancer")
    elif before (month, day, 8, 23):
        return ("Leo")
    elif before (month, day, 9, 23):
        return ("Virgo")
    elif before (month, day, 10, 23):
        return ("Libra")
    elif before (month, day, 11, 22):
        return ("Scorpio")
    elif before (month, day, 12, 22):
        return ("Sagittarius")
    elif before (month, day, 1, 20):
        return ("Capricorn")
    elif before (month, day, 2, 19):
        return ("Aquarius")
    elif before (month, day, 3, 21):
        return ("Pisces")

def main():
    month = int(input("Enter the month of your birthday: "))
    day = int(input("Enter the day of your birthday: "))
    print(sign (month, day))

if __name__ == '__main__':
    main()
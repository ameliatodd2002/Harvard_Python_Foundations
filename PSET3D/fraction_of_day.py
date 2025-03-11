def fraction_of_day(hour, minute, second, am_pm):
    fraction = 0.0000

    if hour == 0 and am_pm == 'A':
        hour == 12
    elif (hour == 12) and (minute == 0) and (second == 0) and (am_pm == 'A'):
        fraction = 0.0000
        hour = 1
    elif am_pm == 'A':
        fraction = float((((hour * 60) * 60) + (minute * 60) + second) / 86400)
    elif am_pm == 'P':
        fraction = float(((((hour * 60) * 60) + (minute * 60) + second) / 86400) + 0.5000)
        hour += 1

    return fraction


def main():
    x = ['12:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM']
    fractions = []
    for i in range (12):
        fraction = fraction_of_day(i, 0, 0, 'A')
        fractions.append(fraction)

    for i in range (12):
        fraction = fraction_of_day(i, 0, 0, 'P')
        fractions.append(fraction)

    print(f"{'Time' : >7}{'Fraction Since Midnight' : >32}")
    for j in range (24):
        print(f"{x[j] : >10}{fractions[j] : >12.4f}")

if __name__ == '__main__':
    main()


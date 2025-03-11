def print_change(day1_price, day2_price, day1_num):
    print(f' Largest change of {abs(day2_price - day1_price)} from  {day1_price}  to  {day2_price} occurred between day #{day1_num} and day #{day1_num + 1}.')

def find_change():
    max_change = 0
    x = 0
    y = 0
    day1_num = 0
    for i in range (10):
        if i == 0:
            x = int(input(f"Enter the stock price for day {i + 1}: "))

        if i != 0:
            y = int(input(f"Enter the stock price for day {i + 1}: "))
            change = abs(y - x)
            if change > max_change:
                max_change = change
                day1_num = i
                day1_price = x
                day2_price = y
            x = y

    return [day1_price, day2_price, day1_num]

def main():
    res = find_change()
    day1_price = res[0]
    day2_price = res [1]
    day1_num = res[2]
    print_change(day1_price, day2_price, day1_num)


if __name__ == '__main__':
    main()
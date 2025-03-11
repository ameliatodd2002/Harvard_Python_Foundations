def print_change(day1_price, day2_price, day1_num):
    print(f'Largest change of {abs(day2_price - day1_price)} from  {day1_price}  to  {day2_price} occurred between day #{day1_num} and day #{day1_num + 1}.')

def find_change():
    price1 = int(input("Price:"))
    price2 = 0
    max_change = 0
    day1_price = 0
    day2_price = 0
    for i in range (11):
        price2 = int(input("Price:"))
        change = abs(price2 - price1)
        if change > max_change:
            max_change = change
            day1_price = price1
            day2_price = price2
            day1_num = i +1
        else:
            change = change
        price1 = price2
    print_change (day1_price, day2_price, day1_num)


def main():
    find_change()

main()
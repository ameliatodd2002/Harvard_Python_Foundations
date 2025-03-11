def baggage_fee(num):
    if num == 1:
        return 35
    elif num == 2:
        return 35 + 45
    else:
        fee = 35 + 45 + (num - 2) * 150
    return fee

def main():
    num = int(input("How many bags?"))
    print (f"The baggage fee for {num} bag is", baggage_fee(num))

if __name__ == "__main__":
    main()
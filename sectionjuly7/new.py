def print_range(i, j):
    if i < j:
        sequence = range(i, j+1)
    elif i > j:
        sequence = range(i, j-1, -1)
    else:
        sequence = [i]

    print(f"", ', '.join(str(num) for num in sequence))


def main():
    print_range(2, 7)
    print_range(19, 11)
    print_range(5, 5)


if __name__ == '__main__':
    main()
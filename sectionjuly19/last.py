def last_items(lsts):
    last = []
    for x in lsts:
        last.append(x[-1])
    return last

def main():
    input_1 = [[1, 2, 10], [5, 2, 1, 3], [3, 8]]
    print(last_items(input_1))

main()
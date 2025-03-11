def my_sort(lst):
    for i in range (len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1] = lst[i]
            lst[i] = lst [i + 1]
    return lst


def main():
    data = [3, 5, 1, 7, 9, 8, 2, 6, 4, 10]
    print(my_sort(data))

main()
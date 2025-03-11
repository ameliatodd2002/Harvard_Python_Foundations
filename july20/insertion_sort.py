# PROBLEM: Implement insertion sort


# Swap the elements i and j in list a
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def insertion_sort(a):
    for i in range (len(a)):
        j = i
        while j >= 1 and (a[j-1] > a[j]):
            swap(a, j-1, j)
            j = j - 1


def main():
    a = [ 2, 1, 9, 7, 6, 4, 8, 3, 5 ]
    insertion_sort(a)
    print(a)


if __name__ == "__main__":
    main()
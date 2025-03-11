def selection_sort(data):
    """
    Sorts the list data using selection sort. Returns Nothing.
    """
 
    for i in range(len(data)):
        minimum = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minimum]:
                minimum = j
        temp = data[i]
        data[i] = data[minimum]
        data[minimum] = temp




def main():
    # Add your solution to the problem that makes use of
    # the above to sort a list.
    nums = [ 3, 1, 4, 1, 5, 9] 
    selection_sort(nums) 
    print(nums)


if __name__ == "__main__":
    main()

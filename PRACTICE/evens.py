def sum_of_evens():
    n = int(input("Pick an number"))
    sum = 0
    for i in range (2, n+1):
        if (i % 2 == 0):
            sum += i
    print("The sum is", sum)

sum_of_evens()


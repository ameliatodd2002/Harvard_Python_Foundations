# PROBLEM:  What values are stored in the list a after the loop has run?

def main():
    a = [ 1, 7, 5, 6, 4, 14, 11 ]
    for i in range(len(a) - 1):
        #has to be len(a) - 1 bc the code is looking ahead to the next value on the list (i +1), so if we dont do len(a) - 1 it will be out of range - WHENEVER YOU USE i + 1 IN FOR LOOP YOUR RANGE NEEDS TO BE -1 SO ITS NOT OUT OF RANGE
        if (a[i] > a[i + 1]):
            a[i + 1] = a[i + 1] * 2
    print(a)

if __name__ == "__main__":
    main()
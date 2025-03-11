# PROBLEM: Write a loop to read in a few numbers from the user and
# report the sum back.
# Use a "constant" variable N to decide how many to read.

# ANSWER:
def main():
    n = 3
    sum = 0
    for i in range (n):
        sum += int(input("Please enter a number"))
    print ("the sum is", sum)

if __name__ == "__main__":
    main()

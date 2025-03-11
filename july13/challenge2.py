# PROBLEM: Complete this code to input N numbers and
# find the maximum and minimum numbers entered.
# Your solution must use append and use the built-in max
# and min functions
# QUESTION: What are the advantages / disadvantages
# of this approach compared to how we did it originally?

def main():
    N = 5
    x = []
    for i in range(N):
       num = int(input("Please enter a number: "))
       x.append(num)
    print("The largest value you entered is", max(x))
    print("The smallest value you entered is", min(x))
    #don't want to do this when we are using a range of trillions of numbers bc it wastes memory

if __name__ == "__main__":
    main()

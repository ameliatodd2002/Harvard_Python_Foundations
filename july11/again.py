import random

# PROBLEM: Write a function that keeps flipping a coin until
# we get n heads in a row.

def flip_until_n_heads_in_a_row(n):
    totalFlips = 0
    hs = 0
    while hs != n:
        print(coinflip(), end='')
        if coinflip() == "H":
            hs += 1
        else:
            hs = 0
        totalFlips += 1
    print(f"\nDone! It took {totalFlips} flips")

def coinflip():
    x = random.randint(0,1)
    if x == 0:
        return ("H")
    if x == 1:
        return ("T")

def main():
    num = int(input("How many heads in a row? "))
    flip_until_n_heads_in_a_row(num)

if __name__ == "__main__":
    main()

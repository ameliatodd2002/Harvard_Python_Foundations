import random

def coin_flip():
    flip = (random.randint(0, 1))
    if flip:
        return 'H'
    else:
        return 'T'


def main():
    c = coin_flip()
    print(f"You flipped a {c}")
    if c == 'H':
        print("I win")
    else:
        print ("You win!")

main()
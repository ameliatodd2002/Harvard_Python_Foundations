import random

def random_capital():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return random.choice(letters)

def random_plate():
    for i in range (20):
        ln = []
        ll = []
        ln.append(str(random.randint(1,9)))
        for j in range (2):
            num = str(random.randint(0,9))
            ln.append(num)
        a = ''.join(ln)
        for k in range (3):
            ll.append(random_capital())
        b = ''.join(ll)

        print(f'{a} {b}')

def main():
    random_plate()

if __name__ == "__main__":
    main()


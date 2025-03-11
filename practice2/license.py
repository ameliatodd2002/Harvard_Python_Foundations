import random

def random_capital():
    alph = letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return random.choice(alph)

def random_plate():
    plate = []
    for i in range(3):
        plate.append(random_capital())
    plate.append(' ')
    for j in range(3):
        if j == 0:
            plate.append(str(random.randint(1,9)))
        else:
            plate.append(str(random.randint(0,9)))
    license_plate = ''.join(plate)
    print(license_plate)

def main():
    for i in range(21):
        random_plate()

main()
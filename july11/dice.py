import random

def main():
    roll1 = 0
    roll2 = 1
    while roll1 != roll2:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print (f"Rolled a {roll1} and a {roll2}")

main()
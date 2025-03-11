import random

def do_roll():
    sum = 0
    while sum not in [4, 5, 6, 8, 9, 10]:
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        sum = (roll_1 + roll_2)
        print_roll(roll_1, roll_2)
    return (sum)

def print_roll(roll_1, roll_2):
    print(f'Computer rolls a {roll_1} and a {roll_2}, for a total of {roll_1 + roll_2}.')
    if (roll_1 + roll_2) in [4, 5, 6, 8, 9, 10]:
        print (f'{roll_1 + roll_2} is now the established POINT.')

def get_point():
    point = do_roll()
    return point

def play_from_point(point):
    new_sum = 0
    while new_sum not in [point, 7]:
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        print(f'Computer rolls a {roll_1} and a {roll_2}, for a total of {roll_1 + roll_2}.')
        new_sum = (roll_1 + roll_2)
    if new_sum == point:
        return True
    if new_sum == 7:
        return False

def main():
    if play_from_point(get_point()):
        print ("YOU WIN")
    else:
        print ("YOU LOSE")

main()

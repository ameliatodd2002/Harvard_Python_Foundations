import random

def drunk_walk():
    outcome = ''
    position = 6
    blocks_walked = 0
    while position != 1 and position != 11:
        rand = random.randint(0, 1)
        if rand == 0:
            position += 1
        elif rand == 1:
            position -= 1
        blocks_walked += 1

    if position == 1:
        outcome = "HOME"
    elif position == 11:
        outcome = "JAIL"

    return [blocks_walked, outcome]

def main():
    N = 11
    for i in range (N):
        print(f"Here we go again... time for a walk!\nWalked {drunk_walk()[0]} blocks, and\nLanded at {drunk_walk()[1]}")

main()
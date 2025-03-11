import random

def drunk_walk():
    block_num = 6
    blocks = 0
    while block_num not in [1, 11]:
        choice = random.randint(0, 1)
        if choice == 0:
            block_num += 1
        elif choice == 1:
            block_num -= 1
        blocks += 1
    if block_num == 11:
        x = 'JAIL'
        return [x, blocks]
    if block_num == 1:
        x = 'HOME'
        return [x, blocks]

def main():
    N = 5
    left = 0
    total_blocks = 0
    avg = 0
    while left < N:
        walkres = drunk_walk()
        x = walkres[0]
        blocks = walkres[1]
        print(f'Here we go again... time for a walk!\nWalked {blocks} blocks, and\nLanded at {x}')
        left += 1
        total_blocks += blocks
    print(f'Average # of blocks equals {total_blocks / N}')


if __name__ == "__main__":
    main()


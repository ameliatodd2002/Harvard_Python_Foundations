import random

def flip_until_n_heads_in_a_row(n):
    streak = 0
    total_flips = 0
    while streak < n:
        total_flips += 1
        flip = coin_flip()
        print(flip, end='')
        if (flip == 'H'):
            streak += 1
        else:
            streak = 0
    print (f"Done! It took {total_flips}")

def coin_flip():
    flip = (random.randint(0, 1))
    if flip:
        return 'H'
    else:
        return 'T'

flip_until_n_heads_in_a_row(3)
def contains(lower, upper, value):
    if lower <= value >= upper:
        return True
    else:
        return False

def main():
    contains(3,8,5)

main()
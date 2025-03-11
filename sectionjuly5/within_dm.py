def within():
    n = int(input("integer"))
    if not (n < 4 or n > 8):
        print ("in range")
    else:
        print ("out of range")

def main():
    within()

main()
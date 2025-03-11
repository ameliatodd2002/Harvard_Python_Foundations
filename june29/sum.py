def main():
    for i in range (100,1000):
        a = i//100
        b = (i//10)%10
        c = (i%10)
        if (a**3 + b**3 + c**3) == i:
            print (i)

main()

#second soultion:

alt():
    for h in range (1,10):
        for t in range (10):
            for u in range (10):

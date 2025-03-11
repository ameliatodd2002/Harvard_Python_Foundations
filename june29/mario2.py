n= int(input("How tall do you want the pyramid to be?"))

for i in range (1, n+1):
    print (" " * (n-i) + "#" * i)
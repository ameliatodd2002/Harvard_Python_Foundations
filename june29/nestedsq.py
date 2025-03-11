outer_length = int(input("How big do you want it?"))
distance = row - 1

if distance > outer_length - row :
    distance = outer_length - row;

if distance > column - 1 :
    distance = column - 1

if distance % 2 == 0 :
    print ("*", end="")
else:
    print (".", end+"")

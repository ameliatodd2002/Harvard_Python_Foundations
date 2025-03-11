a = int (input ("a = "))
b = int (input ("b = "))
c = int (input ("c = "))

discr = b**2 - (4 * a * c) < 0

if discri < 0:
    print ("The polynomial has no real roots!")
elif discr > 0:
    print ()
else:
    print ("Polynomial has ONE real root")
def donor():
    donation = float(input("Enter the amount of a contribution:"))
    if donation >= 10000.00:
        print("Benefactor")
    elif donation >= 1000.00:
        print ("Patron")
    elif donation >= 200.00:
        print("Supporter")
    elif donation >= 15.00:
        print ("friend")
    elif donation >= 0:
        print ("Cheapskate")
    else:
        print ("Error")

donor()
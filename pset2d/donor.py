donation = float(input("Enter the amount of a contribution:"))

def donor():
    if donation >= 10000:
        print ("Benefactor")
    elif donation >= 1000:
        print ("Patron")
    elif donation >= 200:
        print ("Supporter")
    elif donation >= 15:
        print ("Friend")
    elif donation > 0:
        print ("Cheapskate!")
    else:
        print ("Error. Input less than 0")

donor()
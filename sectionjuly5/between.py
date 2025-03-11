def between(lower, upper,value):
    if value >= lower and value <= upper:
        print ("true")
    else:
        print ("false")

def main():
    between()
    lower = int(input("number"))
    upper = int(input("number"))
    value = int(input("number"))

main()
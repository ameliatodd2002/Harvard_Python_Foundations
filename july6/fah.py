# PROBLEM: Use a function to simplify this duplicated
# (and buggy!) code

def fahrenheit(f):
    return (f - 32) * 5 / 9

def main():
    f1 = 77
    c1 = fahrenheit(f1)
    print (f'{f1} is {c1} n celcius')

    f2 = 95
    c2 = fahrenheit(f2)
    print (f'{f2} is {c2} n celcius')

if __name__ == "__main__":
    main()
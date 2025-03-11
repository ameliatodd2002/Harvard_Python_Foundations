def eligible_for_house(age, length_of_citizenship):
    return age >= 25 and length_of_citizenship >= 7

def eligible_for_senate(age, length_of_citizenship):
    return age >= 30 and length_of_citizenship >= 9

def main():
    age = int(input("How old are you?"))
    length_of_citizenship = int(input("How long have you been a citizen of the US?"))

    print (eligible_for_house(age, length_of_citizenship))
    print (eligible_for_senate(age, length_of_citizenship))


if __name__ == '__main__':
    main()
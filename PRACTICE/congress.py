def eligible_for_senate(age, length_of_citizenship):
    return age >= 30 and length_of_citizenship >= 9

def eligible_for_house(age, length_of_citizenship):
    return age >= 25 and length_of_citizenship >= 7

def main():
    age = int(input("age"))
    length_of_citizenship = int(input("length of citizenship"))
    print(eligible_for_senate(age, length_of_citizenship))
    print(eligible_for_house(age, length_of_citizenship))

main()
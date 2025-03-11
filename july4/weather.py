def weather (temp):
    if not (temp >= 70 or temp <= 85):
        print ("Terrible weather!")
    else:
        print ("Great weather!")

def main():
    weather(80)

main()
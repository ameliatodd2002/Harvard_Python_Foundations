def graduation(gpa, total_credit_count, honors_credit):
    if total_credit_count < 180 or gpa < 2.0:
        return "not graduating"
    elif total_credit_count >= 180 and gpa >= 2.0:
        if gpa < 3.6:
            return "graduating"
        elif honors_credit < 15:
            if 3.6 <= gpa < 3.8:
                return "cum laude"
            if gpa >= 3.8:
                return "magna cum laude"
        elif honors_credit >= 15:
            if 3.6 <= gpa < 3.8:
                return "magna cum laude"
            if gpa >= 3.8:
                return "summa cum laude"

def main():
    print(graduation(3.6, 180, 14))

main()
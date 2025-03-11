def weekly_pay(wage, hours):
    if hours <= 40:
        return (wage * hours)
    if hours > 40:
        return 40 * hours + (hours - 40) * wage * 1.5

def main():
    weekly_pay(15, 50)

main()
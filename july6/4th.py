def after_fourth(m,d):
    return (m > 7) or (m == 7 and d > 4)

def main():
    m = 7
    d = 3
    if (after_fourth(m,d)):
        print (f'{m}/{d} is after the fourth')
    else:
        print (f' {m}/{d} is not after the fourth')

main()
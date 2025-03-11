def print_longer(a, b):
    if len(a)>len(b):
        print (f' {a} is the longer list and its last element is {a[-1]}')
    if len(a)<len(b):
        print (f' {b} is the longer list and its last element is {b[-1]}')

def main():
    print_longer(['chocolate', 'vanilla'], [1, 5, 9, 7])

main()
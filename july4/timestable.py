def print_times_table(n):
    for i in range (1, n+1):
        for j in range (1, i+1):
            print (f' {j} times {i} is {j*i}')

def main():
    print_times_table (n=4)

main()

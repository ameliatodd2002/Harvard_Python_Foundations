def sum_of_digits(n):
    answer = 0
    while (n > 0):
        answer += n % 10
        n = n // 10
    return answer

def main():
    print(sum_of_digits(1234))

main()
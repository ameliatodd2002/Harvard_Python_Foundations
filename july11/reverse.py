def reverse(word):
    answer = ''
    for i in range (1, len(word)+ 1):
        answer += (word [-i])
    return answer

def main():
    print(reverse('evian'))
    print(reverse('stressed'))

main()
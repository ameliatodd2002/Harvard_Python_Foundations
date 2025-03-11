def devowel(ad):
    advertisement = []
    for i in range(len(ad)):
        if (ad[i - 1] == ' '):
            advertisement.append(ad[i])
        elif not is_vowel(ad[i]):
            advertisement.append(ad[i])
    return ''.join(advertisement)


def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return c in vowels

def main():
    print(devowel('Desirable unfurnished flat in quiet residential area'))


if __name__ == "__main__":
    main()
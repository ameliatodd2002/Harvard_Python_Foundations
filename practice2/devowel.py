def devowel(ad):
        
    new_ad = []

    for i in range(len(ad)):
        if ad[i] == " " and is_vowel(ad[i + 1]):
            new_ad.append(ad[i])
            new_ad.append(ad[i + 1])
        elif ad[i] == " ":
            new_ad.append(ad[i])
        elif not (is_vowel(ad[i])):
            new_ad.append(ad[i])
        
    final = "".join(new_ad)

    return final


def is_vowel(c):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return c in v


def main():
    print(devowel("Desirable unfurnished flat in quiet residential area"))


main()
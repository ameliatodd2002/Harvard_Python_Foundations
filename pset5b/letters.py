def missing_letters(words):
    missing = []
    new_word = (''.join(words)).upper()
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for x in alph:
        if x not in new_word:
            missing.append(x)
    return missing

def main():
    print(missing_letters(['Now', 'is', 'the', 'TIME']))

if __name__ == "__main__":
    main()
def alphabetical(words):

    alphabetical_list = []

    for i in words:
        alph_word = ''.join(sorted(i, key=str.lower))
        alphabetical_list.append(alph_word)
    
    return alphabetical_list

def main():
    print(alphabetical(['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']))

main()
def alphabetical(word_list):
    new_word_list = []
    for i in range (len(word_list)):
        word = word_list[i]
        aw = list(word)
        aw.sort(key = str.lower)
        new_word = ''.join(aw)
        new_word_list.append(new_word)
    return new_word_list

print(alphabetical(['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']))
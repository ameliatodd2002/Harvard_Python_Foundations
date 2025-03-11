# PROBLEM: Use list comprehension and the split method
# to compute the average word length in a string
# (don't worry about punctuation). Hint: also use sum.

def average_word_lengths(text):
    a = text.split()
    x = 0
    for i in range(len(a)):
        x += (len(a[i]))
    average = x / (len(a))
    return average

def main():
    print(average_word_lengths('The quick brown fox'))

if __name__ == "__main__":
    main()
from romeo_and_juliet_data import lines

"""Add your solution to the problem 'authorship' here."""

# make sure to import your data file here


def word_length_histogram(text_list):
    """Takes the a list of multiword lines and returns
    a dictionary where the keys are word lengths and the
    values are how many words there are of that length.
    Assume there is no punctuation to worry about.
    For example, the input:
        [ "Summer school", "is nearly over"]
    should return the dictionary
        { 6 : 3, 2 : 1, 4 : 1 }
    """
    word_counts = {}
    for line in text_list:
        words = line.split()
        for word in words:
            word = word.replace("'","")
            length = len(word)
            if length not in word_counts:
                word_counts[length] = 1
            elif length in word_counts:
                word_counts[length] += 1
    return word_counts



def main():
    # Add your solution to the problem that makes use of the above to
    # print out the word length frequency table described in the pset.
    histogram = word_length_histogram(lines)
    new_histogram = sorted(histogram.keys())
    total_words = sum(histogram.values())

    for i in new_histogram:
        proportion = (histogram[i]/total_words) * 100
        print(f"Proportion of {i}- letter words: {proportion:.2f}% ({histogram[i]} words)")



if __name__ == "__main__":
    main()

def print_stats(text):
    num_words = len(text.split())
    for v in 'aeiou':
        print (f"Number of {v}: {text.lower().count(v)}")
    print(f"Number of words: {num_words}")

print_stats('hello hi hi')
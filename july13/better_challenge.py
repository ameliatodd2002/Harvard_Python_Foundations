def foo(text):
    wordlist = sorted(text.split(), key = len)
    print (' '.join(wordlist).lower())

foo("This is python")
def foo(text):
    x = text.lower()
    w = x.split()
    y = sorted(w, key=len)
    print(' '.join(y))

foo("This is python")
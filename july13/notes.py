sorted(‘rat’)
       #a, r, t
Sorted (‘raT’)
        #T, a, r  - capital sort before lower
[1, 2, 3] + [1, 1, 1]
    #[1,2,3,1,1,1]
[1, 2, 3]
    #list
(1, 2, 3)
    #tuple
#Each character corresponds with a number (Unicode)
ord()
#tells you the unicode number is
chr()
#tells you the letter fir a unicode
chr(random.randint(ord(‘a’), ord(‘z’)))
#picks a random char
random.choice(‘aeio’)

price = [1,2,3]
max(price)
#prints 3
max('freeze')
#prints z
words = [ 'dog', 'apple', 'cat']
min(words)
#prints apple bc starts w a
sum(price)
#prints 6
words = ['apple', 'dog', 'home']
sorted(words, key=len)
#prints ['dog', 'home', 'apple'] bc it sorts it by length
letters = ['t', 'a', 'R']
sorted(letters)
#[['R', 'a', 't']]
sorted(letters, key=str.lower)
y = [2,1,2,1]
x = y
#this means they share the same data, not copy of y for x
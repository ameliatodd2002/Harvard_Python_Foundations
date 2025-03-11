#sets remove duplicates
#no order

x = {0, 5, 9, 5, 2, 3, 5}
if 5 in x:
    print(x)

#ways to make a set

a = {'dog', 'cat', 'hamster'}
print(a)
b = set('abracadabra')
print(b)
c = set()
c.add(2)
c.add(3)
c.add(2)
print(c)
d = {x + x for x in 'cat'}
print(d)


prices = [10.25, 7.50, 8.99]
print(prices[0])
prices[0] += 5
print(prices[0])
#directly editing list

a = [9,8,7]
b = a
b = [3,4,6]
print(b)
#b changes because you are reassigning it to a new list

x = [1,2,3]
y = x
y[0] = 0
print(x)
#they both change!

a = [1,7,14]
print(len(a))

#can't edit a string only list
w = 'dog'
w = w + 'hey'
print(w)
#you aren't editting string, you are reassigning it

x = [1, 2, 3, 4]
x.append(20)
print (x)
#not making a copy! editing the original list!

x = []
x.append(20)
print(x)

x = [1, 2, 3, 4]
print(x.pop())
#returns 4 and changes the list to [1, 2, 3] - it has a SIDE-EFFECT of changing the list
print(x)

#sorted does not change list and sorts smth
#sort does not return anything, just sorts the list itself

d = [1,3,4,6]
print(sorted(d))
e = [1,3,5,6]
e.sort()
print(e)

m = ['*', '/', '-', '*']
m.insert(2, '+')
print(m)

m.remove('*')
print(m)
#removes the first insance of it

c = ['a','p','p','l','e']
c.sort()
print(c)
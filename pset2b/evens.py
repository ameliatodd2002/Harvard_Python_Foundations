n = int(input("I will compute the sum of even integers from 2 through?"))
sum = 0

for i in range (2,n+1,2):
    sum += i

print ("The sum is", sum)
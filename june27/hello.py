print ("Hello, IDE!")

for i in range (2,6):
    print (i)

print (" ")

for i in range (1,11,3):
    print (i)
print (" ")

for i in range (4):
    print (i*3+1)

print (" ")

for i in range (1,6,-1):
    print (i)

print (" ")

la = input ("How many jingles do you want?")
print ("Fa", end=" ")
la = int (la)
for i in range (la):
    print ("la", end=" ")

print ("LA", end=" ")

print (" ")

base = int (input ("Base"))
height = int (input ("Height"))

print (.5*(base*height))

print (" ")

def main():
    answer = int(input ("Give me an integer:"))
    print ("The next integer is", answer+1)

main()
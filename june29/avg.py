n = int(input("How many days would you like to average?"))

print ("I will average up the price of a stock on", n, "consecutive days!")

sum = 0

for i in range (n):
    sum+= float(input("Type the stock price of day #" + str(i+1) + ":"))

avg = sum/n

print (avg)
def print_recipe ():
    n = int(input("How many batches do you want to make?"))
    #argument is the value of n
    #parameter is the abstract variable
    print ("Mix the following ingredients in a bowl:")
    print (4*n, "cups of flour")
    print (n, "cup butter")
    print (n, "cup sugar")
    print (2*n, "eggs")
    print (n, "bag chocolate chips")
    print ("Place on sheet and bake for about 10 minutes")

print_recipe()
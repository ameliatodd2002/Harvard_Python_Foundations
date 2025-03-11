for i in range (100,901,100):
    if i > 400 and i < 900:
        print ("...")
    else:
        print (f'{i:4d}  {i+((2*(i//100))-2):4d}  {i+(((2*(i//100))-2))*2:4d}  {i+(((2*(i//100))-2))*3:4d}  {i+(((2*(i//100))-2)*8):4d}')
    #d means it is displayed as an integer
    #number before d is the amount of spaces it should take up
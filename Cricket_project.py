import random
a=int(input("""
Do you want to play:- 
1. Yes
2. No
:-)"""))
uruns=0
uwickets=0
while True:
    if a==1:
        if uwickets<1:
            uinput = int(input("Enter your runs between 1 to 6:- "))
            cinput = random.randint(1,6)
            if uinput>6:
                print("You can not enter a number more than 6 It's a dot ball")
            elif (uinput!=cinput):
                uruns+=uinput
                print("User input:-", uinput,"Computer input:-", cinput,"\n")
            elif(uinput==cinput):
                uwickets += 1
                print("User input:-", uinput, "Computer input:-", cinput, "\n")
                print("Out")
        else:
            break
    else:
        break
print("User runs:-", uruns, "\n", "Userwickets:-", uwickets)
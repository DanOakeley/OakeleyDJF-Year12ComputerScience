#A program to do timestables
nNum = int(input("Please input an number between 1 and 10  " ))
#A program to do timestables
nNum = int(input("Please input an number between 1 and 10  " ))
if nNum != 99:
    while nNum < 1 or nNum > 10:
        nNum = int(input("Your number was not valid, Please enter a number between 1 and 10"))
    for counter in range(0, 13):
        print(nNum * counter)
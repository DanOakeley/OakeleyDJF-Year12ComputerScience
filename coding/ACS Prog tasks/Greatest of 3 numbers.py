#program to where 3 numbers are entered and the largest of the 3 are outputed.
#input all the numbers
nNum1 = int(input("Please enter your first number"))
nNum2 = int(input("Please enter your second number"))
nNum3 = int(input("Please enter your third number"))
if nNum1 > nNum2 and nNum1 > nNum3:
    print(nNum1)
if nNum2 > nNum1 and nNum2 > nNum3:
    print(nNum2)
if nNum3 > nNum1 and nNum3 > nNum2:
    print(nNum3)
if nNum1 == nNum2 and nNum1 > nNum3:
    print(nNum1)
if nNum1 == nNum3 and nNum1 > nNum2:
    print(nNum1)
if nNum2 == nNum3 and nNum2 > nNum1:
    print(nNum2)
if nNum1 == nNum2 and nNum1 == nNum3:
    print(nNum1)

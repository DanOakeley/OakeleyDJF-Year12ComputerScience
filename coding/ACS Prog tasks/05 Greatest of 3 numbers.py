#program that takes 3 numbers and outputs the largest number
nNum1 = int(input("Please input a number"))
nNum2 = int(input("Please input a number"))
nNum3 = int(input("Please input a number"))
#use if statements to work out which number is the greatest

if nNum1 > nNum2 and nNum1 > nNum3:
    greatest= nNum1
    if nNum2 > nNum3:
        middle = nNum2
        lowest = nNum3
    else:
        lowest = nNum2
        middle = nNum3
    #end if
    print(greatest, middle, lowest)
#end if
if nNum2 > nNum1 and nNum2 > nNum3:
    greatest= nNum2
    if nNum1 > nNum3:
        middle = nNum1
        lowest = nNum3
    else:
        lowest = nNum1
        middle = nNum3
    #end if
    print(greatest, middle, lowest)
#end if
if nNum3 > nNum2 and nNum3 > nNum1:
    greatest= nNum3
    if nNum1 > nNum2:
        middle = nNum1
        lowest = nNum2
    else:
        lowest = nNum1
        middle = nNum2
    #End if
    print(greatest, middle, lowest)
#end if
if nNum1 == nNum2 and nNum1 == nNum3:
    print(nNum1, nNum2, nNum3)
#end if


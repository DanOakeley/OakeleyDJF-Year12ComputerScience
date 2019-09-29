rows=[]
row1=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row2=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row3=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row4=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row5=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row6=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row7=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row8=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row9=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
row10=["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
rows.append(row1)
rows.append(row2)
rows.append(row3)
rows.append(row4)
rows.append(row5)
rows.append(row6)
rows.append(row7)
rows.append(row8)
rows.append(row9)
rows.append(row10)


sPlate = input("Please enter your number plate")
nRowChosen = int(input("Please enter the row in which you parked")) -1
nCollumnChosen = int(input("Please enter the collumn in which you parked")) -1
if rows[nRowChosen][nCollumnChosen] == "empty":
    rows[nRowChosen][nCollumnChosen] = sPlate
else:
    print("this space is taken!!!")
print(rows)

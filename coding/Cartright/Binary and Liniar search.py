import math
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2 = ['apple','banana','carrot','melon','rasin','strawberry','pair']
#functions
def BinarySearch(aList, itemSought):
	found = False
	index = -1
	first = 0
	last = len(aList)-1
	while first <= last and found == False:
		midpoint = int((first + last)/2)
		if aList[midpoint] == itemSought:
			found = True
			index = midpoint
		else:
			if aList[midpoint] < itemSought:
				first = midpoint + 1
			else:
				last = midpoint - 1
#			endif
#		endif
#	endwhile
	return index
#	endfunction

def LiniarSearch(alist, itemSought):
	found = False
	index = -1
	current = 0
	length = len(alist)
	while current < length and found== False:
		if current == itemSought:
			current = bindex
			found = True
		#endif
	#endwhile
	return index
#main code


#list = input("please pick the list you want to search; 'list1' or 'list2' ")
#if list == list1:
#	item = input(int("please input the item you are searching for"))
#if list == list2:
#	item = input(str("please input the item you are searching for"))
#else:
#	print("you didnt enter a valid list")
#endif
#itemindex = BinarySearch(list, item)
#print(itemindex)

lindex = LiniarSearch(list1, 4)
bindex = BinarySearch(list1, 4)
print(bindex)
print(lindex)

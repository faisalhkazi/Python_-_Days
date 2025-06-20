list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)

list3[0] = "Alpha"      #This is used to replace the words in the list

print(list3)

list3.append('g')       #THis is used to add more into the list

print(list3)

list3.pop()         #This deletes the last items

print(list3)

list3.pop(3)        #Using this we can delete the specific index

print(list3)

sorting_in_order = ['b', 'h', 'd', 'g', 'a', 'e', 'c', 'f']
print(f"This is the lisy which is not in order {sorting_in_order}")
sorting_in_order.sort()         #This is use to sort the list in correct order
print(f"This is the list converted in order {sorting_in_order}")

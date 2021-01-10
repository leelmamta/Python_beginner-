#in list we can have all types of data together 
# even we can have another list into the list 
# list is declared as [2 , 3, "stjd",True, 23.23]
l = [1,2,3]
print(l) # print list as it is 
print(len(l)) # number of elements in list can be calculated by len() function 
print(type(l)) # define type of l 
# we can work on list like strings 
print(l[0])  # access 0th element 
print(l[1:3]) # excluding index 3 
print(l[:3])  # begin with 0th index
# we can change element in the list by accessing list element and assigning value to it 
l[0]="rmya"
print(l)

# we can change particular range of elements 
l[1:3] = ["tyka","rina"]
print(l)
l.insert(2,"water") # inserting at particular position and moving particular position element one ahead 
print(l)
l.append("orange") # insert at the end of list 
print(l)
# to append another list use extend()
lis = ["mina","sina"]
l.extend(lis)
print(l)


##### removing list items 
# to remove specified item use remove()
l.remove("sina")
print(l)
# to remove particular position element use pop(position) if want to pop last element use pop()
l.pop()
print(l)
# del keyword is also used to delete particualr element or complete list
del l[0]
print(l)

# clear() make the list empty 
# sort() is used to arrange list in ascending and descending order
# copy() 
# + , append , extend are used to join two lists 





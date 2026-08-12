list=["friend","family","colleague", 20, 30, 40, 50, 2.43,4.5,True, False]
print(list)
print(list[2:8])
list.insert(3, "neighbor")
print(list)  #list is mutable and does not create a new list with the inserted value
list.remove("friend")
print("List after removing 'friend':", list)
print("Count of 'family' in the list:", list.count("family"))

a=[1,2,3,4,5,45,60,34,23,12,11]
b=["adit","jyoti","priya","shreya"]
b.append("sneha")



#tuple is immutable and does not allow any changes to its elements after creation
t=(1,)  #tuple with a single element must have a trailing comma
print(t)
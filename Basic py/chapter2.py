list=["friend","family","colleague", 20, 30, 40, 50, 2.43,4.5,True, False]
print(list)
print(list[2:8])
list.insert(3, "neighbor")
print(list)  #list is mutable and does not create a new list with the inserted value
list.remove("friend")
print("List after removing 'friend':", list)
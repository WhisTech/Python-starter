#list
list = [1, 2, 3, 4, 5]
print(list)
print(list[0]) #it gets the first element of the list
print(list[-1]) #it gets the last element of the list

print("-------------------")

#slice the list
marks=[65, 70, 75, 80, 85, 90, 95, 100]
print(marks[0:5]) #it gets the first 5 elements of the list
print(marks[-3:]) #it gets the last 3 elements of the list

print("-------------------")

print("Before adding elements to the list")
print(marks)
marks.append(105) #it adds an element to the end of the list
print(marks)
marks.insert(0, 60) #it adds an element to the beginning of the list
print(marks)

print("-------------------")

#tuple
tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 1,1,5)
print(tuple)

tuple.count(1) #it counts the number of occurrences of an element in the tuple
print(tuple.count(1))

tuple.index(3) #it gets the index of the first occurrence of an element in the tuple
print(tuple.index(3))


# set is unindexed there is no order in set and it is mutable and it is a collection of unique elements

set = {"adi",4,5,5,True,None, 5.5, (5,6,7), "aj"}   

print(f"set: {set}, type is: {type(set)} ")

print(len(set))

set.add("aditya")
print(set)

fs1=frozenset({'adi',3,4.5,"aj"}) # frozenset is immutable
print(fs1,type(fs1))


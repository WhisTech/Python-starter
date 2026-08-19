marks = {
    "adi": 100,
    "sujal": 60,
    "sagar": 70,
    "age1":20,
    "age2":22
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks["age2"]=30
print(marks.items())

print(marks["adi"])

print(marks.get("adii"))

marks["AJ"] = 99

aj={}
print(aj.items())

aj = {}
print(type(aj))
e = set()         ## empty set
print(type(e))

set = {1, 4, 5, 9, 93, 20, 43, "adi", "aj"}
print(set)

set.add("nova")
set.remove(5)
print(set)
set.pop()
print(f"Set after removing random element: ,{set}")

s1={1,3,4,5}
s2={1,5,9,6,8,0}

print(s1.intersection(s2))
print(s1.union(s2))

words ={
    "cat" : "manjar",
    "dog" : "kuttra",
    "ghost" : "bhoot"

    }

word = input("enter the word u want to know the meaning : ")

if(word in words):
    print(words[word])
else:
    print("We dont know the meaning of this")

s = set()
i = 1 
while(i != 8):
    num = int(input("enter your no : "))         # # we have to use for loop
    s.add(num)        
    i+=1

print(f"Your unique no of set :{s}")

d = {

}
for i in range(4):
    name = input("Enter your name : ")
       
    if not name.isalpha():
        print("Name should contain letters only.")
        continue

    fav = input("Enter your fav lang : ")

       
    if not fav.isalpha():
        print("Name should contain letters only.")
        continue

    d.update({name:fav})


d.items()
print(f"Your dic after adding all data : {d}")


n=[5,3,9,8,4,6,1,7,5,9,7,2,3]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)

# lang=["Python", "jave",'c','javascript']
# print("python" in lang)
# print("Python" in lang)

print(min(n))
print(f"Smallest no: {min(n)}")
print(f"Largest no: {max(n)}")

avg=sum(n)/len(n)
print(avg)    #average of list

print(round(avg,2))
print("--------------------------------")

#list inside list 

l1=[5, 10, 15, 20, 25,"aj","adi",[1,2,3,4,5],True,None]
print(f'Orignal list : {l1}')

print(f"Element at index -3: {l1[-3]}")

print(f"Element under the index -3 is: {l1[-3][1]}")


fruits = []

for i in range(7):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)
print(fruits)

print("--------------------------------")

marks =[]
for i in range(6):
    mark = input(f"Enter the marks of student {i+1}: ")
    marks.append(mark)

marks.sort()
print(marks)

print(sorted(marks))  #sorted() function returns a new sorted list without modifying the original list

print("--------------------------------")

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
sum = 0
for num in numbers:
    sum += num
print("Given list of numbers:", numbers)
print("Sum of numbers:", sum)

print("--------------------------------")

l=[5, 10, 15, 20, 25]
print(f"sum of list: {sum(l)}")

print("--------------------------------")


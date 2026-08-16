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


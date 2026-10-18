# print("Hello, World!", "Aditya")
# print("Jadhav")
# age=10

# #HOw to take input from user
# name = input("Enter your name: ")
# print("Hello",name)

# #type of variable
# print(type(name))
# print(type(age))

# #COncatenation of string
# first_name = "Aditya"
# last_name = "Jadhav"
# print("Full name by another way is", first_name + last_name)
# full_name = first_name + " " + last_name
# print("Full name is", full_name)

# #Practice EX 1

# name = "Tony Stark"
# age = 53    
# height = 6.1
# print("Hello", name)
# print("Tonys age is", age)
# print("Tonys height is", height)

# superhero_name = input("Enter your superhero name: ")
# print("Your superhero name is", superhero_name)
import math

a=float(input("enter first side: "))
b=float(input("enter 2nd side: "))
c=float(input("enter 3rd side: "))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))
a=math.sqrt(area)
print("Area of triangle is =", a)
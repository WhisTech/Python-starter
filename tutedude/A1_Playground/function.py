# Single value return from function
"""
def add(num1 , num2):
    result = num1+num2
    print(f"Addition of no is: {result}")

a = int(input('Enter no 1: '))
b = int(input('Enter no 2: '))

add(a,b)
"""

# Multi return value from function 
'''
def arethmatic(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    return add, sub, mul, div


no1 = int(input("Enterr your first no: "))
no2 = int(input("Enterr your second no: "))

r1, r2, r3, r4 = arethmatic(no1, no2)
print(f"addition of {no1} and {no2} is: {r1}")
print(f"subtraction of {no1} and {no2} is: {r2}")
print(f"multiplication of {no1} and {no2} is: {r3}")
print(f"division of {no1} and {no2} is: {r4}")
'''

'''
n= int(input("Enter no to find the factorial: "))
factorial = 1 
i =1
while i<=n:
    factorial= factorial*i
    i+=1

print(factorial)
'''   

# Palindrome no 
'''
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

num = input("Enter a number: ")
is_palindrome(num)
'''

# create a function where user enter his marks and it will get the percentage of it 
'''
def student_mark(sid, name, *marks):
    if len(marks)==0:
        print(f"{name} was abesent in all exam!!")
    else:
        result = sum(marks) / len(marks)
        print(f"{name} secured {result}% in his exam")


student_mark(101, "Adi", 50,46,99,68)
student_mark(102, "Sora", 78,89,88,99)
student_mark(103, "Aj")
'''

# take student info like there name ,id , hobby, and there marks 
# print there percentage and there hooby and there sub name 
'''
def student_details(sid, name, *hobby,**marks):
    if len(marks) == 0:
        print(f"{name} was absent for exam")
        print(f"{name} hobby's are: {hobby}")
    else:
        percentage = sum(marks.values())/len(marks)
        print(f"{name} got {percentage}% in his exam")
        print(f"{name} hobby's are: {hobby}")
        print(f"Subjects of {name} are: {marks.keys()}")

student_details(101,"Aditya", "Gaming", "coding", 'reading', maths =99,science=85, marathi=95, english = 65)
print()
student_details(102,"Martis", "networking", "dancing", 'slepping', maths =75,science=85, marathi=80, english = 65)
print()
student_details(103,"Sora", "conten creation", "swiming", 'cricket')
'''

# this is called Docstring we write this at the starting of function
# this tell us about the function and we can dwt it with the help function 
'''
def add(a,b):
    """
    a = is for num 1
    b = is for num 2
    we perform addition of this two no 
    return: int
    """
    r1=a+b
    return r1

help(add)
'''

# factorial of no using Recursion function
'''
def recursion(num):
    if num == 1:
        return 1
    else:
        fact = num * recursion(num-1)
        return fact

print(recursion(5))
'''


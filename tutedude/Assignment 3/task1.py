n= int(input("Enter no to find the factorial: "))
def factorial_no(a):
    factorial = 1 
    for i in range(1, a+1):
        factorial = factorial * i
    return factorial


print(factorial_no(n))

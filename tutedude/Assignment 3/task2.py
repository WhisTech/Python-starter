import math


def Calculations(n):
    square_root = math.sqrt(n)
    logerithum = math.log(n)
    sine = math.sin(n)
    return square_root, logerithum, sine


num = int(input("Enter a no: "))
r1, r2, r3 = Calculations(num)

print(f"Square root of {num} is: {r1}")
print(f"Logerithum of {num} is: {r2}")
print(f"Sine of {num} is: {r3}")

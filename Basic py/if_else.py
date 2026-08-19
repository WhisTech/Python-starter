# a , b, c, d = int(input("enter your no: "))

a, b, c, d = map(int, input("Enter 4 numbers: ").split())

if a > b and a > c and a > d:
    print("a is the greatest number:", a)

elif b > a and b > c and b > d:
    print("b is the greatest number:", b)

elif c > a and c > b and c > d:
    print("c is the greatest number:", c)

elif d > a and d > b and d > c:
    print("d is the greatest number:", d)
a = int(input("enter first no: "))
b = int(input("enter second no: "))
op = input("enter operator (+, -, *, /, **, %): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "**":
    print(a**b)
elif op == "%":
    print(a % b)
else:
    print("Invalid operator")

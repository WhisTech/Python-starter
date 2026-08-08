# conversion of data types
# Type casting
age = input("Enter your age: ")
new_age = int(age) + 5
print("Your age after 5 years will be", new_age)
print(float(age))
print(str(age))
print(bool(age))

name = "Peter Parker"
grade = "C"
# String Operations
print(name.upper())
print(name.lower())

# find
# It follows the 0 indexing rule
print(name.find("Parker"))

# replace
print(name.replace("Peter", "Spider"))
print(name.replace("Parker", "Man"))
print(name.replace("Peter", "Spider").replace("Parker", "Man"))

# practice exercises 2
price1 = float(input("Enter the price of first item: "))
price2 = float(input("Enter the price of second item: "))
price3 = float(input("Enter the price of third item: "))
total_price = price1 + price2 + price3
print("the total price is:", total_price)
average_price = total_price / 3
print("the average price is:", average_price)

superhero_name = input("Enter your superhero name: ")
if superhero_name.startswith(("S", "s")):
    print("true")
else:
    print("false")

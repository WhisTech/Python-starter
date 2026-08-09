# Range
num = range(10)
print(num)

# loops

count = 1
while count <= 5:
    print("AJ")
    count += 1

i = 1
while i <= 5:
    print(i * "*")
    i += 1

print("----------------------")

i = 5
while i >= 1:
    print(i * "*")
    i -= 1

print("----------------------")

# for loop

for i in range(5):
    print(i)

print("----------------------")

for i in range(1, 6):
    print(i)

print("----------------------")

# even number

for i in range(1,11):
    if i % 2 == 0:
        print(i)

#another way to print even no
for n in range(2,11,2):
    print(n)

print("----------------------")

# odd number
for i in range(21):
    if i % 2 != 0:
        print(i)

print("----------------------")

#tabel of 3 without 15
print("Table of 3 without 15")
for i in range(1,51):
    if i==15:
        continue
    if i%3==0:
        print(i)

print("----------------------")

#no that is divisibel by both input no
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))

for i in range(1,1000):
    if i%a==0 and i%b==0:
        print("The first no that is divisible by both", a, "and", b, "is:", i)
        break

print("----------------------")
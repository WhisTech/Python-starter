import random

print("Welcome to the die game!")
print()

while True:
    choice=input("Press 'Enter' to roll die or 'q' to quit: ")
    if choice == 'q':
        print("Thanks for playing!!!")
        break
    elif choice == "":
        no = random.randint(1,6)
        print(f"You rolled a {no}")
    else:
        print("Invalid input. Please try again.")

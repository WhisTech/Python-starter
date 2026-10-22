balence = 0


def check_balence():
    global balence
    print(f"Your Balence is: {balence}$")


def withdraw():
    global balence
    withdraw_amount = int(input("Enter amount to withdraw: "))

    if withdraw_amount > balence:
        print("Insuffecient Balence Try again")
    else:
        balence = balence - withdraw_amount
        print(f"{withdraw_amount}$ is withdraw successfully!!")


def deposit():
    global balence
    deposit_amount = int(input("Enter amount to Diposit: "))
    balence = balence + deposit_amount
    print(f"{deposit_amount}$ is deposited successfully!!!")


print("Wlc to AJ's Bank!!!")

while True:
    print("""
           1. Check Balence
           2. Withdraw
           3.Deposit
           4.Quit   
                     """)

    choise = input("Enter your choise (1-4): ")

    if choise == '1':
        check_balence()
    elif choise == '2':
        withdraw()
    elif choise == '3':
        deposit()
    elif choise == '4':
        break
    else:
        print("Invalid Choise!! PLese try again")

print("Thank You for using AJ's Banking!!!")

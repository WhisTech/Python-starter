balence = 0.0
kyc_document = {}

def check_balence():
    global balence
    print("========================")
    print(f"Your Balence is: {balence}$")
    print("========================")

def withdraw(amount):
    global balence
    

    if withdraw_amount > balence:
        print("========================")
        print("Insuffecient Balence Try again")
        print("========================")
    elif withdraw_amount == 0:
        print("========================")
        print("Cannot witdraw 0$")
        print("========================")
    else:
        balence = balence - withdraw_amount
        print("========================")
        print(f"{withdraw_amount}$ is withdraw successfully!!")
        print("========================")

def deposit(amount):
    global balence
    
    if deposit_amount <= 0:
        print("========================")
        print("Invalid amount")
        print("========================")
    else:
        balence = balence + deposit_amount
        print("========================")
        print(f"{deposit_amount}$ is deposited successfully!!!")
        print("========================")

def check_kyc():
    global kyc_document

    if len(kyc_document)==0:
        print("========================")
        print("kyc not done!!")
        print("========================")
    else:
        for doc in kyc_document:
           
            print(f"{doc} : {kyc_document[doc]}")
            

def kyc_update(docs):
    kyc_document.update(docs)

print("Wlc to AJ's Bank!!!")

while True:
    print("""
           1. Check Balence
           2. Withdraw
           3.Deposit
           4.Check KYC
           5.Update KYC
           6.Quit   
                     """)

    choise = input("Enter your choise (1-6): ")

    if choise == '1':
        check_balence()
    elif choise == '2':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        withdraw(withdraw_amount)
    elif choise == '3':
        deposit_amount = float(input("Enter amount to Diposit: "))
        deposit(deposit_amount)
    elif choise == '4':
        check_kyc()
    elif choise == '5':
        kyc_docs = {}
        n_docs = int(input("Enter the no of doc to update: "))
        for i in range(n_docs):
            key = input("Enter the name of documenet: ")
            value = input("Enter the ID of document: ")
            kyc_docs[key]=[value]
        kyc_update(kyc_docs)
        print("========================")
        print("kyc Updated!!!")
        print("========================")
    elif choise == '6':
        break
    else:
        print("Invalid Choise!! PLese try again")
print("========================")
print("Thank You for using AJ's Banking!!!")
print("========================")

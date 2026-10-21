import random

num = 1
attempt = 10
secret_no = random.randint(1,100)
win = False

print("Wlc to the no guessing game")
print("The no is betwn 1 to 100 u have 10 attempt to guess")


while num <= 10:
    print(f"You have {attempt} attempt left")
    user_guess = int(input("Enter your guess: "))

    if user_guess == secret_no:
        print("Congrats u gess the no!")
        win = True
        break
    else:
        if user_guess < secret_no:
            higher_or_lower = "Higher"
        else:
            higher_or_lower = "Lower"

        attempt-=1
        if attempt == 0:
            break
        else:
            print(f'U did not guess the no try {higher_or_lower}')
    
    num+=1
    

if not win:
    print(f" Bad luck!! Game over Sectert no was {secret_no}")

print("Game Over!!!")



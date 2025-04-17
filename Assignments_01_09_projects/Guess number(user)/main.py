import random
print("Guess the number between 1 to 10!")
number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number :
        print("To low number!")
    elif guess > number:
        print("To high number!")
    else:
        print("Congratulation you got it digit") 
        break 
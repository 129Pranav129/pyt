#guessing_game 
import random

print("Welcome to the guessing game !!")
print("Im thinking of a number between  1 and 100")
computer_choice = random.randint(1,100)
level = input("Do you want easy level or hard level : ")

if(level=='hard'):
    attempts=5
if(level=='easy'):
    attempts=10

while(attempts>0):
    print(f"You have {attempts} attempts remaining")
    guess= int(input("Make a guess : "))

    if(guess>computer_choice):
        print("Too high.")
        attempts-=1
    elif(guess<computer_choice):
        print("Too low.")
        attempts-=1
    elif(guess==computer_choice):
        print("Congratulations u won")   
        break       

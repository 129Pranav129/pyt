import random
import hangman_2


display = []
hangman =0
win=0

computer_word_choice = random.choice(hangman_2.mylist)

print(hangman_2.logo)
# print(computer_word_choice)
for i in computer_word_choice:
    display.append("_")

print(f"{' '.join(display)}")

while(hangman<5):
    guess = input("guess a letter : ").lower()

    if(guess in display):
        print("you have already chosen this choose gain pls ")

    k=0
    g=0
    for i in computer_word_choice:

        
        if(i == guess):
           display[k] = i

        else:
            g+=1
            

        if(g==len(computer_word_choice)):
            hangman+=1 
            print(hangman_2.hangman_ascii_art[hangman])
            print(f"Your guess {guess} is wrong, you have {5-hangman} lives remaining")


  
        k+=1

    # j=0
    # for i in display:
    #     if(i!='_'):
    #         j+=1
    # if(j==len(computer_word_choice)):
    #         win=1
    #         break

    if '_' not in display:
        win=1
        break


    print(f"{' '.join(display)}")

print(f"{' '.join(display)}")    
if(win==1):
    print("YOU WIN THE GAME")
else:
    print("YOU LOSE THE GAME")    

        
#rock 
#paper
#scissor


import random

yourchoice= print(input("Enter R for rock , S for scissor , P for paper \n"))
num= random.randint(0,2)

if(num==0):
    computer='R'
elif(num==1):
    computer='P'
else:
    computer='S'

print("Computer choice is " + computer)    

if(yourchoice=='R'):
    if(computer=='R'):
        print("Tie")
    elif(computer=='S'):
        print("you lose")
    else:        
        print("You win")
elif(yourchoice=='S'):
    if(computer=='S'):
        print("Tie")
    elif(computer=='R'):
        print("you lose")
    else:        
        print("You win")        
else:
    if(computer=='P'):
        print("Tie")
    elif(computer=='S'):
        print("you lose")
    else:        
        print("You win")        
   





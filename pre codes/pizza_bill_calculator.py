#Pizza bill calculator 

bill = 0
print("Welcome to pizaa mania !!")

print("Here is our pizza prize which pizza do u want")
print("Small  - 100" "\n" "Medium - 120" "\n" "Large  - 170")
size = input()

if(size=='S'):
    bill = 100
elif(size=='M'):
    bill = 120
else:
    bill = 170

print("do you want cheese burst")

cheese = input()

if(cheese == 'YES'):
    bill = bill+40

print("do you want cheese paneer")

paneer = input()

if(paneer == 'YES'):
    bill = bill+100


print(f"Your bill is {bill}")        
    

from cofee import MENU
from cofee import resources

def report(total_earnings):
    print("report:")
    water =resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"water : {water}")
    print(f"milk : {milk}")
    print(f"coffee : {coffee}")
    print(f"total earnings : {total_earnings}")
    return

def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    resources["water"]-=MENU[choice]["ingredients"]["water"]
    resources["milk"]-=MENU[choice]["ingredients"]["milk"]
    resources["coffee"]-=MENU[choice]["ingredients"]["coffee"]

    

total_earnings=0

while(1!=0):
    
    choice = input("What would you like : ")
    if(choice=='report'):
        report(total_earnings)
        choice = input("What would you like : ")

    if(MENU[choice]["ingredients"]["water"] <= resources["water"] and
    MENU[choice]["ingredients"]["milk"] <= resources["milk"] and
    MENU[choice]["ingredients"]["coffee"] <= resources["coffee"]):
        resources["water"]-=MENU[choice]["ingredients"]["water"]
        resources["milk"]-=MENU[choice]["ingredients"]["milk"]
        resources["coffee"]-=MENU[choice]["ingredients"]["coffee"]

    else:
        k= input("Resouces are over do u want to refill the resources y or n")
        if(k=='y'):
            refill()
        else:
            print("sry resorces are gone come tomorrow")    

    cost = MENU[choice]["cost"]
    total_earnings+=cost

    print(f"You have ordered a {choice} , your total is {cost}")
    money_inserted= int(input("Please insert coins"))
    change = money_inserted - cost

    if(change>0):
        print(f"here is you change of {change} ruppees")
        
    elif(change<0):
        print("Sorry thats not enough money pls try again ")
        continue

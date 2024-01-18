

choice="YES"
bidding_dict={}
max=0

while(choice == 'YES'):
    
    
    name=input("Whats you name sir/maam : ")
    bid=int(input("Enter the amount you want to bid : "))
    bidding_dict[name]=bid


    max=0
    for i in bidding_dict:
        if(bidding_dict[i]>max):
            ans=i
            max=bidding_dict[i]

    choice=input("Any more bidders")

print(f"{ans} you have won the bid")        


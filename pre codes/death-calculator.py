#death time calculator 
#Assuming you live upto 90

age = int(input("Enter your age"))

weeks_lived = age * 52
total_weeks = 90*52

weeks_left = total_weeks-weeks_lived

print(f"you have {weeks_left} weeks left assuming u live till 90")
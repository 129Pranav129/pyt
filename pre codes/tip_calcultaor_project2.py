#Tip calculator project 2

print("Welcome to Tip calculator")
total_bill = float(input("Enter the total bill please"))
no_of_people = int(input("Enter the no of people bw which the bill should be spilt"))

tip = float(input("Enter the percent of tip you would like to give --- 5%, 10%, 15%, 20%, or more"))

print(type (tip))
print(type(total_bill))
print(type(no_of_people))


total_tip = tip/100*total_bill
total_bill_plus_tip= total_bill + total_tip

spilt = total_bill_plus_tip/no_of_people

print("Each person has to pay " + str(spilt))
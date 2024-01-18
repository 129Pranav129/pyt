#making a calculator using functions and recursion

def start_again():
    choice = 'y'


    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b


    op={"+":add,
        "-":subtract,
        "*":multiply,
        "/":divide}


    num1 = int(input("Enter your first number"))


    while(choice=='y'):
        operation=input("Enter the operation you want to do +,-,*,%")
        num2= int(input("Enter your second number"))

        a=op[operation]
        output = a(num1,num2)
        print(output)

        choice1 = input("do you want to continue with same no, press 1 or make a fresh start, press 2")
        if(choice1=="1"):
            num1=output
        elif(choice1=="2"):
            start_again()



start_again()
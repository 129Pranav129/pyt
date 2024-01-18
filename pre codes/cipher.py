# variable = 'a'

# print(ord(variable))

# new_var = ord(variable) + 4

# print(chr(new_var))


######################################################



def encode(str_input,value):
    a=''
    k=0
    for i in str_input:
        k= ord(i) + value
        if(k>122):
            k=96 + value
            
        a=a+chr(k)
     
    print(chr(k)) 
    print(a)
    print(f"Encoded message is {a}")    


def decode(str_input,value):
    a=''
    k=0
    for i in str_input:
        k= ord(i) - value
        if(k<97):
            k=123-value
        a=a+chr(k)

    print(f"Encoded message is {a}")  


u="YES"

while(u == "YES"):
    u = input("Press YES to continue NO to end ")
    print("Welcome to the cipher area")

    str_input = input("Input you string : ").lower()
    value = int(input("Enter the encode/decode value : "))
    choice = input("Do u want to encode or decode : ")

    if(choice == 'encode'):
        encode(str_input,value)

    if(choice == 'decode'):
        decode(str_input,value)    
#password generator
import random

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', ]




num_alphabets = int(input("enter the no of alphabets u want not more than 30"))
num_numerals = int(input("enter the no of numerals u want not more than 9"))
num_special = int(input("enter the no of special charc u want"))


list_new = []
for i in range (0,num_alphabets):
    list_new.append(alphabet_list[random.randint(0,51)])

for i in range (0,num_numerals):
    list_new.append(numbers_list[random.randint(0,9)])

for i in range (0,num_special):
    list_new.append(special_characters_list[random.randint(0,11)])    

print(list_new) 

password = ''
for i in range(0,len(list_new)):
    num = random.randint(0,len(list_new)-1 )
    password = password + list_new[num]
    list_new.remove(list_new[num])
    
# the shuffling u did in line 33 to 35 can be simply done by a python function -->  random.shuffle(list_new) , which will 
# simply shuffle and reorder the contents of the list 

print(f"new password is {password}")    


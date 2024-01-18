#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:\\pyt\\day_24\\Mail_Start\\Input\\Letters\\starting_letter.txt") as file:
    read_letter = file.read()

with open("C:\\pyt\\day_24\\Mail_Start\\Input\\Names\\invited_names.txt") as file1:
    read_names = file1.readlines()



for i in read_names:
    strip=i.strip()
    with open(f"C:\\pyt\\day_24\\Mail_Start\\Output\\ReadyToSend\\{strip}.txt","w") as file2:
        with open("C:\\pyt\\day_24\\Mail_Start\\Input\\Letters\\starting_letter.txt") as file3:
            temp = file3.read()
            temp1 = temp.replace("[name]",strip)
            file2.write(temp1)           






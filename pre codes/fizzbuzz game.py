# #prit  no from 1 to 100 
# when no i divisible by 3 print fizz
# when no divisisble by 5 print buzz
# when no divisble by both print fizzbuzz


for i in range(1,101):
    if(i%3 == 0) and (i%5 == 0):
        print("fizzbuzz")
    elif(i%3 ==0) and (i%5 != 0):
        print("fizz")
    elif(i%3 !=0) and (i%5 == 0):
        print("buzz")
    else:
        print(i)    
                         
              
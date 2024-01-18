class Quiz:
    pass


def quizzing(ran_quest,ran_answer):
    score =0



    print("Your question is :")
    print(ran_quest)
    your_answer = input("Input your answer True or false : ")

    if(your_answer == ran_answer):
        print("Correct !!!!!")
        score+=1
    elif(your_answer != ran_answer):
        print("Wrong !!!")



    return score      


from question_model import Question
from data import question_data
import random
from quiz_brain import quizzing



question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))
 
k=0
for i in question_bank:
    ran_quest = i.quest
    ran_answer = i.ans

    score = quizzing(ran_quest,ran_answer)

    if(score == 1):
        k+=1

print(f"Your final score is {k}")  







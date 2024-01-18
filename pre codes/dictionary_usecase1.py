grade_name = {"Rohan":58,
              "Ravi":79,
              "Engina":91,
              "Fureero":20}

for i in grade_name:
    if(grade_name[i] >90 and grade_name[i]<101):
        grade_name[i]="Outstanding"
    elif(grade_name[i]>80 and grade_name[i]<91):
        grade_name[i]="Good"
    elif(grade_name[i]>70 and grade_name[i]<81):
        grade_name[i]="Average"
    elif(grade_name[i]>60 and grade_name[i]<71):
        grade_name[i]="Poor"
    elif(grade_name[i]<60):
        grade_name[i]="Very Bad"


print(grade_name)                        
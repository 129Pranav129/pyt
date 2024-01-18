from turtle import Turtle,Screen

myturtle = Turtle()
myscreen = Screen()

myturtle.speed(0)
def move_forward():
    myturtle.forward(20)

def move_backward():
    myturtle.back(20)

def move_left():
    myturtle.left(1)

def move_right():
    myturtle.right(1)    

def clear_screen():
    myturtle.clear()
    myturtle.penup()
    myturtle.goto(0,0)
    myturtle.pendown()    

myscreen.listen()

myscreen.onkey(move_forward,"w")
myscreen.onkey(move_backward,"s")
myscreen.onkeypress(move_left,"a")
myscreen.onkeypress(move_right,"d") 
myscreen.onkey(clear_screen,"space")
   



myscreen.exitonclick()
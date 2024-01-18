

from turtle import Turtle,Screen

myturtle = Turtle()
myscreen = Screen()


def move_forward():
    myturtle.forward(20)

myscreen.listen()
myscreen.onkey(move_forward,"space")




myscreen.exitonclick()
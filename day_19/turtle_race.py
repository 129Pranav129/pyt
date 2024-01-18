from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
screen.bgcolor("grey")
bet = screen.textinput("Make your bet","Select the color which will win ")

turtle_list = []
color = ["red","blue","green","orange","yellow"]
is_race_on = False

y=-100
for i in range(0,5):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color[i])
    turtle.penup()
    turtle.goto(-240,y)
    y=y+50
    turtle_list.append(turtle)


if(bet):
    is_race_on=True

while is_race_on:
    for turtle in turtle_list:
        if(turtle.xcor() > 230):
            is_race_on=False
            winner=turtle.pencolor()
            if(bet==winner):
                print("YOUR TURTLE WON THE RACE")
            else:
                print("YOUR TURTLE LOST THE RACE")    
        n=random.randint(0,10)
        turtle.forward(n)
           
screen.exitonclick()


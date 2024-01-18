from turtle import Turtle as t, Screen
import random
myturtle = t()

###make a square###
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(100)


###MAKE A DESHED KINE ####

# for i in range (0,10):
#     myturtle.forward(10)
#     myturtle.penup()
#     myturtle.forward(10)
#     myturtle.pendown()


### ALL SHAPES IN ONE ###

# n=3

# while(n<=100):
#     no_of_sides = 360/n

#     for i in range (0,n):
#         myturtle.forward(50)
#         myturtle.right(no_of_sides)

#     n+=1




#### RANDOM WALK OF SHAME ###


# mylist = [0,90,270,360]

turtle_colors = [
    "black", "white", "red", "green", "blue", "cyan", "magenta", "yellow",
    "orange", "purple", "brown", "pink", "gray", "lightblue", "darkgreen",
    "darkred", "gold", "violet", "indigo", "darkblue"
]


# for _ in range(0,1000):
#     myturtle.speed(0)
#     myturtle.pensize(10)
#     myturtle.color(random.choice(turtle_colors))
#     myturtle.forward(10)
#     myturtle.left(random.choice(mylist))
    





############## SPIROGRAPH   ####################

# for _ in range(0,100):
#     myturtle.color(random.choice(turtle_colors))
#     myturtle.speed(0)
#     myturtle.circle(100)
#     myturtle.left(5)



###### COLOUR GRAM SPOT PAINTING ########


myturtle.penup()
myturtle.goto(0,-200)
myturtle.pendown()
x=-710
y=-200
for i in range(0,100):
    for j in range(0,10):
        myturtle.speed(0)  
        myturtle.dot(10,random.choice(turtle_colors))
        myturtle.penup()
        myturtle.forward(20)
        myturtle.pendown()

    y=y+20
    
    myturtle.speed(0)
    myturtle.penup()
    myturtle.goto(0, y)  # Set the coordinates for the start of the next line
    myturtle.pendown()    





myscreen = Screen()
myscreen.exitonclick()

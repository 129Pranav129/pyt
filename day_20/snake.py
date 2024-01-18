from turtle import Turtle
from food import *

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)
            print(len(self.snake))


    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)    
        self.snake.append(new_segment)
        print(len(self.snake))

    def increase_snakesize(self):
        self.add_segment(self.snake[-1].position())

    #making the snake body move
    def move(self):    
        for i in range(len(self.snake) -1,0,-1):
            x=self.snake[i-1].xcor()
            y=self.snake[i-1].ycor()
            self.snake[i].goto(x,y)
        self.snake[0].forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_boundary(self):
            if(self.snake[0].xcor()==300):
                    self.snake[0].goto(-300,self.snake[0].ycor())
                    self.snake[0].forward(DIST)
                    # self.move()
   

            if(self.snake[0].xcor()==-300):
                    self.snake[0].goto(300,self.snake[0].ycor())
                    self.snake[0].forward(DIST)
                    # self.move()
 

            if(self.snake[0].ycor()==300):
                    self.snake[0].goto(self.snake[0].xcor(),-300)
                    self.snake[0].forward(DIST)
                    # self.move()
                                        

            if(self.snake[0].ycor()==-300):
                    self.snake[0].goto(self.snake[0].xcor(),300)
                    self.snake[0].forward(DIST)
                    # self.move()
 
 
    def check_itself_collision(self):
        k=0
        for i in self.snake[1:]:                       
            if(self.head.distance(i) < 10):
                k=1

        return k       
            





        
            

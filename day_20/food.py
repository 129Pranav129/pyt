#Food 

import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5,0.5,0.5)
        self.penup()
        numx=random.randint(-280,280)
        numy=random.randint(-280,280)
        self.goto(numx,numy)
       
    def refresh_food(self):
        numx=random.randint(-280,280)
        numy=random.randint(-280,280)
        self.goto(numx,numy)        



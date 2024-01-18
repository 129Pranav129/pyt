from turtle import Turtle,Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


myscreen = Screen()
myscreen.setup(600,600)
myscreen.bgcolor("black")
myscreen.title("Snake Game")
myscreen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

myscreen.listen()

myscreen.onkeypress(snake.up,"Up")
myscreen.onkeypress(snake.down,"Down") 
myscreen.onkeypress(snake.left,"Left")
myscreen.onkeypress(snake.right,"Right") 

game_is_on = True
k=0
while(game_is_on):
    myscreen.update()
    time.sleep(1)
    snake.check_boundary()
    snake.move()
    
    k = snake.check_itself_collision()
    if(k==1):
        game_is_on= False
        print("game is lost stopped ")


    #Detect collision with the food  
    
    if(snake.head.distance(food) < 15):
        food.refresh_food()
        k+=1
        snake.increase_snakesize()
        score.print_score()
        score.highscore_cal()

score.goto(0,0)        
score.write("GAME OVER !!", move=False, align="center", font=("Courier", 14, "normal"))

myscreen.exitonclick()
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.highscore=0
        self.scorecount=0
        self.color("white")
        self.penup()
        self.goto(-150,270)
        self.hideturtle()
        with open("C:\\pyt\\day_20\\score.txt") as file:
            self.highscore = int(file.read())
        self.write(f"Score : {self.scorecount}  HighScore : {self.highscore}", move=False, align="center", font=("Courier", 14, "normal"))

    def print_score(self):
        self.scorecount+=1
        self.clear()
        self.write(f"Score : {self.scorecount}  HighScore : {self.highscore}", move=False, align="center", font=("Courier", 14, "normal"))  

    def highscore_cal(self):
        if(self.scorecount > self.highscore):                        
            with open("C:\\pyt\\day_20\\score.txt", mode="w") as file:
                file.write(str(self.scorecount))
            print("outside checkkkkkkk")    


               
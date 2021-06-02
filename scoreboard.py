from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(50, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def left_score(self):
        self.lscore += 1
        self.update()

    def right_score(self):
        self.rscore += 1
        self.update()

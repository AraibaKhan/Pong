from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setpos(0, 0)
        self.x_mov = 10
        self.y_mov = 10
        self.move_speed = 0.07

    def move(self):
        self.penup()
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)


    def if_coll_wall(self):
        self.y_mov *= -1

    def if_coll_padle(self):
        self.x_mov *= -1
        self.move_speed *= 0.9

    def if_miss_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_mov *= -1


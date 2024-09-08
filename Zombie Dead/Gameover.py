from turtle import Turtle

class Gameover:
    def __init__(self):
        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(0, 0)
        self.text.color("white")
        self.text.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
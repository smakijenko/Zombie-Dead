from turtle import Turtle

class PlayerHealth:
    def __init__(self):
        self.healthBar = Turtle()
        self.healthBar.shape("img/playerHealth100.gif")
        self.healthBar.penup()
        self.healthBar.goto((-280, 255))

    def updateHealth(self, health):
        self.healthBar.shape(f"img/playerHealth{health}.gif")
        if health == 0: self.healthBar.hideturtle()
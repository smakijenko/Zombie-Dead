from turtle import Turtle
import random

class Player:
    speed = 7
    def __init__(self):
        self.player = Turtle()
        self.player.shape("img/playerSpriteUp.gif")
        self.player.penup()
        self.player.goto((0, 100))
        self.health = 100
        self.ticksBetweenDamage = 20

    def headingRight(self):
        self.player.setheading(0)
        self.player.shape("img/playerSpriteRight.gif")

    def headingUp(self):
        self.player.setheading(90)
        self.player.shape("img/playerSpriteUp.gif")

    def headingLeft(self):
        self.player.setheading(180)
        self.player.shape("img/playerSpriteLeft.gif")

    def headingDown(self):
        self.player.setheading(270)
        self.player.shape("img/playerSpriteDown.gif")

    def move(self, screen):
        self.ticksBetweenDamage += 1
        width = screen.screensize()[0] - 25
        height = screen.screensize()[1] - 25
        posX = self.player.xcor()
        posY = self.player.ycor()
        if posX <= width and posX >= -width and posY <= height and posY >= -height:
            self.player.forward(self.speed)
        else:
            if posX >= width:
                self.player.setx(width - 10)
            elif posX <= -width:
                self.player.setx(-width + 10)
            elif posY >= height:
                self.player.sety(height - 10)
            elif posY <= -height:
                self.player.sety(-height + 10)
        
    def playerPos(self):
        return self.player.pos()
    
    def damageByZombie(self, zombiePos):
        if self.ticksBetweenDamage > 20 and self.health > 0:
            if self.player.distance(zombiePos) < 20:
                self.health -= 25
                self.ticksBetweenDamage = 0
                x = self.player.xcor()
                y = self.player.ycor()
                randomPushX = random.choice([-25, -20, -15, 15, 20, 25])
                randomPushY = random.choice([-25, -20, -15, 15, 20, 25])
                self.player.goto(x + randomPushX, y + randomPushY)


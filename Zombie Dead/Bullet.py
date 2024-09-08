from turtle import Turtle
import math

class Bullet:
    def __init__(self, playerPos, clickX, clickY):
        self.bullet = self.createBullet(playerPos, (clickX, clickY))

    def createBullet(self, startPos, clickPoint):
        b = Turtle("circle")
        b.penup()
        b.color("black")
        b.shapesize(0.22)
        b.goto(startPos)
        degrees = b.towards(clickPoint)
        b.setheading(degrees)
        return b
    
    def move(self):
        self.bullet.forward(15)

    def outOfBounds(self, screen):
        width = screen.screensize()[0]
        height = screen.screensize()[1]
        if self.bullet.xcor() >= width: return True
        elif self.bullet.ycor() >= height: return True
        elif self.bullet.xcor() <= -width: return True
        elif self.bullet.ycor() <= -height: return True
        return False
    
    def bulletPos(self):
        return (self.bullet.xcor(), self.bullet.ycor())
    
    def deleteBullet(self):
        self.bullet.hideturtle()
        self.bullet.clear()


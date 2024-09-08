from turtle import Turtle
import random
from playsound import playsound

class Zombie:
    def __init__(self, speed):
        zombiePos = random.choice(self.generateRandomPos())
        self.zombie = Turtle()
        self.healthBar = Turtle()
        self.health = 100
        self.speed = speed
        self.healthBar.penup()
        self.healthBar.goto(zombiePos)
        self.healthBar.shape(f"img/zombieHealth{self.health}.gif")
        self.zombie.penup()
        self.zombie.goto(zombiePos)
        self.zombie.shape("img/zombieSprite0.gif")

    def generateRandomPos(self):
        y = random.randint(70, 120)
        x1 = random.randint(20, 80)
        x2 = random.randint(20, 80)
        return [(-425, y), (x1, -325), (x2, 325)]
    def setHeading(self, degrees):
        if 0 <= degrees < 20:
            self.zombie.shape("img/zombieSprite0.gif")
        elif 20 <= degrees < 70:
            self.zombie.shape("img/zombieSprite45.gif")
        elif 70 <= degrees < 110:
            self.zombie.shape("img/zombieSprite90.gif")
        elif 110 <= degrees < 160:
            self.zombie.shape("img/zombieSprite135.gif")
        elif 160 <= degrees < 200:
            self.zombie.shape("img/zombieSprite180.gif")
        elif 200 <= degrees < 250:
            self.zombie.shape("img/zombieSprite225.gif")
        elif 250 <= degrees < 290:
            self.zombie.shape("img/zombieSprite270.gif")
        elif 290 <= degrees <= 360:
            self.zombie.shape("img/zombieSprite315.gif")

    def updateHealtBar(self):
        self.healthBar.shape(f"img/zombieHealth{self.health}.gif")

    def move(self, playerPos):
        deg = self.zombie.towards(playerPos)
        self.zombie.setheading(deg)
        self.setHeading(deg)
        self.zombie.forward(self.speed)
        self.healthBar.setheading(deg)
        self.healthBar.forward(self.speed)

    def hitByBullet(self, bulletPos):
        distance = self.zombie.distance(bulletPos)
        if self.health > 0:
            if distance < 15:
                # playsound()
                self.health -= 20
                self.updateHealtBar()
                return True
        return False
    
    def unableToLayer(self, zombiePos):
        if self.zombie.distance(zombiePos) < 20:
            x = self.zombie.xcor()
            y = self.zombie.ycor()
            randomPushX = random.choice([-25, -20, -15, 15, 20, 25])
            randomPushY = random.choice([-25, -20, -15, 15, 20, 25])
            self.zombie.goto(x + randomPushX, y + randomPushY)
            self.healthBar.goto(self.zombie.pos())

    def zombiePos(self):
        return self.zombie.pos()
    
    def deleteZombie(self):
        self.zombie.hideturtle()
        self.healthBar.hideturtle()
        self.zombie.clear()
        self.healthBar.clear()

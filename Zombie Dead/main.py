from turtle import Screen
from Player import Player
from Bullet import Bullet
from Zombie import Zombie
from PlayerHealth import PlayerHealth
from Gameover import Gameover
import random

#Screen properties
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Zombie Dead")
screen.bgpic("img/backgroundSprite.png")
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)
#Player sprites
screen.register_shape("img/playerSpriteLeft.gif")
screen.register_shape("img/playerSpriteUp.gif")
screen.register_shape("img/playerSpriteRight.gif")
screen.register_shape("img/playerSpriteDown.gif")
#Zombies sprites
screen.register_shape("img/zombieSprite0.gif")
screen.register_shape("img/zombieSprite45.gif")
screen.register_shape("img/zombieSprite90.gif")
screen.register_shape("img/zombieSprite135.gif")
screen.register_shape("img/zombieSprite180.gif")
screen.register_shape("img/zombieSprite225.gif")
screen.register_shape("img/zombieSprite270.gif")
screen.register_shape("img/zombieSprite315.gif")
#Zombies health
screen.register_shape("img/zombieHealth100.gif")
screen.register_shape("img/zombieHealth80.gif")
screen.register_shape("img/zombieHealth60.gif")
screen.register_shape("img/zombieHealth40.gif")
screen.register_shape("img/zombieHealth20.gif")
screen.register_shape("img/zombieHealth0.gif")
#Players health
screen.register_shape("img/playerHealth100.gif")
screen.register_shape("img/playerHealth75.gif")
screen.register_shape("img/playerHealth50.gif")
screen.register_shape("img/playerHealth25.gif")
screen.register_shape("img/playerHealth0.gif")

#Variables
gameOn = True
moveRight = False
moveUp = False
moveLeft = False
moveDown = False
ticks = 50

#Objects
player = Player()
bulletsList = []
bulletsToDelete = []
def createBullet(clickX, clickY):
    global ticks
    if ticks > 5:
        ticks = 0
        bullet = Bullet(player.playerPos(), clickX, clickY)
        bulletsList.append(bullet)
        return bullet

zombieSpeed = 1
levelOfZombies = 0
zombieList = []
zombiesToDelete = []
def spawningZombies():
    global levelOfZombies, zombieSpeed
    if len(zombieList) == 0:
        zombieSpeed += 0.5
        levelOfZombies += 1
        for i in range(levelOfZombies):
            zombie = Zombie(zombieSpeed)
            zombieList.append(zombie)

healthBar = PlayerHealth()

#Key press handlers
def pressRight():
    global moveRight
    moveRight = True

def releaseRight():
    global moveRight
    moveRight = False

def pressUp():
    global moveUp
    moveUp = True

def releaseUp():
    global moveUp
    moveUp = False

def pressLeft():
    global moveLeft
    moveLeft = True

def releaseLeft():
    global moveLeft
    moveLeft = False

def pressDown():
    global moveDown
    moveDown = True

def releaseDown():
    global moveDown
    moveDown = False

#Key bindings
    #Moving
screen.onkeypress(pressRight, "d")
screen.onkeyrelease(releaseRight, "d")
screen.onkeypress(pressUp, "w")
screen.onkeyrelease(releaseUp, "w")
screen.onkeypress(pressLeft, "a")
screen.onkeyrelease(releaseLeft, "a")
screen.onkeypress(pressDown, "s")
screen.onkeyrelease(releaseDown, "s")

    #Shooting
screen.onscreenclick(createBullet)
screen.listen()

#Game loop
while gameOn:
    #Counting ticks between shots
    ticks += 1

    #Player movement handling
    if moveRight or moveUp or moveLeft or moveDown:
        if moveRight:
            player.headingRight()
        elif moveUp:
            player.headingUp()
        elif moveLeft:
            player.headingLeft()
        elif moveDown:
            player.headingDown()
        player.move(screen)
        
    #Zombie actions handling
    spawningZombies()
    for z in zombieList:
        z.move(player.playerPos())
        player.damageByZombie(z.zombiePos())
        healthBar.updateHealth(player.health)
        if player.health == 0: gameOn = False
        for zombie in zombieList:
            if z != zombie:
                zombie.unableToLayer(z.zombiePos())
    #Removing zombies
        for b in bulletsList:
            if z.hitByBullet(b.bulletPos()):
                if z.health <= 0:
                    zombiesToDelete.append(z)
    for z in zombiesToDelete:
        if z in zombieList:
            zombieList.remove(z)
            z.deleteZombie()

    #Bullet actions handling
    for b in bulletsList:
        b.move()
    #Removing bullets
        if b.outOfBounds(screen):
            bulletsToDelete.append(b)
    for b in bulletsToDelete:
        if b in bulletsList:
            bulletsList.remove(b)
            b.deleteBullet()
    #Cleaning "trash"
    zombiesToDelete.clear()
    bulletsToDelete.clear()

    screen.update()

#Gameover handling
    if not gameOn:
        text = Gameover()

#Keeping window open
screen.exitonclick()

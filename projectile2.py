import pygame
import math

class Projectile (object):
    x               = 0
    y               = 0
    sprite          = None
    speed           = 0
    angle           = 0.0  # 0 -> completely right, pi/2 -> completely down, pi -> completely left
    damage          = 0
    
    # initialization
    def __init__(self, xval, yval, spd, ang, damg, filepath):
        self.x        = xval
        self.y        = yval
        self.speed    = spd
        self.angle    = ang
        self.damage   = damg
        self.filepath = filepath
        self.setSprite(filepath)
    
    def getx(self):
        return self.x
        
    def gety(self):
        return self.y

    def getSprite(self):
        return self.sprite
        
    def getDamage(self):
        return self.damage
        
    def getFilepath(self):
        return self.filepath
        
    def getSpeed(self):
        return self.speed
        
    def getAngle(self):
        return self.angle
        
    def setx(self, xval):
        self.x = xval
        
    def sety(self, yval):
        self.y = yval
        
    def setSprite(self, filepath):
        self.sprite = pygame.image.load(filepath)
        
    def setSpeed(self, spd):
        self.speed = spd
        
    def setAngle(self, ang):
        self.angle = ang
        
    def draw(self, context):
        xstr = str(self.x)
        ystr = str(self.y)
        print(xstr + "," + ystr)
        #context.blit(self.sprite, [int(math.floor(self.x)), int(math.floor(self.y))])
        context.blit(self.sprite, [80, 80])
        
    # takes an x and y value and returns the updated coordinates based on on speed and angle
    def movementPattern(self, x, y):
        deltax = math.cos(self.angle) * self.speed
        deltay = math.sin(self.angle) * self.speed
        #newx   = int(math.floor(x + deltax)) # first floors the result and then converts to Int
        #newy   = int(math.floor(y + deltay))
        newx   = x + deltax
        newy   = y + deltay
        return (newx, newy)                  # returns (x,y)
        
    def setNextLocation(self):
        newCoord = self.movementPattern(self.x,self.y) # Gets coordinates for next frame
        self.x   = newCoord[0]                         # sets x
        self.y   = newCoord[1]                         # sets y
        return newCoord                                # returns (x,y)
        


# ai.py
# 
# controls movement of enemies

import random, math

class ai:
    def __init__(self):
        self.flyInSpeed = 10

    # ship will fly in from this point to StartPos
    def getOffscreenOrigin(self, context_size):
        return [random.randint(0,context_size[0]), -50]

    def getStartPos(self, context_size):
        return [random.randint(0,context_size[0]),random.randint(0,context_size[1]/2)]

    def getNextPos(self, pos):
        return pos

class circling_ai(ai):
    """ radius: the radius of orbit; speed: speed of rotation (rad/frame)"""
    def __init__(self, radius = 50, speed = .1):
        ai.__init__(self)
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def getStartPos(self, context_size):
        r = self.radius
        self.center = [random.randint(r,context_size[0] - r),random.randint(r ,context_size[1]/2) - r]
        return [self.center[0] + r, self.center[1]]

    def getNextPos(self, pos):
        r = self.radius
        self.angle += self.speed
        return [self.center[0] + r * math.cos(self.angle), self.center[1] + r * math.sin(self.angle)]
        
class sin_ai(ai):
    # moves left to right in a sine pattern.
    def __init__(self, amplitude = None, speed = None):
        ai.__init__(self)
        self.amplitude = amplitude
        self.speed     = speed
        self.angle     = 0
        
    # make sure ai doesn't spawn along the x axis closer than the amplitude of the ai
    def getStartPos(self, context_size):
        if self.amplitude == None:
            self.amplitude = random.randint(25,context_size[0]/2 - 50)
        if self.speed == None:
            self.speed = 10.0 / self.amplitude
        print(str(self.speed) + "," + str(self.amplitude))
        randx = random.randint(self.amplitude, context_size[0] - self.amplitude)
        self.center = [randx, random.randint(0, context_size[1]/2)]
        return self.center
        
    def getNextPos(self, pos):
        self.angle += self.speed
        return [math.sin(self.angle) * self.amplitude + self.center[0], self.center[1]]
        



# a list of ai constructors along with parameters - when generating a new enemy, choose randomly from among these 
aiList = [(ai,[]),(circling_ai,[]),(circling_ai,[50,-.1]),(sin_ai,[])]
#aiList = [(sin_ai,[])] # testing

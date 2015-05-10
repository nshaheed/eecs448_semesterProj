
# ai.py
# 
# controls movement of enemies

import random, math

class ai:
    def __init__(self):
        pass

    def getStartPos(self, context_size):
        return [random.randint(0,context_size[0]),random.randint(0,context_size[1]/2)]

    def getNextPos(self, pos):
        return pos

class circling_ai(ai):
    """ radius: the radius of orbit; speed: speed of rotation (rad/frame)"""
    def __init__(self, radius = 50, speed = .1):
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
    def __init__(self, amplitude = 50, speed = 0.1):
        self.amplitude = amplitude
        



# a list of ai constructors along with parameters - when generating a new enemy, choose randomly from among these 
aiList = [(ai,[]),(circling_ai,[]),(circling_ai,[50,-.1])]


# ai.py
# 
# 
import random, math

class ai:
    def __init__(self):
        pass

    def getStartPos(self, context_size):
        return (randint(0,context_size[0]),randint(0,context_size[1]/2))

    def getNextPos(self, x, y):
        return (x, y)


class circling_ai(ai):
    """ radius: the radius of orbit; speed: speed of rotation (rad/frame)"""
    def __init__(self, radius = 50, speed = .1):
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def getStartPos(self, context_size):
        r = self.radius
        self.center = (randint(r,context_size[0] - r),randint(r ,context_size[1]/2) - r)
        return (self.center[0] + r, self.center[1])

    def getNextPos(self, x, y):
        r = self.radius
        self.angle += self.speed
        return (self.center[0] + r * math.cos(self.angle), self.center[1] + r * math.sin(self.angle))
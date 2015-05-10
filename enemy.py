import ship, math

class enemy_object (ship.ship_object):
    def __init__(self,art,context_size, context,ai,weapon,proj,mvmt_ptrn):
        self.weapon       = weapon([0,0],proj,mvmt_ptrn,context,context_size)
        ship.ship_object.__init__(self,art,context_size, context, self.weapon)
        self.ai = ai
        self.inPosition = False
        self.patternStartPos = self.ai.getStartPos(context_size)
        self.pos = self.ai.getOffscreenOrigin(context_size)

    def update(self):
        #ship.ship_object.update(self)
        if self.inPosition:
            self.pos = self.ai.getNextPos(self.pos)
        else:
            dist = euclideanDist(self.pos, self.patternStartPos)
            if dist < self.ai.flyInSpeed:
                self.pos = self.patternStartPos
                self.inPosition = True
            else:
                distRatio = self.ai.flyInSpeed / dist
                x = self.pos[0] + distRatio * (self.patternStartPos[0] - self.pos[0])
                y = self.pos[1] + distRatio * (self.patternStartPos[1] - self.pos[1])
                self.pos = [x,y]


def euclideanDist(v1, v2):
    #print("eudlidean distance: ", v1, v2)
    return math.sqrt(sum([(v1[i] - v2[i]) ** 2 for i in range(len(v1))]))

import ship
class enemy_object (ship.ship_object):
    def __init__(self,art,context_size, context, ai,weapon,proj,mvmt_ptrn):
        self.weapon       = weapon([0,0],proj,mvmt_ptrn,context,context_size) # TODO: add proper initialization parameters
        ship.ship_object.__init__(self,art,context_size, context, self.weapon)
        self.ai = ai
        self.pos = self.ai.getStartPos(context_size)

    def update(self):
        ship.ship_object.update(self)
        self.pos = self.ai.getNextPos(self.pos)
        
                

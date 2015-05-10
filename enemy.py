import ship
class enemy_object (ship.ship_object):
    def __init__(self,art,context_size, context, ai,weapon):
        ship.ship_object.__init__(self,art,context_size, context, weapon)
        self.ai = ai
        self.pos = self.ai.getStartPos(context_size)

    def update(self):
        self.pos = self.ai.getNextPos(self.pos)
        
                

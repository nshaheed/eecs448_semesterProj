import ship
class enemy_object (ship.ship_object):
    def __init__(self,art,context_size,ai,weapon):
        ship.ship_object.__init__(self,art,context_size,weapon)
        self.ai = ai
        self.x, self.y = self.ai.getStartPos(context_size)

    def update():
        self.x, self.y = self.ai.getNextPos(self.x, self.y)
        
                

from   copy import deepcopy
import projectile2

# make cleanup function

class weapon(object):
    def __init__(self,coord,projType,movementPattern,context,context_size):
        self.proj            = []
        self.pos             = coord
        self.projType        = projType
        self.movementPattern = movementPattern
        self.counter         = 0 # increment this every frame, use mod to get the rate of fire
        self.context         = context
        self.context_size    = context_size
        
#    def __init__(self, xval, yval, spd, ang, damg, filepath):
    def newProj(self):
        xval     = self.projType.getx()
        yval     = self.projType.gety()
        spd      = self.projType.getSpeed()
        ang      = self.projType.getAngle()
        dmg      = self.projType.getDamage()
        filepath = self.projType.getFilepath()
        projNew  = projectile2.Projectile(xval,yval,spd,ang,dmg,filepath)
        return projNew
        
    def get_pos(self):
        return self.pos

    def get_x_pos(self):
        return self.pos[0]

    def get_y_pos(self):
        return self.pos[1]
        
    def get_proj(self):
        return self.proj
        
    def set_pos(self,pos): #pos must be a list [x_pos, y_pos]
        self.pos = pos

    def set_x_pos(self,x):
        self.pos[0] = x
        
    def set_y_pos(self,y):
        self.pos[0] = y
        
    def set_projType(self, projType):
        self.projType = projType
        
    # first updateProj updates the weapons x,y location,
    #    then it checks if it is time to add another projectile,
    #    if so, it appends it to the proj array
    #    then it cycles through all the projectiles, calls setNextLocation,
    #    and then if the projectile is off screen, removes it,
    #       else, it draw it.
    #    for enemies, the projectile will have a positive speed, and for
    #    the player will have a negative speed (assuming (0,0) is the 
    #    top left corner
    # updateProj(Int,Int)      :: Void 
    
    def updateProj(self,x,y):
        self.pos  = (x,y)
        angle     = self.movementPattern(self.counter)
        removeIdx = []
        
        if angle != None: # movementPattern returned a valid number, this means that it is time to generate a new projectile
            print(len(self.proj))
            newProjectile = self.newProj()
            newProjectile.setAngle(angle)
            self.proj.append(newProjectile)
            print(len(self.proj))
            print("")
            
        # run through all the projectiles, updating them on the screen.  If the projectiles are off the screen, 
        #   remove them from the list
        # note: use store a list of indexes to remove, use del on all those vals
        for i in range(0, len(self.proj) - 1):
            self.proj[i].draw(self.context) # draw to screen
            self.proj[i].setNextLocation()
            
            # finds index of projectiles that are off screen and need to be removed
            if self.proj[i].getx() < -64 or self.proj[i].getx() >= self.context_size[0] + 64:
                removeIdx.append(i)
            if self.proj[i].gety() < -64 or self.proj[i].gety() >= self.context_size[0] + 64:
                removeIdx.append(i)
                
        # removes projectiles 
        for j in range(0, len(removeIdx) - 1):
            del self.proj[j]
        
        
                
        self.counter = self.counter + 1
            
        
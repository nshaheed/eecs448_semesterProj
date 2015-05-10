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
    def newProj(self,x,y):
        spd      = self.projType.getSpeed()
        ang      = self.projType.getAngle()
        dmg      = self.projType.getDamage()
        filepath = self.projType.getFilepath()
        projNew  = projectile2.Projectile(x,y,spd,ang,dmg,filepath)
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
        
    # draws all projectiles
    def draw(self):
        for i in range(len(self.proj)):
            self.proj[i].draw(self.context) # draw to screen
            print("     proj" + str(i) + ": " + str(self.proj[i].getx()) + "," + str(self.proj[i].gety()))
    
    def updateProj(self,x,y,genNew):
        self.pos  = (x,y) # update position
        removeIdx = []
        angle     = self.movementPattern(self.counter)
        
        print("weapon pos:   " + str(self.pos))
        if genNew:
            if angle != None: # movementPattern returned a valid number, this means that it is time to generate a new projectile
                print("new proj coord: " + str(self.pos))
                print("-----------------------")
                newProjectile = self.newProj(x,y)
                newProjectile.setAngle(angle)
                self.proj.append(newProjectile)

        # run through all the projectiles, updating them on the screen.  If the projectiles are off the screen, 
        #   remove them from the list
        # note: use store a list of indexes to remove, use del on all those vals
        for i in range(len(self.proj)):
            # print("pos" + str(i) + "      (" + str(self.proj[i].getx()) + "," + str(self.proj[i].gety()) + ")")
            # self.proj[i].draw(self.context) # draw to screen
            self.proj[i].setNextLocation()
            
            if i == 0:
                print("zero")
                
            # finds index of projectiles that are off screen and need to be removed
            if self.proj[i].getx() < -64 or self.proj[i].getx() >= self.context_size[0] + 64:
                if i == 0: 
                    print("zeroxclear")
                removeIdx.append(i)
            if self.proj[i].gety() < -64 or self.proj[i].gety() >= self.context_size[0] + 64:
                if i == 0: 
                    print("zeroyclear")
                removeIdx.append(i)
                
        # removes projectiles that are off screen 
        for j in range(len(removeIdx)):
            print("removeIdx:  " + str(removeIdx))
            del self.proj[removeIdx[j]]
            
        self.counter = self.counter + 1
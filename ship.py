class ship_object (object):
#     def __init__(self,coord,projType,movementPattern,context,context_size):

        def __init__(self,art,context_size,context,weapon):
            self.weapon       = weapon
            self.art          = art
            self.hp           = 100
            self.context_size = context_size
            self.context      = context
            self.pos          = [(self.context_size[0]/2)-16,(self.context_size[1]/2)-16]
            self.vel          = [0,0]
            
        def reset():
            self.hp  = 100
            self.pos = [(self.context_size[0]/2)-16,(self.context_size[1]/2)-16]
            self.weapon.reset()

        def set_x_vel(self,vel):
            self.vel[0]=vel
            
        def set_y_vel(self,vel):
            self.vel[1]=vel

        def mod_x_vel(self,vel):
            self.vel[0]=self.vel[0]+vel
            
        def mod_y_vel(self,vel):
            self.vel[1]=self.vel[1]+vel

        def set_pos(self,pos):#pos must be a list [x_pos, y_pos]
            self.pos = pos
            self.weapon.set_pos(pos)

        def set_weapon(weapon):
            self.weapon = weapon

        def get_weapon(self):
            return self.weapon

        def set_x_pos(self,x_pos):
            self.pos[0] = x_pos
            self.weapon.set_x_pos

        def set_y_pos(self,y_pos):
            self.pos[1] = y_pos

        def get_pos(self):
            return self.pos

        def get_x_pos(self):
            return self.pos[0]

        def get_y_pos(self):
            return self.pos[1]

        def draw(self, context):
            #print("I'm drawing the enemy!!!!!")
            context.blit(self.art, self.pos)
            
        def draw_proj(self):
            self.weapon.draw()
         
        def get_hp(self):
            return self.hp

        def set_hp(self,hp):
            self.hp = hp

        def set_art(art):
            self.art = art
                
        def update_proj(self,genNew):
            self.weapon.updateProj(self.pos[0], self.pos[1], genNew)


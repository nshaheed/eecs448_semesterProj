class ship_object (object):
        def __init__(self,art,context_size):
            self.art = art
            self.hp = 100
            self.context_size = context_size
            self.pos = [(self.context_size[0]/2)-16,(self.context_size[1]/2)-16]
            self.vel = [0,0]

        def x_vel(self,vel):
            self.vel[0]=self.vel[0]+vel
            
        def y_vel(self,vel):
            self.vel[1]=self.vel[1]+vel

        def set_x_pos(self,x_pos):#pos must be a list [x_pos, y_pos]
            self.pos[0] = x_pos

        def set_y_pos(self,y_pos):#pos must be a list [x_pos, y_pos]
            self.pos[1] = y_pos

        def get_pos(self):
            return self.pos

        def draw(self, context):
            context.blit(self.art, self.pos)
         
        def get_hp(self):
                return self.hp

        def set_hp(self,hp):
                self.hp = hp

        def set_art(art):
                self.art = art


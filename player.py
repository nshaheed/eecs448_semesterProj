class player_object (object):
        def __init__(self,art,context_size):
            self.art = art
            self.context_size = context_size
            self.pos = [(self.context_size[0]/2)-16,(self.context_size[1]/2)-16]
            self.vel = [0,0]

        def x_vel(self,vel):
            self.vel[0]=self.vel[0]+vel
            
        def y_vel(self,vel):
            self.vel[1]=self.vel[1]+vel

        def update(self):
            if self.pos[0]+self.vel[0]>=0 and self.pos[0]+self.vel[0]+32<=self.context_size[0]:
                self.pos[0] = self.pos[0]+self.vel[0]
            if self.pos[1]+self.vel[1]>=0 and self.pos[1]+self.vel[1]+32<=self.context_size[1]:
                self.pos[1] = self.pos[1]+self.vel[1]

        def draw(self, context):
            context.blit(self.art, self.pos)
         
        

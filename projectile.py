class projectile_holder_object (object):
    def __init__ (self, art_arr,context_size):
        self.proj_arr = []
        self.proj_ticker = 0
        self.MAX_PROJ = 100
        self.context_size = context_size
        self.art_arr = art_arr
        for i in range(0,self.MAX_PROJ):
            self.proj_arr.append(projectile_object())

    def spawn_proj(self,stats):#the structure of stats is expected to be a list [art_ID,x_loc,y_loc,x_vel,y_vel,proj_type]
        self.proj_arr[self.proj_ticker].spawn(stats)
        self.proj_ticker = (self.proj_ticker + 1)%self.MAX_PROJ

    def update(self):
        for i in range (0,len(proj_arr)):
            if proj_arr[i].active:
                self.proj_arr[i].update()
                
    def draw(context):
        for i in range (0,len(proj_arr)):
            if proj_arr[i].active:
                context.blit(self.art_arr[self.proj_arr[i].stats[0]],self.proj_arr[i].get_loc())

class projectile_object (object):
    def __init__ (self):
        #the structure of stats is [art_ID,x_loc,y_loc,x_vel,y_vel,proj_type]
        self.stats = [0,0,0,0,0,0]
        self.active = False

    def spawn(self,stats):#the structure of stats is expected to be[art_ID,x_loc,y_loc,x_vel,y_vel,proj_type]
        self.stats = stats
        self.active = True
        
    def get_loc(self):
        return(self.stats[1],self.stats[2])
    
    def update(self):
        self.stats[1]=self.stats[1]+self.stats[3]
        self.stats[2]=self.stats[2]+self.stats[4]

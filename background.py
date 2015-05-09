import random
import pygame
class starfield_object (object):
    def __init__(self, context_size):
        self.WHITE    = ( 255, 255, 255)
        self.MAX_STARS = 200#200 looks good
        self.context_size = context_size
        self.star_arr = []
        self.star_arr_init()
        print("Parallax BG initialized!")
        
    def star_arr_init(self):
        for i in range(0,self.MAX_STARS):
            s = random.randint(1,4)#(1,4) is good
            x = random.randint(-3,self.context_size[0]-5)#(-3,self.context_size[0]-5) is good
            y = random.randint(-200,self.context_size[1])#(-200,self.context_size[1]) is good
            w = random.randint(1,3)#(1,3) is good
            l = random.randint(1,3)#(1,3) is good
            v = random.randint(1,100)#(2,7) is good (no loop needed) the loop method looks better with (2,20)
            if v<100:
                v=((v/2)%4)+2
            else:
                v=18
            d = 0 #randint(0,4)-2
            new_star = star_object(self.context_size,s,x,y,w,l,v,d)
            self.star_arr.append(new_star)

    def update(self):
        [self.star_arr[i].update() for i in range(0,len(self.star_arr))]

    def draw(self, context):
        [pygame.draw.rect(context, self.WHITE,[self.star_arr[i].x_loc,self.star_arr[i].y_loc,self.star_arr[i].length,self.star_arr[i].width]) for i in range(0,len(self.star_arr))]

class star_object (object):
    def __init__(self,context_size,size,x_loc,y_loc,length,width,y_vel,x_drift):
        self.context_size = context_size
        self.size = size
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.length = length
        self.width = width
        self.y_vel = y_vel
        self.x_drift = x_drift #unused for he moment
    
    def get_loc(self):
        return (self.x_loc,self.y_loc)
    
    def update(self):
        if ((self.y_loc+self.y_vel+self.size)<=self.context_size[1]):
            self.y_loc = self.y_loc+self.y_vel
        else:
            self.y_loc = random.randint(-350,-50)
            self.x_loc = random.randint(-3,self.context_size[0]-5)#(-3,self.context_size[0]-5) is good
            
            

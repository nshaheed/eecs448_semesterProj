import random
import pygame
class starfield_object (object):
    def __init__(self, context_size):
        self.context_size = context_size
        self.star_arr = []
        self.star_arr_init()
        self.WHITE    = ( 255, 255, 255)
    def star_arr_init(self):
        for i in range(0,200):
            s = random.randint(1,4)
            x = random.randint(-3,self.context_size[0]-5)
            y = random.randint(-200,self.context_size[1])
            w = random.randint(1,3)
            l = random.randint(1,6)
            v = random.randint(2,7)
            d = 0 #randint(-200,context_size[1])
            new_star = star_object(self.context_size,s,x,y,w,l,v,d)
            self.star_arr.append(new_star)

    def update(self):
        for i in range(0,len(self.star_arr)):
            self.star_arr[i].update()

    def draw(self, context):
        for i in range(0,len(self.star_arr)):
            pygame.draw.rect(context, self.WHITE,[self.star_arr[i].x_loc,self.star_arr[i].y_loc,self.star_arr[i].length,self.star_arr[i].width])


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
            self.y_loc = -200
            
            

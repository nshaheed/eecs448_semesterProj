import enemy
import projectile2
import weapon
import ai
import math
import random
import threading
import projectile2

class enemy_holder(object):
    def __init__(self,ship_art,proj_art,context_size,context):
        self.time          = 0
        self.context_size  = context_size
        self.context       = context
        #weap1             = weapon.weapon((0,0), proj1, mvmtPtrn1, screen, size)
        self.enemy_arr     = []
        self.ship_art_arr  = ship_art
        self.proj_art_arr  = proj_art
        self.move_ptrn_arr = []
        self.ai_func_arr   = []
        self.proj1         = projectile2.Projectile(0, 0, 15, 1.5 * math.pi, 10, proj_art[0])
        self.move_ptrn_arr.append(self.mvmtPtrn1)
        #self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def reset(self):
        self.enemy_arr     = []

    def update(self):
        [self.enemy_arr[i].update() for i in range(len(self.enemy_arr))]
        self.time = (self.time +1)%250
        if not self.time:
            self.add_random_enemy()
            #self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])
            
    # def points(self):
        # return len([
            
    # detects collisions between enemy ships and player projectiles
    def update_coll(self, proj, proj_size):

        points = 0
        # Go through all enemy ships
        for i in range(len(self.enemy_arr)):
            ship_pos  = self.enemy_arr[i].get_pos()
            ship_size = self.enemy_arr[i].get_art_size()
            
            # print("ship pos:  " + str(ship_pos))
            # print("ship size: " + str(ship_size))
            
            # check if projectiles overlap with the current ship
            for j in range(len(proj)):
                # find if the boxes are intersecting
                x_bool = math.fabs(ship_pos[0] - (proj[j][0] + proj_size[0])) + 15 < (ship_size[0] + proj_size[0])
                y_bool = math.fabs(ship_pos[1] - (proj[j][1] + proj_size[1])) + 15 < (ship_size[1] + proj_size[1])
                
                # if there is a collision, kill the ship
                if x_bool and y_bool:
                    #print("coll" + str(i))
                    self.enemy_arr[i].set_alive(False)
                    points += 1
                    #print(self.enemy_arr[i].get_alive())
                  
        # print(points)
        return points
                    
    def update_proj_coll(self,player_pos,player_size=(32,32)):
        for i in range(len(self.enemy_arr)):
            proj = self.enemy_arr[i].weapon.get_proj_pos()
            #print(proj)
            proj_size = self.enemy_arr[i].weapon.get_proj_art_size()

            for j in range(len(proj)):
                x_bool = math.fabs(player_pos[0] - (proj[j][0] + proj_size[0])) < (player_size[0] + proj_size[0])
                y_bool = math.fabs(player_pos[1] - (proj[j][1] + proj_size[1])) < (player_size[1] + proj_size[1])
                
            # if there is a collision, kill the ship
                if x_bool and y_bool:
                    return True
        return False
    
    def draw(self):
        [self.enemy_arr[i].draw(self.context) for i in range(len(self.enemy_arr))]

    def add_enemy(self,art,ai_obj,weapon, weapon_ptrn):
        self.enemy_arr.append(enemy.enemy_object(art, self.context_size, self.context, ai_obj, weapon,self.proj1,weapon_ptrn))


    def add_random_enemy(self):
        (ai_func, args) = random.choice(ai.aiList)
        ai_object = ai_func(*args)
        self.add_enemy(random.choice(self.ship_art_arr), ai_object, weapon.weapon, random.choice(self.move_ptrn_arr))

    def kill_enemy(self,i):
        self.enemy_arr.pop(i)

    def draw_proj(self):
        for i in range(len(self.enemy_arr)):
            self.enemy_arr[i].draw_proj()

    def update_proj(self):
    
        # Finds which enemies are alive,
        #   if an enemy is dead and it has
        #   no projectiles, it is totally
        #   dead, remove it
        removeIdx = []
        for i in range(len(self.enemy_arr)):
            self.enemy_arr[i].update_proj(True)
            if not self.enemy_arr[i].get_alive():
               # print(len(self.enemy_arr[i].get_weapon().get_proj()))
                if len(self.enemy_arr[i].get_weapon().get_proj()) == 0:
                    # print("adding " + str(i))
                    removeIdx.append(i)
                    
        #print(removeIdx)
                    
        # removes enemies that are totally dead 
        for j in range(len(removeIdx)-1,-1,-1):
            del self.enemy_arr[removeIdx[j]]
            
        # [self.enemy_arr[i].update_proj(True) for i in range(len(self.enemy_arr))]

       # threads = []
       # for i in range(len(self.enemy_arr)):
       #     t=threading.Thread(target=self.enemy_arr[i].update_proj,args =(True,))
       #     threads.append(t)
       # for t in threads:
       #     t.start()

       # for x in threads:
       #     x.join()


    def mvmtPtrn1(self,x):
        if x % 32 == 0: # fire proj
            return (.5 * math.pi)
        else:
            return None    
       
# straight line       
# def mvmtPtrn1(x):
    # if x % 8 == 0: # fire proj
        # return (1.5 * math.pi)
    # else:
        # return None
        
 # spray
# def mvmtPtrn2(x):
    # if x % 8 == 0: # fire proj
        # return (1.5 * math.pi)
    # else:
        # return None

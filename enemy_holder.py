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
        self.time = 0
        self.context_size = context_size
        self.context = context
        #weap1    = weapon.weapon((0,0), proj1, mvmtPtrn1, screen, size)
        self.enemy_arr = []
        self.ship_art_arr = ship_art
        self.proj_art_arr = proj_art
        self.move_ptrn_arr = []
        self.proj1    = projectile2.Projectile(0, 0, 15, 1.5 * math.pi, 10, proj_art[0])
        self.move_ptrn_arr.append(self.mvmtPtrn1)
        #self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def update(self):
        [self.enemy_arr[i].update() for i in range(len(self.enemy_arr))]
        self.time = (self.time +1)%250
        if not self.time:
            self.add_random_enemy()
            #self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def draw(self):
        [self.enemy_arr[i].draw(self.context) for i in range(len(self.enemy_arr))]

    def add_enemy(self,art,ai_obj,weapon, weapon_ptrn):
        self.enemy_arr.append(enemy.enemy_object(art, self.context_size, self.context, ai_obj, weapon,self.proj1,weapon_ptrn))


    def add_random_enemy(self):
        (ai_func, args) = random.choice(ai.aiList)
        ai_object = ai_func(*args)
        self.add_enemy(random.choice(self.ship_art_arr), ai_object, weapon.weapon, random.choice(self.move_ptrn_arr))
#=======
#    def add_enemy(self,art,ai_func,weapon,weapon_ptrn):
#        self.enemy_arr.append(enemy.enemy_object(self.ship_art_arr[random.randint(0,2)],self.context_size,self.context,ai_func(),weapon,self.proj1,weapon_ptrn))
#>>>>>>> 6ed0d6e78b57e80bf8639a16da639d31a57fcb81

    def kill_enemy(self,i):
        self.enemy_arr.pop(i)

    def draw_proj(self):
        for i in range(len(self.enemy_arr)):
            self.enemy_arr[i].draw_proj()

    def update_proj(self):
        [self.enemy_arr[i].update_proj(True) for i in range(len(self.enemy_arr))]

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
        

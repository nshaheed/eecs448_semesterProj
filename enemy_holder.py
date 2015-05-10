import enemy
import projectile2
import weapon
import ai
import math
import random

class enemy_holder(object):
    def __init__(self,art_arr,context_size,context):
        self.proj1    = projectile2.Projectile(0, 0, 15, 1.5 * math.pi, 10, "Assets/Art/projectile.png")
        self.time = 0
        self.context_size = context_size
        self.context = context
        #weap1    = weapon.weapon((0,0), proj1, mvmtPtrn1, screen, size)
        self.enemy_arr = []
        self.art_arr = art_arr
        self.move_ptrn_arr = []
        self.ai_func_arr = []
        self.move_ptrn_arr.append(self.mvmtPtrn1)
        self.ai_func_arr.append(ai.circling_ai)
        #self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def update(self):
        [self.enemy_arr[i].update() for i in range(len(self.enemy_arr))]
        self.time = (self.time +1)%250
        if not self.time:
            self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def draw(self):
        [self.enemy_arr[i].draw(self.context) for i in range(len(self.enemy_arr))]

    def add_enemy(self,art,ai_func,weapon,weapon_ptrn):
        self.enemy_arr.append(enemy.enemy_object(self.art_arr[random.randint(0,2)],self.context_size,self.context,ai_func(),weapon,self.proj1,weapon_ptrn))

    def kill_enemy(i):
        self.enemy_arr.pop(i)


    def mvmtPtrn1(x):
        if x % 8 == 0: # fire proj
            return (1.5 * math.pi)
        else:
            return None    
        

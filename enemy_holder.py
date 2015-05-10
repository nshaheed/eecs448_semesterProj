import enemy
import projectile2
import weapon

class enemy_holder(object):
    def __init__(self,art_arr,context_size,context):
        #proj1    = projectile2.Projectile(0, 0, 15, 1.5 * math.pi, 10, "Assets/Art/projectile.png")
        #weap1    = weapon.weapon((0,0), proj1, mvmtPtrn1, screen, size)
        self.enemy_arr = []
        self.art_arr = art_arr
        self.move_ptrn_arr = []
        self.ai_func_arr = []
        self.move_ptrn_arr.append(mvmtPtrn1)
        self.add_enemy(self.art_arr[0],self.ai_func_arr[0],weapon.weapon,self.move_ptrn_arr[0])

    def update(self):
        [self.enemy_arr[i].update() for i in range(0,len(self.enemy_arr))]

    def add_enemy(self,art,ai_func,weapon,weapon_ptrn):
        self.enemy_arr.append(enemy.enemy_object(self.art_arr[0],self.context_size,self.context,ai_func(),weapon,weapon_ptrn))

    def kill_enemy(i):
        self.enemy_arr.pop(i)


    def mvmtPtrn1(x):
        if x % 8 == 0: # fire proj
            return (1.5 * math.pi)
        else:
            return None    
        

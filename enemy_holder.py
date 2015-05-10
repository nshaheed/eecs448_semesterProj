import enemy
class enemy_holder(object):
    def __init__(self,art_arr,):
        self.enemy_arr = []
        

    def update(self):
        [self.enemy_arr[i].update() for i in range(0,len(self.enemy_arr))]

    def add_enemy(self,art,context_size,ai,weapon):
        self.enemy_arr.append(enemy.enemy_object(art,context_size,context,ai,weapon))

    def kill_enemy(i):
        self.enemy_arr.pop(i)


        
        

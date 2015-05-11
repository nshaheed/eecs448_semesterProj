# import pygame library
import pygame
import math
import player
import menu
import background
import projectile_temp
import threading
import projectile2 
import weapon
import enemy_holder

# initializing pygame
pygame.init()

print(str(pygame.mixer.get_num_channels()))
# Color definitions
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#defins max ups
GAME_UPS = 60

#player move speed
PLAYER_VEL = 10

# creating the window
size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PySho!")

# music loader
#menu_music = pygame.mixer.music.load("Assets/Music/main_menu.mp3")
pygame.mixer.music.load("Assets/Music/main_menu.mp3")
#game_session_music = pygame.mixer.music.load("Assets/Music/gmPly.mp3")
print("Music loaded!")

# soundFX loader
player_shoot_laser_sound = pygame.mixer.Sound("Assets/SoundFX/Laser_Shoot7.wav")
explosion_death_sound    = pygame.mixer.Sound("Assets/SoundFX/Explosion4.wav")
hull_damage_sound        = pygame.mixer.Sound("Assets/SoundFX/Explosion2.wav")
shield_damage_sound      = pygame.mixer.Sound("Assets/SoundFX/Hit_Hurt82.wav")
burning_death_sound      = pygame.mixer.Sound("Assets/SoundFX/Danger2.wav")
print("SoundFX loaded!")

# art loader
# ships
player_ship    = pygame.image.load("Assets/Art/player_ship.png")#.convert()
enemy_ship     = pygame.image.load("Assets/Art/enemy_ship.png")#.convert()
kamina_ship    = pygame.image.load("Assets/Art/kamina_ship.png")#.convert()
boss_ship      = pygame.image.load("Assets/Art/enemy_ship_mb0.png")#.convert()

#enemy ship arrays
enemy_ship_arr = []
enemy_ship_arr.append(enemy_ship)
enemy_ship_arr.append(kamina_ship)
enemy_ship_arr.append(boss_ship)

menu_art = []
menu_art.append(boss_ship)
menu_art.append(enemy_ship)
menu_art.append(kamina_ship)
menu_art.append(player_ship)
# shields
shield         = pygame.image.load("Assets/Art/shield_dmg_0.png")#.convert()
shield_dmg     = pygame.image.load("Assets/Art/shield_dmg_1.png")#.convert()

# projectiles
p_proj_art_arr = [] #order is player proj
e_proj_art_arr = [] #order is eproj, eproj2
p_proj_art_arr.append(pygame.image.load("Assets/Art/projectile.png"))#.convert())
e_proj_art_arr.append(pygame.image.load("Assets/Art/Eprojectile_2.png"))#.convert())
e_proj_art_arr.append(pygame.image.load("Assets/Art/Eprojectile.png"))#.convert())
print("Art loaded!")

# spawn a proj every other frame, returning 1.5 * pi when returning an angle
def mvmtPtrn1(x):
    if x % 8 == 0: # fire proj
        return (1.5 * math.pi)
    else:
        return None
        
proj1    = projectile2.Projectile(0, 0, 15, 1.5 * math.pi, 10, p_proj_art_arr[0])
weap1    = weapon.weapon((0,0), proj1, mvmtPtrn1, screen, size)

# object initialization

menu               = menu.menu_object(menu_art,size,screen)
player             = player.player_object(player_ship,size,screen,weap1)
starfield          = background.starfield_object(size)
enemy_hldr         = enemy_holder.enemy_holder(enemy_ship_arr,e_proj_art_arr,size,screen)

#tracks if the player is alive
player_alive = True

#tracks frames for timers
frame_counter = 0

#value to determine if the player is shooting or not
spawn_proj = False
                
# value to keep the program running or exit
done = False

#value to track whether a game is in session or not
running = False

#value to track whether a game is in paused or not
paused = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# holds menu button positions and sizes
menu_pos = [(90,120,420,200),(175,460,250,100),(175,590,250,100)]
pygame.mixer.music.play(-1)

while not done:
    # Main event loop
    
    #updates the mouse position
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.           
            # escape to pause/unpause the game
            if event.key == pygame.K_ESCAPE:
                if not paused:
                    running = False
                    paused  = True
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    running = True
            if event.key == pygame.K_a:
                player.mod_x_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_d:
                player.mod_x_vel(PLAYER_VEL)
            if event.key == pygame.K_w:
                player.mod_y_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_s:
                player.mod_y_vel(PLAYER_VEL)
            if event.key == pygame.K_SPACE:
                spawn_proj = True           
            #print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a:
                player.mod_x_vel(PLAYER_VEL)
            if event.key == pygame.K_d:
                player.mod_x_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_w:
                player.mod_y_vel(PLAYER_VEL)
            if event.key == pygame.K_s:
                player.mod_y_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_SPACE:
                spawn_proj = False
            #print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not running:
                if mouse_pos[0]<426 and mouse_pos[0]>174:
                    if mouse_pos[1]<559 and mouse_pos[1]>459:
                        if paused:
                            paused = False
                            pygame.mixer.music.unpause()
                        elif player_alive:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("Assets/Music/gmPly.mp3")
                            pygame.mixer.music.play(-1)
                        running=True;
                    elif mouse_pos[1]<689 and mouse_pos[1]>589:
                        if paused:
                            paused = False
                            player_alive = True
                            menu.set_hp(100)
                            player.__init__(player_ship,size,screen,weap1)
                            enemy_hldr.reset()
                            pygame.mixer.music.load("Assets/Music/main_menu.mp3")
                            pygame.mixer.music.play(-1)
                        else:
                            done= True  # Flag that we are done so we exit this loop
                        #print("User wants to leave...")
            #print("User pressed a mouse button")
            
    # Game logic should go here

    #update starfield background
    if not paused:
        #threading usage example. I'd like to contain the big
        starfield_t=threading.Thread(target=starfield.update)
        starfield_t.start()

    if not running:
        pass
        #call menu class and do menu things
    else:
        #call game class and do game things and update game variables and stuff

        #updates player loc
        player_t=threading.Thread(target=player.update)
        player_t.start()
        #player.update()
        
        # update coords for player projectile, have spawn_proj be pass to update_proj
        proj_t=threading.Thread(target=player.update_proj,args =(spawn_proj,))
        proj_t.start()
        enemy_t=threading.Thread(target=enemy_hldr.update)
        enemy_t.start()
        enemy_proj_t=threading.Thread(target=enemy_hldr.update_proj)
        enemy_proj_t.start()   
    
    # Drawing code should go here  
    # clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #draw starfield background
    starfield_t.join()

    starfield.draw(screen)

    #the process of thread joining should be double checked and cleaned up
        # if not running, call pause/main menu, otherwise do game stuff
    if not running:
        if not paused:
            menu.draw_menu()
        else:
            player_t.join()
            proj_t.join()
            enemy_proj_t.join()
            enemy_t.join()

            #drawing for the pause menu
            enemy_hldr.draw_proj()
            enemy_hldr.draw()
            player.draw_proj()
            if player_alive:
                menu.draw_pause(player.get_pos())
            else:
                menu.draw_game_over(player.get_pos())

    else:
        # fire weapon if space bar is held down
        # put colision detection here
        player_t.join()
        proj_t.join()
        enemy_proj_t.join()
        enemy_t.join()

        # collision detection & update points
        points = enemy_hldr.update_coll(player.get_weapon().get_proj_pos(),player.get_weapon().get_proj_art_size())
        # print(points)
        menu.add_points(points)

        #begin the final updates and drawing
        if enemy_hldr.update_proj_coll(player.get_pos()):
            menu.dec_hp()        
        enemy_hldr.draw_proj()
        enemy_hldr.draw()
        player.draw_proj()
            #call game class and do game things and update game variables and stuff
        player.draw(screen)
            # adds hud
        menu.draw_hud()
        
        # Go ahead and update the screen with what we've drawn.
    if not menu.get_hp():
    #if not True:
        player_alive = False
        paused = True
        running = False
    
    pygame.display.flip()
    # --- Limit to 60 frames per second
    frame_counter = frame_counter+1    
    clock.tick_busy_loop(GAME_UPS)
pygame.quit()

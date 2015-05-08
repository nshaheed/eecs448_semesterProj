# import pygame library
import pygame
import math
import player
import menu
import background
import projectile
import threading

# initializing pygame
pygame.init()

print(str(pygame.mixer.get_num_channels()))
# Color definitions
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#defins max fps
GAME_FPS = 60

#player move speed
PLAYER_VEL = 5

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
player_ship = pygame.image.load("Assets/Art/player_ship.png")#.convert()
enemy_ship     = pygame.image.load("Assets/Art/enemy_ship.png")#.convert()
kamina_ship    = pygame.image.load("Assets/Art/kamina_ship.png")#.convert()
boss_ship      = pygame.image.load("Assets/Art/enemy_ship_mb0.png")#.convert()
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

# object initialization
player             = player.player_object(player_ship,size)
starfield          = background.starfield_object(size)
enemy_proj_holder  = projectile.projectile_holder_object(e_proj_art_arr,size)
player_proj_holder = projectile.projectile_holder_object(p_proj_art_arr,size)

# Select the font to use, size, (bold, italics)
title_font = pygame.font.SysFont('Calibri', 140, True, False)
menu_font  = pygame.font.SysFont('Calibri', 50, True, False)
hud_font   = pygame.font.SysFont('Calibri', 25, True, False)

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

# move this to separate file eventually
def pause_menu():
    #call menu class and do menu things

    #menu ship preview
    screen.blit(player_ship, player.get_pos())
    screen.blit(enemy_ship,  ((size[0]/2)-121, 60))
    screen.blit(enemy_ship,  ((size[0]/2)+89, 60))
    screen.blit(boss_ship,   ((size[0]/2)-75, 20))

        
    # menu structure code        
    pygame.draw.rect(screen, RED, [menu_pos[0][0],menu_pos[0][1],menu_pos[0][2],menu_pos[0][3]])
    pygame.draw.rect(screen, RED, [menu_pos[1][0],menu_pos[1][1],menu_pos[1][2],menu_pos[1][3]])
    pygame.draw.rect(screen, RED, [menu_pos[2][0],menu_pos[2][1],menu_pos[2][2],menu_pos[2][3]])

    #render strings to text
    title_text   = title_font.render("PySho!",True,WHITE)
    start_text_1 = menu_font.render("Resume",True,WHITE)
    start_text_2 = menu_font.render("conquering",True,WHITE)
    exit_text_1  = menu_font.render("Exit",True,WHITE)
    exit_text_2  = menu_font.render("to class...",True,WHITE)
        
    # Put the image of the text on the screen at 250x250
    screen.blit(title_text, [98, 155])
    screen.blit(start_text_1, [211, 460])
    screen.blit(start_text_2, [186, 505])
    screen.blit(exit_text_1, [262, 595])
    screen.blit(exit_text_2, [203, 640])
	
def main_menu():
    #call menu class and do menu things

    #menu ship preview
    screen.blit(player_ship, ((size[0]/2)-16, (size[1]/2)-16))
    screen.blit(enemy_ship,  ((size[0]/2)-121, 60))
    screen.blit(enemy_ship,  ((size[0]/2)+89, 60))
    screen.blit(boss_ship,   ((size[0]/2)-75, 20))

        
    # menu structure code        
    pygame.draw.rect(screen, RED, [menu_pos[0][0],menu_pos[0][1],menu_pos[0][2],menu_pos[0][3]])
    pygame.draw.rect(screen, RED, [menu_pos[1][0],menu_pos[1][1],menu_pos[1][2],menu_pos[1][3]])
    pygame.draw.rect(screen, RED, [menu_pos[2][0],menu_pos[2][1],menu_pos[2][2],menu_pos[2][3]])

    #render strings to text
    title_text   = title_font.render("PySho!",True,WHITE)
    start_text_1 = menu_font.render("Conquer",True,WHITE)
    start_text_2 = menu_font.render("your foes!!",True,WHITE)
    exit_text_1  = menu_font.render("Exit",True,WHITE)
    exit_text_2  = menu_font.render("to class...",True,WHITE)
        
    # Put the image of the text on the screen at 250x250
    screen.blit(title_text,   [98, 155])
    screen.blit(start_text_1, [211, 460])
    screen.blit(start_text_2, [186, 505])
    screen.blit(exit_text_1,  [262, 595])
    screen.blit(exit_text_2,  [203, 640])
	
# layers the hud on top of the game
def hud():
	# health and points values
	health = player.get_hp()
	points = 0
	
	# render strings to text
	health_text = hud_font.render("Health: " + str(health), True, WHITE)
	points_text = hud_font.render("Points: " + str(points), True, WHITE)
	
	# put the image of the text on the screen in the bottom left corner (
	screen.blit(health_text, [15, 730])
	screen.blit(points_text, [15, 765])
	
while not done:
    # Main event loop
    
    #updates the mouse position
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            #print("User chose to quit.")
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_ESCAPE:
                if not paused:
                    running = False
                    paused  = True
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    running = True
            #if event.key == pygame.K_ESCAPE: # have escape pause the game
            #done = True
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
                        #print("User wants to play!")
                        #game.init()
                        if paused:
                            paused = False
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.fadeout(500)
                            pygame.mixer.music.load("Assets/Music/gmPly.mp3")
                            pygame.mixer.music.play(-1)
                        running=True;
                    elif mouse_pos[1]<689 and mouse_pos[1]>589:
                        done = True  # Flag that we are done so we exit this loop
                        #print("User wants to leave...")
            #print("User pressed a mouse button")
            
    # Game logic should go here

    #update starfield background
    if not paused:
        #threading usage example. I'd like to contain the big
        #update sweeps in individual threads per object.
        #Ex, starfield update thread, projectile thread, enemy ai thread,...
        starfield_t=threading.Thread(target=starfield.update)
        starfield_t.start()
        #starfield.update()

    if not running:
        pass
        #call menu class and do menu things
    else:
        #call game class and do game things and update game variables and stuff

        #determines if the player is firing and limits then to a predefined firing rate (framerate/counter modulus)
        if (spawn_proj):
            if (not (frame_counter%8)):
                player_proj_holder.spawn_proj([0,player.get_pos()[0],player.get_pos()[1],0,-10,0])

        #updates player loc
        player.update()
		
        #updates the various projectile holders
        player_proj_holder.update()
        enemy_proj_holder.update()
    
    
    # Drawing code should go here  
    # clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #draw starfield background
    starfield_t.join()
    starfield.draw(screen)
    
    # if not running, call pause/main menu, otherwise do game stuff
    if not running:
        if not paused:
            main_menu()
        else:
            pause_menu()

    else:
        #call game class and do game things and update game variables and stuff
        player_proj_holder.draw(screen)
        player.draw(screen)
        enemy_proj_holder.draw(screen)
        # adds hud
        hud()
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    #clock.tick(60)
    frame_counter = frame_counter+1    
    clock.tick_busy_loop(GAME_FPS)
pygame.quit()

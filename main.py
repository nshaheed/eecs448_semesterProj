# import pygame library
import pygame
import math
import player
import menu
# initializing pygame
pygame.init()

# Color definitions
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#player move speed
PLAYER_VEL = 5

# creating the window
size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PySho!")

# music loader
menu_music = pygame.mixer.Sound("Assets/Music/main_menu.mp3")
game_session_music = pygame.mixer.Sound("Assets/Music/gmPly.mp3")
print("Music loaded!")

# soundFX loader
player_shoot_laser_sound = pygame.mixer.Sound("Assets/SoundFX/Laser_Shoot7.wav")
explosion_death_sound = pygame.mixer.Sound("Assets/SoundFX/Explosion4.wav")
hull_damage_sound = pygame.mixer.Sound("Assets/SoundFX/Explosion2.wav")
shield_damage_sound = pygame.mixer.Sound("Assets/SoundFX/Hit_Hurt82.wav")
burning_death_sound = pygame.mixer.Sound("Assets/SoundFX/Danger2.wav")
print("SoundFX loaded!")

# art loader
# ships
player_ship = pygame.image.load("Assets/Art/player_ship.png")#.convert()
enemy_ship = pygame.image.load("Assets/Art/enemy_ship.png")#.convert()
kamina_ship = pygame.image.load("Assets/Art/kamina_ship.png")#.convert()
boss_ship = pygame.image.load("Assets/Art/enemy_ship_mb0.png")#.convert()
# shilelds
shield = pygame.image.load("Assets/Art/shield_dmg_0.png")#.convert()
shield_dmg = pygame.image.load("Assets/Art/shield_dmg_1.png")#.convert()
# projectiles
enemy_projectile_1 = pygame.image.load("Assets/Art/Eprojectile_2.png")#.convert()
enemy_projectile_2 = pygame.image.load("Assets/Art/Eprojectile.png")#.convert()
player_projectile = pygame.image.load("Assets/Art/projectile.png")#.convert()
print("Art loaded!")

# object initialization
player = player.player_object(player_ship,size)

# Select the font to use, size, (bold, italics)
title_font = pygame.font.SysFont('Calibri', 140, True, False)
menu_font = pygame.font.SysFont('Calibri', 50, True, False)
                
# value to keep the program running or exit
done = False

#value to track wether a game is in session or not
running = False

#value to track wether a game is in paused or not
paused = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# holds menu button positions and sizes
menu_pos = [(90,120,420,200),(175,460,250,100),(175,590,250,100)]

while not done:
    # Main event loop
    
    #updates the mouse position
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            print("User chose to quit.")
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_a:
                player.x_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_d:
                player.x_vel(PLAYER_VEL)
            if event.key == pygame.K_w:
                player.y_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_s:
                player.y_vel(PLAYER_VEL)
            if event.key == pygame.K_SPACE:
                pass           
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a:
                player.x_vel(PLAYER_VEL)
            if event.key == pygame.K_d:
                player.x_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_w:
                player.y_vel(PLAYER_VEL)
            if event.key == pygame.K_s:
                player.y_vel(-1*PLAYER_VEL)
            if event.key == pygame.K_SPACE:
                pass
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[0]<426 and mouse_pos[0]>174:
                if mouse_pos[1]<559 and mouse_pos[1]>459:
                    print("User wants to play!")
                    #game.init()
                    running=True;
                elif mouse_pos[1]<689 and mouse_pos[1]>589:
                    done = True  # Flag that we are done so we exit this loop
                    print("User wants to leave...")
            print("User pressed a mouse button")
            
    # Game logic should go here

    if not running:
        pass
        #call menu class and do menu things
    else:
        #call game class and do game things and update game variables and stuff
        player.update()
    
    
    # Drawing code should go here  
    # clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    
    if not running:
        #call menu class and do menu things

        # menu structure code        
        pygame.draw.rect(screen, RED, [menu_pos[0][0],menu_pos[0][1],menu_pos[0][2],menu_pos[0][3]])
        pygame.draw.rect(screen, RED, [menu_pos[1][0],menu_pos[1][1],menu_pos[1][2],menu_pos[1][3]])
        pygame.draw.rect(screen, RED, [menu_pos[2][0],menu_pos[2][1],menu_pos[2][2],menu_pos[2][3]])

        #render strings to text
        title_text = title_font.render("PySho!",True,WHITE)
        start_text_1 = menu_font.render("Conquer",True,WHITE)
        start_text_2 = menu_font.render("your foes!!",True,WHITE)
        exit_text_1 = menu_font.render("Exit",True,WHITE)
        exit_text_2 = menu_font.render("to class...",True,WHITE)
        
        # Put the image of the text on the screen at 250x250
        screen.blit(title_text, [98, 155])
        screen.blit(start_text_1, [211, 460])
        screen.blit(start_text_2, [186, 505])
        screen.blit(exit_text_1, [262, 595])
        screen.blit(exit_text_2, [203, 640])

    else:
        #call game class and do game things and update game variables and stuff
        player.draw(screen)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()

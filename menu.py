import pygame
class menu_object (object):
        def __init__(self,art,context_size,context):
            self.menu_pos = [(90,120,420,200),(175,460,250,100),(175,590,250,100)]
            self.art_arr = art
            self.context_size = context_size
            self.context = context
            self.health = 100
            self.points = 0
            self.BLACK    = (   0,   0,   0)
            self.WHITE    = ( 255, 255, 255)
            self.GREEN    = (   0, 255,   0)
            self.RED      = ( 255,   0,   0)
            self.BLUE     = (   0,   0, 255)
            # Select the font to use, size, (bold, italics)
            self.title_font = pygame.font.SysFont('Calibri', 140, True, False)
            self.menu_font  = pygame.font.SysFont('Calibri', 50,  True, False)
            self.hud_font   = pygame.font.SysFont('Calibri', 25,  True, False) 
            self.title_text = self.title_font.render("PySho!",True,self.WHITE)
            self.start_text_1 = self.menu_font.render("Conquer",True,self.WHITE)
            self.start_text_2 = self.menu_font.render("your foes!!",True,self.WHITE)
            self.exit_text_1 = self.menu_font.render("Exit",True,self.WHITE)
            self.exit_text_2 = self.menu_font.render("to class...",True,self.WHITE)
            self.pause_text_1 = self.menu_font.render("Resume",True,self.WHITE)
            self.pause_text_2 = self.menu_font.render("conquering",True,self.WHITE)
            self.menu_return_text_1 = self.menu_font.render("Go to",True,self.WHITE)
            self.menu_return_text_2 = self.menu_font.render("menu...",True,self.WHITE)
            self.health_text = self.hud_font.render("Health: " + str(self.health), True, self.WHITE)
            self.points_text = self.hud_font.render("Points: " + str(self.points), True, self.WHITE)
            print("Menu Initialized!")
            
        def set_hp(self,hp):
            self.health = health
            self.health_text = self.hud_font.render("Health: " + str(self.health), True, self.WHITE)

        def dec_hp(self,dec=1):
            self.health = self.health-dec
            self.health_text = self.hud_font.render("Health: " + str(self.health), True, self.WHITE)

        def set_points(self,points):
            self.points_text = self.hud_font.render("Points: " + str(self.points), True, self.WHITE)
            self.points = points
            
        def clicked(self,mouse_pos):
            #check to see if the mouse pos is inside the buttons.
            #if the mosue clicked a button, return the appropriate function...still figuring out a clean way

                if mouse_pos[0]<426 and mouse_pos[0]>174:
                        if mouse_pos[1]<559 and mouse_pos[1]>459:
                            print("User wants to play!")
                            e = start_game
                            return e
                        elif mouse_pos[1]<689 and mouse_pos[1]>589:
                            #done = True  # Flag that we are done so we exit this loop
                            return exit_game
                            print("User wants to leave...")
                return do_nothing

        def start_game(self):
            running = True

        def exit_game(self):
            done = True

        def do_nothing(self):
            pass
        
        def draw_menu(self):
            #draw menu objects
            self.draw_ships()
            pygame.draw.rect(self.context, self.RED, self.menu_pos[0])
            pygame.draw.rect(self.context, self.RED, self.menu_pos[1])
            pygame.draw.rect(self.context, self.RED, self.menu_pos[2])
            self.context.blit(self.title_text, [98, 155])
            self.context.blit(self.start_text_1, [211, 460])
            self.context.blit(self.start_text_2, [186, 505])
            self.context.blit(self.exit_text_1, [262, 595])
            self.context.blit(self.exit_text_2, [203, 640])

        def draw_pause(self,player_pos):
            self.draw_ships(player_pos,True)
            #pygame.draw.rect(self.context, self.RED, self.menu_pos[0])
            pygame.draw.rect(self.context, self.RED, self.menu_pos[1])
            pygame.draw.rect(self.context, self.RED, self.menu_pos[2])
            #self.context.blit(self.title_text, [98, 155])
            self.context.blit(self.pause_text_1, [211, 460])
            self.context.blit(self.pause_text_2, [186, 505])
            self.context.blit(self.menu_return_text_1, [262, 595])
            self.context.blit(self.menu_return_text_2, [203, 640])

        def draw_hud(self):
            self.context.blit(self.health_text, [15, 730])
            self.context.blit(self.points_text, [15, 765])    

        def draw_ships(self,player_pos=(0,0),paused=False):
            #menu ship preview
            if paused:
                self.context.blit(self.art_arr[3], player_pos)
            else:
                self.context.blit(self.art_arr[3], ((self.context_size[0]/2)-16, (self.context_size[1]/2)-16))
                self.context.blit(self.art_arr[1], ((self.context_size[0]/2)-121, 60))
                self.context.blit(self.art_arr[1], ((self.context_size[0]/2)+89, 60))
                self.context.blit(self.art_arr[0], ((self.context_size[0]/2)-75, 20))    

            

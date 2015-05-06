class menu_object (object):
        def __init__(self,art,context_size):
            self.menu_pos = [(90,120,420,200),(175,460,250,100),(175,590,250,100)]
            self.context_size = context_size

            self.title_text = title_font.render("PySho!",True,WHITE)
            self.start_text_1 = menu_font.render("Conquer",True,WHITE)
            self.start_text_2 = menu_font.render("your foes!!",True,WHITE)
            self.exit_text_1 = menu_font.render("Exit",True,WHITE)
            self.exit_text_2 = menu_font.render("to class...",True,WHITE)
            
        def x_vel(self,vel):
            pass
            #don't know if this is necessary for the menu
        def y_vel(self,vel):
            pass
            #don't know if this is necessary for the menu
        def clicked(self,mouse_pos):
            #check to see if the mouse pos is inside the buttons.
            #if the mosue clicked a button, return the appropriate function...still figuring out a clean way

                if mouse_pos[0]<426 and mouse_pos[0]>174:
                        if mouse_pos[1]<559 and mouse_pos[1]>459:
                            print("User wants to play!")
                            e = start_game()
                            return e
                        elif mouse_pos[1]<689 and mouse_pos[1]>589:
                            done = True  # Flag that we are done so we exit this loop
                            print("User wants to leave...")

        def start_game(self):
            pass

        def exit_game(self):
            pass

        def do_nothing(self):
            pass
        
        def draw(self, context):
            #draw menu objects
            pygame.draw.rect(context, RED, [self.menu_pos[0][0],self.menu_pos[0][1],self.menu_pos[0][2],self.menu_pos[0][3]])
            pygame.draw.rect(context, RED, [self.menu_pos[1][0],self.menu_pos[1][1],self.menu_pos[1][2],self.menu_pos[1][3]])
            pygame.draw.rect(context, RED, [self.menu_pos[2][0],self.menu_pos[2][1],self.menu_pos[2][2],self.menu_pos[2][3]])

            

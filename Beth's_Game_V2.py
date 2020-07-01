# @@@@@@@@@@@@@@@@@@@ Beth's Game @@@@@@@@@@@@@@@@@@@@@@@

#Gain access to the pygame library
import pygame

# Pygame, mixer and font initiations. Font decision:
pygame.mixer.init()
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 70)

# A test to make sure mixer is up and running, returns error if not working.
pygame.mixer.get_init()

# The sounds are stored in the same file as the code.
BS1 = pygame.mixer.Sound('./sound_files/Birdsong 1.ogg')
BS2 = pygame.mixer.Sound('./sound_files/Birdsong 2.ogg')
BS3 = pygame.mixer.Sound('./sound_files/Birdsong 3.ogg')
BS4 = pygame.mixer.Sound('./sound_files/Birdsong 4.ogg')

P1 = pygame.mixer.Sound('./sound_files/p1soundtr.ogg')
P2 = pygame.mixer.Sound('./sound_files/p2soundtr.ogg')
P3 = pygame.mixer.Sound('./sound_files/p3soundtr.ogg')
P4 = pygame.mixer.Sound('./sound_files/p4soundtr.ogg')
P5 = pygame.mixer.Sound('./sound_files/p5soundtr.ogg')
P6 = pygame.mixer.Sound('./sound_files/p6soundtr.ogg')

# Size of the screen
SCREEN_TITLE = 'SoulMate'
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()

success = 15
song_end = 14
p = 0
m = 0
class Game:
 
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60
 
    # Initializer for the game class to set up the width, height, and title
    def __init__(self, image_path, image_path_2, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        
        # Create the window of specified size to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        
       
        self.game_screen.fill(WHITE_COLOR)
        # Give it a title.
        pygame.display.set_caption(title)
        # 
        background_image = pygame.image.load(image_path)
        background_image_2 = pygame.image.load(image_path_2)
        self.image2 = pygame.transform.scale(background_image_2, (width, height))
        self.image = pygame.transform.scale(background_image, (width, height))
        
    
        
 
    def run_game_loop(self):
        is_blackbird_over = False
        

                
        while not is_blackbird_over:
            
            mousex, mousey = pygame.mouse.get_pos()
            global song_end
            global success
            pygame.mixer.Channel(0).set_endevent(song_end)

            # call check if close under one function check_if_close which takes multiple if statements.
            # check if mouse is near select coordinates in screen 1 and 2 for bird songs to trigger.

            def check_if_close():
                global p
                global m
                if m == 0 and abs(mousex - 610) <= 4 and abs (mousey - 340) <= 5:
                    m = 1
                    BS1.play(loops = 0)
                    
                    hey = font.render("TEST", 0, BLACK_COLOR, True)
                    self.game_screen.blit(hey, (410, 400))
                elif p == 0 and abs(mousex - 120) <= 4 and abs(mousey - 470) <= 5:
                    p = 1
                    BS2.play(loops = 0)
                elif p == 0 and abs(mousex - 750) <= 4 and abs(mousey - 410) <= 5:
                    p = 1
                    BS3.play(loops = 0)
                elif p == 0 and abs(mousex - 570) <= 4 and abs(mousey - 20) <= 5:
                    p = 1
                    pygame.mixer.Channel(7).play(BS1, 0)
                    pygame.mixer.Channel(7).set_endevent(success)
                            
                elif p == 0 and abs(mousex - 1010) <= 4 and abs(mousey - 478) <= 5:
                    p = 1
                    BS4.play(loops = 0)
                else:
                    return
                    
                  

            
                
                
               
                
                    # Code for Text render(NOT WORKING)
                    #while pygame.mixer.get_busy() == True:
                        #text = font.render('This is my sound :)', True, BLACK_COLOR)
                        #self.game_screen.blit(text, (300, 350))
                    
               
        
                
            for event in pygame.event.get():
                global p
                if event.type == pygame.QUIT:
                    is_blackbird_over = True
                print(event)
                if event.type == song_end:
                    p = 0
                    self.image = self.image2
                elif event.type == success:

                    pygame.mixer.Channel(0).play(P1)
                    clock.tick(2)
                    pygame.mixer.Channel(1).play(P2)
                    clock.tick(2)
                    pygame.mixer.Channel(2).play(P3)
                    clock.tick(2)
                    pygame.mixer.Channel(3).play(P4)
                    clock.tick(2)
                    pygame.mixer.Channel(4).play(P5)
                    clock.tick(2)
                    pygame.mixer.Channel(5).play(P6)
                 
                
                    

        
                    
            
            check_if_close()
            
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))
            
            pygame.display.update()
            clock.tick(self.TICK_RATE)
        
    
         
        
    
        
            


        
pygame.init()
 
Soulmate = Game('./image_files/Blackbird.jpg', './image_files/Perfectpark.jpg', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
Soulmate.run_game_loop()

# Perfect_Park = Game('Perfectpark.jpg', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)


    
        

   
 
# Quit pygame and the program
pygame.quit()
quit()

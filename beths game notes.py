background_image = pygame.image.load('Blackbird.jpg')
background_image = pygame.transform.scale(background_image, (800, 800))
background_image2 = pygame.image.load('Perfectpark.jpg')
background_image2 = pygame.transform.scale(background_image, (800, 800))
                                                             
  # Beginnings of a star!
  # SO i want the points of the star to trigger a sound effect when mouse hovers over them.
  # I need to locate the 'points':

    # I realise of course the points correlate to the polygon x and y coordinates!
    # 2 triangles 3 points each so six sets of xy coordinates
p1_coord = (300, 150)
p2_coord = (400, 200)
p3_coord = (450, 350)
p4_coord = (350, 400)
p5_coord = (250, 350)
p6_coord = (250, 200)


# Our checks are made against this: Change this and change the code.
soundbank = [SP2, SP1, SP4, SP6, SP5, SP3]



# Creating a check to see if sounds were played in the correct order:
#If not: error sound. and reset counter. If correct: Print hurray print proptotype finished reset counter.

index = 0


def sound_check(order):
        global index
        if soundbank[index] == order:
                
                index += 1
                print(index)
                print(len(soundbank))
                
                if index == len(soundbank):
                    print('Hurray!')
                    print('Prototype finished')
                    index = 0

        else:
                ERR.play()
                index = 0
# My version square zone Trigger: 
# def button_trig():
       # if mousex >= buttonx and mousex <= buttonx + button_width and mousey >= buttony and mousey <= buttony + button_height:
                

#notes:
       # position of mid bird is 405, 340


        
song_end = 14

is_perfectpark = False
m = 0
while not is_blackbird_over:
        

        # Sammy's simple distance trigger!:   
        mousex, mousey = pygame.mouse.get_pos()

       
        
        def check_if_close(xcoord, ycoord):
                global m
                
                Song_end = 14
                if m == 1:
                        return
                
                elif m == 0 and abs(mousex - xcoord) <= 4 and abs(mousey - ycoord) <= 4:
                               
                                m = 1
                                BS1.play(loops = 0)
                                while pygame.mixer.get_busy():
                                        text = font.render('This is my sound :)', True, BLACK_COLOR)
                                        game_screen.blit(text, (300, 350))
                                        pygame.display.update()
                                        clock.tick(1)
                                         #5.121406078338623 BS1 length
                                        
                                        global song_end

                                        pygame.mixer.Channel(0).set_endevent(song_end)
                                        
                                                
                                        
                                        
                else:
                        return
                
                                        
                                       
                              
                       
                                
                                
                        
                
                
        
        check_if_close(405, 340)

        # a press down check.
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1 == True:
                print(mousex, mousey)
        def star_trigger(index):

        
                #if the mouse hover meets the x,y coord of the trigger points the sound plays
                if check_if_close(p1_coord[0], p1_coord[1]): #WIP not working as intended.
                    SP2.play()
                    sound_check(SP1)
                    
                elif pygame.mouse.get_pos() == p2_coord:
                    SP1.play()
                    sound_check(SP2)
                    
                elif pygame.mouse.get_pos() == p3_coord:
                    SP6.play()
                    sound_check(SP3)
                    
                elif pygame.mouse.get_pos() == p4_coord:
                    SP3.play()
                    sound_check(SP4)
                    
                elif pygame.mouse.get_pos() == p5_coord:
                    SP5.play()
                    sound_check(SP5)
                    
                elif pygame.mouse.get_pos() == p6_coord:
                    SP4.play()
                    sound_check(SP6)
                else:
                        return  

           #call upon our star trigger function: 
       # star_trigger(index)
        
       
        
       
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        is_blackird_over = True
                if event.type == song_end:
                        print('song ended')
                        is_blackbird_over = True
                        is_perfectpark = True
                        
        #pygame.draw.polygon(game_screen, BLACK_COLOR, [[350, 400], [250, 200], [400, 200]] )
       # pygame.draw.polygon(game_screen, BLACK_COLOR, [[450, 350], [300, 150], [250, 350]] )
       # pygame.draw.circle(game_screen, BLACK_COLOR, [300, 150], 8, 0)#Circle 1
        
        game_screen.blit(background_image, (0,0))
    
         

while is_perfectpark:
        

        for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        is_perfectpark = False
                     
                           
        

        game_screen.blit(background_image2, (0,0))
    
        pygame.display.update()

        clock.tick(TICK_RATE)
pygame.quit()
quit()


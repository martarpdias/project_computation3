#this is the file we need to change

import pygame
from utils import * # no need to import pygame because the import is in utils
from config import * # importing colors and the like

def interface():

    # initiating pygame
    pygame.init()
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    #fonts
    corbel_font = pygame.font.SysFont("Corbel", 50)
    comicsans_font = pygame.font.SysFont("Comic Sans MS", 50)

    #text
    #firts parameter is the text
    #second parameter is anti-aliasing, always True
    #third parameter is the color
    wilderness_text = corbel_font.render("Wilderness Explorer", True, white)
    rules_text = corbel_font.render("Rules", True, white)
    options_text = corbel_font.render("Options", True, white)
    credits_text = corbel_font.render("Credits", True, white)
    quit_text = corbel_font.render("Quit", True, white)
    title_text = comicsans_font.render("Computation III - Project", True, glowing_light_red)

    #main game loop
    while True:
        #event handling
        for ev in pygame.event.get():
            #quitting the game with the close button on the window (X)
            if ev.type == pygame.QUIT:
                pygame.quit()
                
            #detecting if the user clicked on the quit button (450, 600 t0 590, 660) 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450<=mouse[0]<=590 and 600<=mouse[1]<=660:
                    pygame.quit()

            #detecting if the user clicked on options button (90, 630 to 230, 660):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90<=mouse[0]<=230 and 600<=mouse[1]<=660:
                    under_construction()

            #detecting if the user clicked on the rules button (90, 480 to 230, 540):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90<=mouse[0]<=230 and 480<=mouse[1]<=540:
                    under_construction()

            #detecting if the user clicked on the wilderness explorer button (90, 240 to 630, 300):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90<=mouse[0]<=630 and 240<=mouse[1]<=300:
                    wilderness_explorer()

            #detecting if the user clicked on the credits button (450, 480 to 590, 540):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450<=mouse[0]<=590 and 480<=mouse[1]<=540:
                    credits_()




        #backgroud
        screen.fill(deep_black)

        #Bunch of things

        #get the mouse infomration
        mouse = pygame.mouse.get_pos() #locates where the mouse is

        #drawing the buttons

        #wilderness explorer button - apperance
        pygame.draw.rect(screen, dark_red, [90, 240, 540, 60]) #90 pixels from the left, 240 from the top, 540 width, 60 height
        #text - functionality
        wilderness_rect = wilderness_text.get_rect(center=(90 + 540//2, 240 + 60//2)) #use the floor divison, because half pixels don't exist
        #Writting
        screen.blit(wilderness_text, wilderness_rect)

        #rules button
        pygame.draw.rect(screen, grey, [90, 480, 140, 60])
        rules_rect = rules_text.get_rect(center=(90 + 140//2, 480 + 60//2))
        screen.blit(rules_text, rules_rect)

        #options button
        pygame.draw.rect(screen, grey, [90, 600, 140, 60])
        options_rect = options_text.get_rect(center=(90 + 140//2, 600 + 60//2))
        screen.blit(options_text, options_rect)

        #credits button
        pygame.draw.rect(screen, grey, [450, 480, 140, 60])
        credits_rect = credits_text.get_rect(center=(450 + 140//2, 480+ 60//2))
        screen.blit(credits_text, credits_rect)

        #quit button
        pygame.draw.rect(screen, grey, [450, 600, 140, 60])
        quit_rect = quit_text.get_rect(center=(450 + 140//2, 600 + 60//2))
        screen.blit(quit_text, quit_rect)

        #title
        screen.blit(title_text, (55, 0))


        #at the end
        pygame.display.update()





# Under construction screen
def under_construction():

    # creating the screen at 720x720 pixels - placeholder
    screen = pygame.display.set_mode(resolution)

    #fonts
    corbel_font = pygame.font.SysFont("Corbel", 50)
    conversation_font = pygame.font.SysFont("Arial", 30)

    #text
    back_text = corbel_font.render("    back", True, white)
    construction_text = corbel_font.render("Under Construction", True, white)

    #positions for the stick figures
    bob_x_position = 460
    bob_y_position = 450

    normal_x_position = 260
    normal_y_position = 450

    #main game loop
    while True:
        #mouse information
        mouse = pygame.mouse.get_pos()

        #check for events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    interface()

        #background
        screen.fill(deep_black)

        #display 'UNDER CONSTRUCTION' text
        construction_rect = construction_text.get_rect(center=(360, 300))
        screen.blit(construction_text, construction_rect)
            
        #draw a back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_rect = back_text.get_rect(center=(450 + 140//2, 600 + 60//2))
        screen.blit(back_text, back_rect)

        #stick figures
        draw_normal_stick_figure(screen, normal_x_position, normal_y_position)
        draw_stick_figure_with_hat(screen, bob_x_position, bob_y_position)

        #conversation
        normal_speech = conversation_font.render("Can we fix it?", True, white)
        bob_response = conversation_font.render("Probably not.", True, white)

        screen.blit(normal_speech, (normal_x_position - 60, normal_y_position - 80))
        screen.blit(bob_response, (bob_x_position - 60, bob_y_position - 80))

        #Update the screen
        pygame.display.update()

        

def credits_():
    screen = pygame.display.set_mode(resolution)

    #fonts
    comicsans_font = pygame.font.SysFont("Comic Sans MS", 25)
    corbel_font = pygame.font.SysFont("Corbel", 50)

    #text
    augusto = comicsans_font.render("Augusto Santos, ajrsantos@novaims.unl.pt", True, white)
    diogo = comicsans_font.render("Diogo Rasteiro, drasteiro@novaims.unl.pt", True, white)
    liah = comicsans_font.render("Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white)

    #main game loop
    while True:
        #mouse information
        mouse = pygame.mouse.get_pos()

        #check for events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    interface()

        #background
        screen.fill(deep_black)

        #display text
        screen.blit(augusto, (0,0))
        screen.blit(diogo, (0,25))
        screen.blit(liah, (0,50))

        #draw a back button [x, y, width, height]
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_text = corbel_font.render("    back", True, white)
        back_rect = back_text.get_rect(center=(450 + 140//2, 600 + 60//2))
        screen.blit(back_text, back_rect)

        #Update the screen
        pygame.display.update()

    


def rules_():
    print("Displaying rules...")


def wilderness_explorer():
    print("Wilderness Explorer Game Starting...")

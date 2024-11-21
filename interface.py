import pygame 
from utils import *
from config import *
from class_player import Player
from class_projectile import Projectile
from class_enemy import Enemy
from game import *



# Load images once to avoid reloading each frame
# Update the path to include the subfolder "game_project"
walkRight = [pygame.image.load(f'game_project/pics/R{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(f'game_project/pics/L{i}.png') for i in range(1, 10)]
backgroundPic = pygame.image.load('game_project/pics/bg.webp')
still = pygame.image.load('game_project/pics/standing.png')
clock = pygame.time.Clock()


# Initialize screen outside of function calls
pygame.init()
screen = pygame.display.set_mode((resolution))

def interface():
    global screen

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
    wilderness_text1 = corbel_font.render("Wilderness Explorer1", True, white)
    rules_text = corbel_font.render("Rules", True, white)
    options_text = corbel_font.render("Options", True, white)
    credits_text = corbel_font.render("Credits", True, white)
    quit_text = corbel_font.render("Quit", True, white)
    title_text = comicsans_font.render("Computation III - Project", True, glowing_light_red)

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

            #detecting if the user clicked on the game button (450, 480 to 590, 540):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90<=mouse[0]<=630 and 140<=mouse[1]<=300:
                    execute_game()

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


        #butao jogo
        pygame.draw.rect(screen, dark_red, [90, 140, 540, 60]) #90 pixels from the left, 240 from the top, 540 width, 60 height
        wilderness_rect = wilderness_text1.get_rect(center=(90 + 540//2, 140 + 60//2)) #use the floor divison, because half pixels don't exist
        screen.blit(wilderness_text1, wilderness_rect)


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


# Corrected wilderness_explorer function
# Corrected wilderness_explorer function
def wilderness_explorer():
    screen = pygame.display.set_mode(resolution)
    man = Player(300, 470, 64, 64, walkRight, walkLeft, still)
    goblin = Enemy(100, 475, 64, 64, 550)
    shoot_loop = 0
    running = True

    # Set up font outside the loop to avoid reloading it every frame
    corbel_font = pygame.font.SysFont("Corbel", 50)
    back_text = corbel_font.render("    back", True, white)
    back_rect = pygame.Rect(550, 600, 140, 60)

    bullets = []  # Define bullets array here and keep it persistent in wilderness_explorer

    while running:
        clock.tick(27)

        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 3:
            shoot_loop = 0

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return interface()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if back_rect.collidepoint(mouse):
                    return interface()

        for bullet in bullets:
            # Check if bullet hit goblin
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))

            if 0 < bullet.x < resolution[0]:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shoot_loop == 0:
            facing = 1 if man.right else -1
            if len(bullets) < 7:
                # Corrected Projectile initialization with both x and y correctly specified
                bullets.append(Projectile(man.x + man.width // 2, man.y + man.height // 2, 8, deep_black, facing))

            shoot_loop = 1

        if keys[pygame.K_LEFT] and man.x > man.distance:
            man.x -= man.distance
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < resolution[0] - man.width - man.distance:
            man.x += man.distance
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not man.jumpping:
            if keys[pygame.K_UP]:
                man.jumpping = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1 if man.jumpCount > 0 else -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.jumpping = False
                man.jumpCount = 10

        # Pass bullets to redrawGameWindow so they can be displayed
        redrawGameWindow(screen, man, goblin, bullets, back_text, back_rect)


# Updated redrawGameWindow to accept bullets
def redrawGameWindow(screen, man, goblin, bullets, back_text, back_rect):
    clock.tick(27)
    screen.blit(backgroundPic, (0, 0))
    man.draw(screen)
    goblin.draw(screen)

    # Draw each bullet in the bullets list
    for bullet in bullets:
        bullet.draw(screen)

    # Draw the "back" button
    pygame.draw.rect(screen, grey, back_rect)
    screen.blit(back_text, back_rect)

    pygame.display.update()

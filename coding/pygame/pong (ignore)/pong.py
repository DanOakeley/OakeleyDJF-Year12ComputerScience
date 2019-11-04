##--Functions
import pygame
import sys
#--Colour
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#initalise pygame
pygame.init()

#-- Blank Screen
display_width = 640
display_length = 480
size = (640,480)
screen = pygame.display.set_mode(size)
#--Title of new window/screen
pygame.display.set_caption("pong")
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
#declare variables
fontName = pygame.font.match_font('arial')
def PongDrawTextWhite (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def PongDrawTextBlack (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def Main_Menu():
    #Menu variables
    MainMenuDone = False
    Title = "Main Menu"
    MenuLine1 = "Pick an Option:"
    MenuLine2 = "Enter [1] To Start Pong"
    MenuLine3 = "Enter [2] To open Pong settings"
    MenuLine4 = "Enter [3] To Quit"
    P1Instructions1 = "Player 1 Controls:"
    P1Instructions2 = "[W] to move up"
    P1Instructions3 = "[S] to move down"
    P2Instructions1 = "Player 2 Controls:"
    P2Instructions2 = "[UP] to move up"
    P2Instructions3 = "[DOWN] to move down"
    #Menu loop
    while not MainMenuDone:
        for event in pygame.event.get():
            MainMenuDone = False
        #--Quit conditon if press ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                MainMenuDone = True
                Pong_Game()
           #endif
            if event.key == pygame.K_2:
               MainMenuDone = True
               Settings_Menu()
            #endif
            if event.key == pygame.K_3:
                MainMenuDone = True
            #endif
        #endif

        # -- Screen background is BLACK
        screen.fill (WHITE)
        # -- Draw here
        pygame.draw.rect(screen, YELLOW, (0,0,display_width,150))
        pygame.draw.rect(screen, BLUE, (430,270,300,250))
        PongDrawTextBlack(screen, str(Title), 50, 150, 50)
        PongDrawTextBlack(screen, str(MenuLine1), 20, 60, 170)
        PongDrawTextBlack(screen, str(MenuLine2), 20, 90, 220)
        PongDrawTextBlack(screen, str(MenuLine3), 20, 121, 240)
        PongDrawTextBlack(screen, str(MenuLine4), 20, 66, 260)
        PongDrawTextWhite(screen, str(P1Instructions1), 20, 520, 280)
        PongDrawTextWhite(screen, str(P1Instructions2), 20,561, 320)
        PongDrawTextWhite(screen, str(P1Instructions3), 20,570, 340)
        PongDrawTextWhite(screen, str(P2Instructions1), 20, 520, 380)
        PongDrawTextWhite(screen, str(P2Instructions2), 20, 525, 420)
        PongDrawTextWhite(screen, str(P2Instructions3), 20,550, 440)

#        drawText(screen, str(Leftscore), 18, 20, 10)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - e clock ticks over
        clock.tick(60)
    #End While

def Settings_Menu():
    #Menu variables
    MenuDone = False
    Title = "Settings Menu"
    Options1 = "Change Ball Speed:"
    Options2 = "Please pick a level for the ball speed"
    Options3 = "Enter [1] to set the dificity to easy"
    Options4 = "Enter [2] to set the dificity to medium"
    Options5 = "Enter [3] to set the dificity to hard"
    CloseText = "To close the menu press [ESC]"

    #Menu loop
    while not MenuDone:
        for event in pygame.event.get():
            MenuDone = False
        #--Quit conditon if press ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                MenuDone = True
           #endif
         #endif

        # -- Screen background is BLACK
        screen.fill (WHITE)
        # -- Draw here
        pygame.draw.rect(screen, YELLOW, (0,0,display_width,150))
        PongDrawTextBlack(screen, str(Title), 50, 150, 50)
        PongDrawTextBlack(screen, str(Options1), 20, 80, 150)
        PongDrawTextBlack(screen, str(Options2), 20, 140, 170)
        PongDrawTextBlack(screen, str(Options3), 20, 125, 220)
        PongDrawTextBlack(screen, str(Options4), 20, 137, 240)
        PongDrawTextBlack(screen, str(Options5), 20, 123, 260)
        PongDrawTextBlack(screen, str(CloseText), 20, 120, 450)

#        drawText(screen, str(Leftscore), 18, 20, 10)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - e clock ticks over
        clock.tick(60)
    #End While

def Pong_Game():
    #Game variables
    done = False
    x_val = 150
    y_val = 200
    x_direction = 5
    y_direction = 5
    ball_width = 20
    Leftpaddle_length = 15
    Leftpaddle_width = 60
    Leftx_padd = 0
    Lefty_padd = 20
    Lefty_offset=0
    Rightpaddle_length = 15
    Rightpaddle_width = 60
    Rightx_padd = 625
    Righty_padd = 20
    Righty_offset=0
    Leftscore = 0
    Rightscore = 0
    Totscore = Leftscore + Rightscore
    #Game loop
    while not done:
        # -- User input and controls
        for event in pygame.event.get():
            done = False

            #--Controls for paddles and quit condition
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                     Lefty_offset=-6
                elif event.key == pygame.K_s:
                     Lefty_offset=6
                elif event.key == pygame.K_UP:
                     Righty_offset = -6
                elif event.key == pygame.K_DOWN:
                     Righty_offset = 6
                elif event.key == pygame.K_ESCAPE:
                     done = True
                #End if
            elif event.type == pygame.KEYUP:
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    Lefty_offset = 0
                elif event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                    Righty_offset = 0
                #endif
            #endif
# -- Game logic goes after this comment

        #-paddle movement
        Lefty_padd = Lefty_padd + Lefty_offset
        Righty_padd = Righty_padd + Righty_offset
        x_val = x_val + x_direction
        y_val = y_val + y_direction

        #--ball direction
        if y_val == 480 - ball_width or y_val == 0:
            y_direction = y_direction * -1
        #endif

        #Left paddle collisions (with points added)
        if x_val < ball_width and y_val > Lefty_padd and y_val < Lefty_padd + Rightpaddle_width:
                x_direction *= -1
        else:
            if x_val == 0:#  and y_val != Lefty_padd:
                x_val = size[0] // 2
                y_val = size[1] // 2
                x_direction *= -1
                Rightscore = Rightscore + 1
            #Endif
        #Endif

        #Right paddle collisions (with points added)
        if x_val >= display_width - 20 - ball_width and y_val > Righty_padd and y_val < Righty_padd + Rightpaddle_width:
                x_direction *= -1
        else:
            if x_val > 640:
                x_val = size[0] // 2
                y_val = size[1] // 2
                x_direction *= -1
                Leftscore = Leftscore + 1
            #endif
        #endif

        #scoreboard
        if Leftscore == 11:
            done = True
        elif Rightscore == 11:
            done = True

        # -- Screen background is BLACK
        screen.fill (BLACK)
        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
        pygame.draw.rect(screen, WHITE, (Leftx_padd,Lefty_padd,Leftpaddle_length,Leftpaddle_width))
        pygame.draw.rect(screen, WHITE, (Rightx_padd,Righty_padd,Rightpaddle_length,Rightpaddle_width))
        PongDrawTextWhite(screen, str(Leftscore), 18, 20, 10)
        PongDrawTextWhite(screen, str(Rightscore), 18, 620, 10)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - e clock ticks over
        clock.tick(60)
    #End While - End of game loop

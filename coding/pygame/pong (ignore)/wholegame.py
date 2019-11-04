import pygame
import sys
import pong
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

def drawTextWhite (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def drawTextBlack (surf, text, size, x, y):
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
    MenuLine3 = "Enter [2]              "
    MenuLine4 = "Enter [3] To Quit"
    #Menu loop
    while not MainMenuDone:
        for event in pygame.event.get():
            MainMenuDone = False
        #--Quit conditon if press ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                MainMenuDone = True
                pong.Main_Menu()
           #endif
            if event.key == pygame.K_2:
               MainMenuDone = True
               #WIP
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
        drawTextBlack(screen, str(Title), 50, 150, 50)
        drawTextBlack(screen, str(MenuLine1), 20, 60, 170)
        drawTextBlack(screen, str(MenuLine2), 20, 90, 220)
        drawTextBlack(screen, str(MenuLine3), 20, 121, 240)
        drawTextBlack(screen, str(MenuLine4), 20, 66, 260)

#        drawText(screen, str(Leftscore), 18, 20, 10)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - e clock ticks over
        clock.tick(60)
    #End While

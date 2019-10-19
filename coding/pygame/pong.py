import pygame
import sys
#-- Global Constants

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
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
#declare variables
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
fontName = pygame.font.match_font('arial')

##--Functions
def drawText (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        done = False
#--Quit conditon if press ESC
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_ESCAPE:
#                done = True
           #endif
         #endif
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
#--Controls for Right paddle
#        if event.type == pygame.QUIT:
#            done = True
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_UP:
#                 Righty_offset=-6
#            elif event.key == pygame.K_DOWN:
#                 Righty_offset=6
            #End if
#        elif event.type == pygame.KEYUP:
#            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
#                Righty_offset = 0
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
    if x_val >= display_width - Rightpaddle_width and y_val >= Righty_padd - ball_width and y_val <= Righty_padd + Rightpaddle_length:
            x_direction *= -1
    else:
        if x_val > 640:
            x_val = size[0] // 2
            y_val = size[1] // 2
            x_direction *= -1
            Leftscore = Leftscore + 1
        #endif
    #endif
##--paddle collison (left)
#    if x_val <= 15 and y_val >= Lefty_padd-20 and y_val <= Lefty_padd+60:
#        x_direction = x_direction * -1
#    #endif
##--paddle collsion (right)
#    if x_val   <= 15 and y_val >= Righty_padd-20 and y_val <= Righty_padd+60:
#        x_direction = x_direction * -1
#    #endif
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

    drawText(screen, str(Leftscore), 18, 20, 10)
    drawText(screen, str(Rightscore), 18, 620, 10)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - e clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

import pygame
import math
import random
#varialbes
size = (640,480)
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

#--Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,0,0)
YELLOW = (255,255,0)

#initalise pygame
pygame.init()

#lists
theballs = []
newball = []
colourlist = [BLACK,WHITE,BLUE,RED,YELLOW]
numnew = 0

#classes
class Ball():
    # Constructor function to define initial state of a ball object
    def __init__(self, x, y, col,x_speed, y_speed, court):
        # --- Class Attributes ---
        #playarea size (square)
        self.court = court


        # Ball position
        self.x = x
        self.y = y

        # Ball's vector
        self.change_x = x_speed
        self.change_y = y_speed

        # Ball size
        self.size = 10

        # Ball colour
        self.color = col

    # --- Class Methods ---
    # Defines the the ball's movement
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x >= self.court[2] or self.x <= self.court[0]:
            self.change_x = self.change_x * -1
        if self.y >= self.court[3] or self.y <= self.court[1]:
            self.change_y = self.change_y * -1

    # Draws the ball on the screen
    def draw(self):
        pygame.draw.circle(screen,self.color, [self.x, self.y], self.size )
#main Game
done = False

#create the Balls
for counter in range(0,1):

    X = random.randint(1,700)
    Y = random.randint(1,400)
    SIZE = random.randint(5,25)
    Colour = random.choice(colourlist)
    xSpeed = random.randint(-10,10)
    ySpeed = random.randint(-10,10)
    Court = (random.randint(0,640),random.randint(0,480),random.randint(100,size[0]),random.randint(100,size[1]))
    theballs.append(Ball(X,Y,Colour,xSpeed,ySpeed,Court))


while not (done):
    RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #Clear the screen
    #screen.fill (BLACK)
    #Draw the ball on the screen and then move it
    for counter in range(0,1 + numnew):
        theballs[counter].draw()
        theballs[counter].move()

    #Spacebar to spawn new ball
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for counter in range(0,10):
                    Court = (random.randint(0,640),random.randint(0,480),random.randint(100,size[0]),random.randint(100,size[1]))
                    theballs.append(Ball(random.randint(1,700),random.randint(1,400),RANDOM,random.randint(-10,10),random.randint(-10,10),Court))
                    numnew = numnew + 1
            if event.key == pygame.K_p:
                done = True
#-- Blank Screen
#####################################
screen = pygame.display.set_mode(size)
#--Title of new window/screen
pygame.display.set_caption("My Window")
#done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop

    # -- flip display to reveal new position of objects
pygame.display.flip()
    # - The clock ticks over
clock.tick(60)
#End While - End of game loop
pygame.quit()

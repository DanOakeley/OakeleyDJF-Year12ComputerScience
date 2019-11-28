import pygame
import math
import random
# -- Global constants


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Snow")

# -- Classes
class Snow(pygame.sprite.Sprite):
# Define the constructor for snow
    def __init__(self, color, width, height, speed):
        #set the speed of Sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 400)
    def update(self):
        self.rect.y = self.rect.y + self.speed

#--lists
snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

#Create snowflakes
number_of_flakes = 50
for x in range (number_of_flakes):
    my_snow = Snow(WHITE,5,5,1)
    snow_group.add (my_snow)
    all_sprites_group.add (my_snow)
#next x
# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()


# -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #nextevent

    # -- Game logic goes after this comment
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw (screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

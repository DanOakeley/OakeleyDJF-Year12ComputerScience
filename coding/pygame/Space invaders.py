import pygame
import math
import random
# -- Global constants


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,50,50)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")

# -- Classes
class Invader(pygame.sprite.Sprite):
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

class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        #set the speed of Sprite
        self.speed = 0
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 470
        self.lives = 5
        self.bullet_count = 50
    def update(self):
        self.rect.x = self.rect.x + self.speed
    def player_set_speed(self,val):
        self.speed = val

class Bullet(pygame.sprite.Sprite):
    def __init__(self,color,speed):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = 2

        self.speed = speed
    def update():
        self.rect.y = self.rect.y - self.speed
#--lists
invader_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bullet_hit_group = pygame.sprite.Group()


#Create invaders
number_of_invaders = 10
for x in range (number_of_invaders):
    my_invader = Invader(BLUE,5,5,1)
    invader_group.add (my_invader)
    all_sprites_group.add (my_invader)
#next x

#Create the Player
player = Player(YELLOW,10,10)
all_sprites_group.add (player)
# -- Exit game flag set to false
done = False

#Create the bullets

# --Manages how fast screen refreshes
clock = pygame.time.Clock()


# -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.bullet_count = player.bullet_count – 1
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        #endif
    #nextevent

    # -- Game logic goes after this comment
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for foo in player_hit_group:
        player.lives = player.lives - 1

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

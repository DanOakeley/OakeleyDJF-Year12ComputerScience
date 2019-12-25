import pygame
# -- Global constants

#--map
map = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]

# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#classes

class tile(pygame.sprite.Sprite):
    #define the constructor for invader
    def __init__(self,color,width,height,x_ref,y_ref):
        #call the super constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref

class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height,speed):
        #call the super consturctor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("grover_face.png")
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        #set the position fof the player attributes
        self.rect.x = 20
        self.rect.y = 20

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def player_set_speed_x(self,val):
        self.speed_x = val
    def player_set_speed_y(self,val):
        self.speed_y = val


#create a list of all sprites
all_sprites_list = pygame.sprite.Group()

#create a lsit of tiles for the walls
wall_list = pygame.sprite.Group()

#create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range(10):
        if map[x][y] == 1:
            my_wall = tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
#create the player
pacman = Player(YELLOW, 15, 15, 20)
all_sprites_list.add(pacman)
# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.player_set_speed_x(-2)
            elif event.key == pygame.K_RIGHT:
                pacman.player_set_speed_x(2)
            if event.key == pygame.K_UP:
                pacman.player_set_speed_y(-2)
            elif event.key == pygame.K_DOWN:
                pacman.player_set_speed_y(2)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pacman.player_set_speed_x(0)
                pacman.player_set_speed_y(0)
        #endif
    #nextevent

    # -- Game logic goes after this comment
    all_sprites_list.update()
    # -- Check for collisions between pacman and wall tiles
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)


    for foo in player_hit_list:
        pacman.player_set_speed_x(0)
        pacman.player_set_speed_y(0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y

    # Run the update function for all sprites
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    all_sprites_list.update()

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

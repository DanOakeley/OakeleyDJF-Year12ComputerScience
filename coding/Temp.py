import pygame
#-- Global Constants

#--Colour
black = (0,0,0)
white = (255,255,255)
blue = (50,50,50)
yellow = (255,255,0)

#initalise pygame
pygame.init()

#-- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
#--Title of new window/screen
pygame.display.set_caption("My Window")
#done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

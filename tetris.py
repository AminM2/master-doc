import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 1000

pygame.init()
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.display.update()

# Window doesn't close on Windows
# - Perhaps needs a clock?
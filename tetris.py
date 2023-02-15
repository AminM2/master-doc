import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 500
WINDOWHEIGHT = 750

pygame.init()
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
import pygame, sys

pygame.init()
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((1000,600))
running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running= False

    pygame.Display.update()
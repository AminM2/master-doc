import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 500
WINDOWHEIGHT = 750

TEAL = (99, 252, 255)
BLUE = (2, 11, 245)
ORANGE = (245, 153, 5)
YELLOW = (250, 234, 5)
GREEN = (25, 222, 18)
PURPLE = (136, 22, 201)
RED = (245, 17, 17)

pygame.init()
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
running = True

#THIS IS PEACESIZE
SQUARE = 25

def drawBoard():
  k = 0
  c = SQUARE
  l = 0
  o = -1
  p = 2
  p2 = 1
  for i in range(1,264):
    if i%12 == 0:
      l += SQUARE
      c = o*SQUARE*p
      k = -o*SQUARE*p2
      o = o * -1
      if p == 2:
        p = 1
        p2 = 2
        pygame.draw.rect(window,"gray",(SQUARE+100,l+100,SQUARE,SQUARE))
      elif p == 1:
        p = 2
        p2 = 1
        pygame.draw.rect(window,"darkgray",(SQUARE+100,l+100,SQUARE,SQUARE))
    if (i%2 == 0):
      k += SQUARE*2
      pygame.draw.rect(window,"gray",(k+100,l+100,SQUARE,SQUARE))
    elif i == 1:
      pygame.draw.rect(window,"gray",(100,100,SQUARE,SQUARE))
      pygame.draw.rect(window,"darkgray",(c+100,100,SQUARE,SQUARE))
    elif i%2 == 1:
      c += SQUARE*2
      pygame.draw.rect(window,"darkgray",(c+100,l+100,SQUARE,SQUARE))
  pygame.draw.rect(window,"black",(SQUARE+100,SQUARE+100,SQUARE*10,SQUARE*20))
  pygame.draw.rect(window,"black",(425,125,SQUARE,SQUARE*21))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawBoard()
    pygame.display.update()


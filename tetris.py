import pygame, sys

WINDOWWIDTH = 600
WINDOWHEIGHT = 1000

pygame.init()
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
running = True

square = 20

def drawBoard():
  k = 0
  c = square
  l = 0
  o = -1
  p = 2
  p2 = 1
  for i in range(1,240):
    if i%12 == 0:
      l += square
      c = o*square*p
      k = -o*square*p2
      o = o * -1
      if p == 2:
        p = 1
        p2 = 2
        pygame.draw.rect(window,"gray",(square,l,square,square))
      elif p == 1:
        p = 2
        p2 = 1
        pygame.draw.rect(window,"darkgray",(square,l,square,square))
    if (i%2 == 0):
      k += square*2
      pygame.draw.rect(window,"gray",(k+0,l,square,square))
    elif i == 1:
      pygame.draw.rect(window,"gray",(0,0,square,square))
      pygame.draw.rect(window,"darkgray",(c+0,0,square,square))
    elif i%2 == 1:
      c += square*2
      pygame.draw.rect(window,"darkgray",(c+0,l,square,square))
  pygame.draw.rect(window,"black",(square,square,square*10,square*18))


while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    drawBoard()
    pygame.display.update()


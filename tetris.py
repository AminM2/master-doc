import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 500
WINDOWHEIGHT = 750
STARTBUTTONWIDTH = 150
STARTBUTTONHEIGHT = 75
TEXTSIZE = 60
SQUARE = 25
#Piece size ^

TEAL = (99, 252, 255)
BLUE = (2, 11, 245)
ORANGE = (245, 153, 5)
YELLOW = (250, 234, 5)
GREEN = (25, 222, 18)
PURPLE = (136, 22, 201)
RED = (245, 17, 17)
PINK = (245, 0, 167)
DARKPINK = (92, 0, 63)

pregame = True

startText = "Start"

pygame.init()
fontObject = pygame.freetype.SysFont("arial.ttf", TEXTSIZE)
pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
running = True

startButtonRect = pygame.Rect((WINDOWWIDTH/2)-(STARTBUTTONWIDTH/2), WINDOWHEIGHT/2, STARTBUTTONWIDTH, STARTBUTTONHEIGHT)


def drawStartButton():
    global fontObject, startText
    pygame.draw.rect(window, PINK, startButtonRect)
    boundingBox = fontObject.get_rect(startText, size=TEXTSIZE)
    fontObject.render_to(window, (startButtonRect.x + (startButtonRect.w - boundingBox.w)/2, startButtonRect.y + (startButtonRect.h - boundingBox.h)/2), startText, DARKPINK)

def startGame():
    global pregame
    if pregame and startButtonRect.collidepoint(mousePos):
        pregame = False

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
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos
            startGame()
        
    
    drawBoard()
    if pregame:
        drawStartButton()

    if not pregame:
        None
        # Write game loop code here
    
    pygame.display.update()



#vars
square = 20
#I sware to god if i lose sync one more bloody time

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
        pygame.draw.rect(screen,"gray",(square,l,square,square))
      elif p == 1:
        p = 2
        p2 = 1
        pygame.draw.rect(screen,"darkgray",(square,l,square,square))
    if (i%2 == 0):
      k += square*2
      pygame.draw.rect(screen,"gray",(k+0,l,square,square))
    elif i == 1:
      pygame.draw.rect(screen,"gray",(0,0,square,square))
      pygame.draw.rect(screen,"darkgray",(c+0,0,square,square))
    elif i%2 == 1:
      c += square*2
      pygame.draw.rect(screen,"darkgray",(c+0,l,square,square))
  pygame.draw.rect(screen,"black",(square,square,square*10,square*18))




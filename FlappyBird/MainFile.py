import pygame
import random

pygame.init()
gameScreen = pygame.display.set_mode((900, 600))
gameTitle = pygame.display.set_caption("Space Shooter")

#Surface
block = pygame.Surface((100, 200))

#Player
player = pygame.image.load('image/player.png').convert_alpha()
#Star
star  = pygame.image.load('image/star.png').convert_alpha()
#Star random
x = random.randint(0, 900)
y = random.randint(0, 600)

fps = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#BAckground
    gameScreen.fill('gray29')
#PLayer
    gameScreen.blit(player, (100, 100))
#Star
    gameScreen.blit(star, (x, y))





    pygame.display.update()
   
    #FPS
    fps.tick(60)

pygame.quit()            
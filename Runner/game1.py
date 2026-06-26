import pygame   
from sys import exit

def Score():
    time = int(pygame.time.get_ticks() / 1000) - start_time
    scoreBg = text_write.render(F'Score : {time}', False, "Black" )
    score_rect = scoreBg.get_rect(center = (250, 90))
    screen.blit(scoreBg, score_rect)
    return time

pygame.init()
screen = pygame.display.set_mode((507 ,320))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

gravity = 0
game_active = False
start_time = 0
score1 = 0

text_write = pygame.font.Font(None, 30)
gameNameBg = text_write.render('Welcome to the Runner Game', False , 'Black')
gameName_rect = gameNameBg.get_rect(center = (248, 50))


skyBg = pygame.image.load('GAME/Runner/gameBg/sky.webp').convert()
ground = pygame.image.load('GAME/Runner/gameBg/groundBg.webp').convert()

hero = pygame.image.load('GAME/Runner/chBg/hero.png').convert_alpha()
heroSm = pygame.transform.scale(hero, (30, 50))
heroSm_rect = heroSm.get_rect(bottomleft = (30, 270))

vill = pygame.image.load('GAME/Runner/chBg/vil.png').convert_alpha()
villSm = pygame.transform.scale(vill, (30, 50))
villSm_rect = villSm.get_rect(bottomleft = (400 , 270))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heroSm_rect.collidepoint(event.pos):
                    if heroSm_rect.bottom == 270:
                        gravity = -15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                    if heroSm_rect.bottom == 270:
                        gravity = -15
                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    heroSm_rect.x -= 14

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    heroSm_rect.x += 14   

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True        
                    villSm_rect.x = 507
                    heroSm_rect.x = 20
                    start_time = int(pygame.time.get_ticks()/1000)

    if game_active:    
        screen.blit(ground, (0,-95))  
        screen.blit(skyBg, (0,0))      

        score1 = Score()

        screen.blit(gameNameBg, gameName_rect)
        Score()

        screen.blit(heroSm, heroSm_rect)
    
        if heroSm_rect.left >= 507: heroSm_rect.right = 0 
        gravity += 1
        heroSm_rect.y += gravity
        if heroSm_rect.bottom >=270: heroSm_rect.bottom = 270


        screen.blit(villSm, villSm_rect)
        villSm_rect.x -= 3
        if villSm_rect.x <= 0:
            villSm_rect.x = 507

        if heroSm_rect.colliderect(villSm_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))        
        End_text = pygame.font.Font(None, 30)
        restart_text = pygame.font.Font(None, 30)
        ending = End_text.render("Pixel Runner", False, (111, 196,169) )
        end_restart = restart_text.render("Press SPACE to Start the Game", False, (111, 196,169) )
        screen.blit(ending, (200, 50))

        scoreNum = text_write.render(f"Score : {score1}", False, (111, 196, 169))


        if score1 == 0:
            screen.blit(end_restart, (100, 260))
        else:
            screen.blit(scoreNum, (210, 260))
        
        Logo = pygame.image.load("GAME/Runner/chBg/hero.png").convert_alpha()
        logoSm = pygame.transform.scale(Logo, (50, 80))
        logo1 = logoSm.get_rect(center = (250, 170) )
        screen.blit(logoSm, logo1)






    pygame.display.update()
    clock.tick(60)
#imports e inicialização
import pygame, sys, time
import random
from pygame.locals import *
pygame.init()

#janela display e imagens
largura_janela = 550
altura_janela = 550
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
VEL = 5

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'


mainClock = pygame.time.Clock()
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo Do Monstro")

chao = pygame.image.load('green.jpg').convert()

#caracteristicas monstro
MOVESPEED_monstro = 5

x = 10
y = 10
width = 40
height = 40
vel=10
player_rect = pygame.Rect(x,y,width,height)

pit1= pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44)
pit2= pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44)
pit3= pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44)
pit4= pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44)
pit5= pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44)

ouro = pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),20, 20)

porta = pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),50, 50)

b1 = {'rect':pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44), 'color':GREEN, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(random.randint(0,largura_janela),random.randint(0,altura_janela),44, 44), 'color':GREEN, 'dir':DOWNRIGHT}
boxes = [b1, b2]

font = pygame.font.SysFont(None, 48)

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

gold = False
done = True
while True:
    UP = True
    moveLeft = moveRight = moveUp = moveDown = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == KEYDOWN:
            if event.key == K_z:
                reverseCheat = True
            if event.key == K_x:
                slowCheat = True
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_z:
                reverseCheat = False
                score = 0
            if event.key == K_x:
                slowCheat = False
                score = 0
            if event.key == K_ESCAPE:
                terminate()

            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False

    if moveLeft and player_rect.left > 0:
        player_rect.move_ip(-1 * vel, 0)
    if moveRight and player_rect.right < largura_janela:
        player_rect.move_ip(vel, 0)
    if moveUp and player_rect.top > 0:
        if UP == True:
            player_rect.move_ip(0, -1 * vel)
    if moveDown and player_rect.bottom < altura_janela:
        player_rect.move_ip(0, vel)


    janela.blit(chao, (0, 0))
    jogador1 = pygame.draw.rect(janela, RED, player_rect)
    poco1 = pygame.draw.rect(janela, BLUE, pit1)
    poco2 = pygame.draw.rect(janela, BLUE, pit2)
    poco3 = pygame.draw.rect(janela, BLUE, pit3)
    poco4 = pygame.draw.rect(janela, BLUE, pit4)
    poco5 = pygame.draw.rect(janela, BLUE, pit5)

    ouro1 = pygame.draw.rect(janela, YELLOW, ouro)

    pygame.draw.rect(janela, b1['color'], b1['rect'])
    pygame.draw.rect(janela, b2['color'], b2['rect'])

    porta1 =pygame.draw.rect(janela,(91,51,15), porta)

    pygame.display.update()
    time.sleep(0.024)

    if player_rect.colliderect(b1['rect']) or player_rect.colliderect(b2['rect']):
        drawText('Oh não o monstro comeu-te', font, janela, (largura_janela / 3 - 100), (altura_janela / 3))
        pygame.display.update()
        time.sleep(5)
        break

    if player_rect.colliderect(pit1)or player_rect.colliderect(pit2)or player_rect.colliderect(pit3)or player_rect.colliderect(pit4)or player_rect.colliderect(pit5):
        drawText('Oh não caíste no poço', font, janela, (largura_janela / 3-100), (altura_janela / 3))
        pygame.display.update()
        time.sleep(3)
        break
    if gold == False:
        if player_rect.colliderect(ouro):
            gold = True
            drawText('Tens o ouro agora foge até à porta', font, janela, (largura_janela / 3 - 175), (altura_janela / 3))
            pygame.display.update()


    if player_rect.colliderect(porta):
        if gold == True:
            drawText('Ganhaste Parabéns', font, janela, (largura_janela / 3 - 100),(altura_janela / 3))
            pygame.display.update()
            time.sleep(3)
            break
        else:
            drawText('Não te esqueças do ouro', font, janela, (largura_janela / 3 - 100), (altura_janela / 3))
            pygame.display.update()

    for b in boxes:
        # Move the box data structure.
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED_monstro
            b['rect'].top += MOVESPEED_monstro
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED_monstro
            b['rect'].top += MOVESPEED_monstro
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED_monstro
            b['rect'].top -= MOVESPEED_monstro
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED_monstro
            b['rect'].top -= MOVESPEED_monstro

        # Check whether the box has moved out of the window.
        if b['rect'].top < 0:
            # The box has moved past the top.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > altura_janela:
            # The box has moved past the bottom.
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # The box has moved past the left side.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > largura_janela:
            # The box has moved past the right side.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
    pygame.time.delay(30)


pygame.quit()

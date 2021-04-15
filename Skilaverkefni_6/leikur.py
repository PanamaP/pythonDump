# Elfar Snær Arnarson
# 06 april 2020
# Skilaverkefni 6


from dicethrower import DiceThrower, Dice
import pygame
from pygame.locals import *
from pygame.locals import \
    (
    K_ESCAPE,
    QUIT,
)

pygame.init()

window_size = window_width, window_height = 640, 480
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Timaverkefni 3")

teningur = [pygame.image.load('myndir/sd0.png'),
            pygame.image.load('myndir/sd1.png'),
            pygame.image.load('myndir/sd2.png'),
            pygame.image.load('myndir/sd3.png'),
            pygame.image.load('myndir/sd4.png'),
            pygame.image.load('myndir/sd5.png'),
            pygame.image.load('myndir/sd6.png')]

tolvaKast = DiceThrower()
spilariKast = DiceThrower()
eittKast = Dice()

tolva_teningar = [0, 0]
spilari_teningar = [0, 0, 0]

font = pygame.font.Font(pygame.font.get_default_font(), 25)

spilaTexti = font.render("Spila", 1, (255, 255, 255))
spilaTakki = Rect(30, 300, 80, 30)

haldaStigumTexti = font.render("Halda Stigum", 1, (255, 255, 255))
haldaStigumTakki = Rect(470, 300, 170, 30)

kastaAfturTexti = font.render("Kasta Aftur", 1, (255, 255, 255))
kastaAfturTakki = Rect(250, 300, 145, 30)

nidurstadaTexti = font.render("test", 1, (10, 10, 10))
nidurstadaTextaKassi = Rect(10, 400, 400, 30)

game = False
gameOver = False
tolurVal = False
tolulisti = False
teljari = 0


def EndGame(tolvuTeningur, spilariTeningur):
    nidurstada = "Tölvan: " + str(sum(tolvuTeningur)) + " Spilari: " + str(sum(spilariTeningur)) + ". "
    if sum(tolvuTeningur) > sum(spilariTeningur):
        nidurstada += "Ég vann."
    elif sum(tolvuTeningur) < sum(spilariTeningur):
        nidurstada += "Þú vannst.."
    else:
        nidurstada += "Jafntefli."
    return nidurstada


listiYfirX = []
leikur = True
while leikur:
    if tolulisti:
        listiYfirX = []
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                leikur = False
        elif event.type == pygame.QUIT:
            leikur = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and spilaTakki.collidepoint(event.pos):
            if game == False:
                spilari_teningar = spilariKast.throw()
                tolva_teningar = tolvaKast.throw()
                gameOver = False
                nidurstadaTexti = font.render("", 1, (10, 10, 10))
                teljari = 0
            game = True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and haldaStigumTakki.collidepoint(event.pos) \
                and game:
            gameOver = True
            nidurstadaTexti = font.render('leikmaður heldur stigum, leiklokið', 1, (10, 10, 10))
            game = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and kastaAfturTakki.collidepoint(event.pos) \
                and game:
            if teljari != 2:
                if tolurVal:
                    for x in listiYfirX:
                        if x <= 1:
                            tolva_teningar[x] = eittKast.throw()
                            screen.blit(teningur[tolva_teningar[x]], ((x * 100 + 220), 100))
                            pygame.display.update()
                        elif x >= 2:
                            spilari_teningar[x - 2] = eittKast.throw()
                            screen.blit(teningur[spilari_teningar[x - 2]], ((x - 2 * 100 + 180), 100))
                            pygame.display.update()
                teljari += 1
                print(listiYfirX)
                listiYfirX = []
            else:
                print("Þú hefur kastað tvisvar sinnum.")
                gameOver = True
                nidurstadaTexti = font.render('Þú hefur kastað tvisvar sinnum, Leiklokið', 1, (10, 10, 10))
                game = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game:
            for x in range(len(listi)):
                if listi[x].collidepoint(event.pos):
                    listiYfirX.append(x)
                    print(listi[x], x)
            tolurVal = True

    screen.fill((255, 255, 255))

    listi = []
    # Teikna teninga
    for i in range(0, 2):
        listi.append(screen.blit(teningur[tolva_teningar[i]], ((i * 110 + 220), 10)))
    for i in range(0, 3):
        listi.append(screen.blit(teningur[spilari_teningar[i]], ((i * 110 + 180), 120)))

    pygame.draw.rect(screen, (0, 0, 255), spilaTakki)
    screen.blit(spilaTexti, spilaTakki)

    pygame.draw.rect(screen, (0, 0, 255), haldaStigumTakki)
    screen.blit(haldaStigumTexti, haldaStigumTakki)

    pygame.draw.rect(screen, (0, 0, 255), kastaAfturTakki)
    screen.blit(kastaAfturTexti, kastaAfturTakki)

    if gameOver:
        screen.blit(nidurstadaTexti, nidurstadaTextaKassi)

    pygame.display.update()

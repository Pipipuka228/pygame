import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
RAZMER_DOMA = 250

# цвета выбраны с сайта: https://htmlcolorcodes.com/
GOLYBOI = (0, 255, 255)
ZELENI = (0, 255, 0)
BORDOVI = (136, 0, 21)
SERI = (127, 127, 127)
BELI = (255, 255, 255)
JELTI = (255,255, 0)
JERNI = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(GOLYBOI)  # заливка фона
pg.display.set_caption("Игра")
clock = pg.time.Clock()

#trava
pg.draw.rect(screen, ZELENI, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
#dom
pg.draw.rect(screen, BORDOVI, (WIDTH // 8, HEIGHT // 3 , RAZMER_DOMA, RAZMER_DOMA))
#krisha doma
pg.draw.polygon(screen, SERI,
                [[WIDTH // 8, HEIGHT // 3], [WIDTH // 8 + RAZMER_DOMA, HEIGHT // 3],
                 [WIDTH // 8 + RAZMER_DOMA // 2, HEIGHT // 3 - 90]])
#okno
pg.draw.circle(screen, BELI, (WIDTH // 8 + RAZMER_DOMA // 2, HEIGHT // 3 + RAZMER_DOMA // 2), 50)
#rama okna
pg.draw.circle(screen, JERNI, (WIDTH // 8 + RAZMER_DOMA // 2, HEIGHT // 3 + RAZMER_DOMA // 2), 50, 10)
#son
pg.draw.circle(screen, JELTI, (WIDTH, 0),150)
#lychi son
pg.draw.line(screen, JELTI, [830, 20], [700, 20], 5)
pg.draw.line(screen, JELTI, [900, HEIGHT // 4 - 20], [780, 250], 5)
pg.draw.line(screen, JELTI, [WIDTH - 20, 160], [WIDTH - 20, 300], 5)

# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()

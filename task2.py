import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

a = 50
x = 0
y = WIN_HEIGHT // 2 - a//2
speed = 2

pg.draw.rect(screen, ORANGE, (x, y, a, a))  # рисуем круг
pg.display.update()  # обновляем окно

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

    if x >= WIN_WIDTH - a: #kasaetsa pravoi stenki
        speed = -speed
        speed -= 1.5
        if speed < -100:
            speed = -100
    elif x < 0: #kasaetsa levoi stenki
        speed = -speed
        speed += 1.5
        if speed > 100:
            speed = 100
    x += speed

    screen.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.rect(screen, ORANGE, (x, y, a, a))

    pg.display.update()  # обновляем окно

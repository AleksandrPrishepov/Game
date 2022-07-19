import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    """обработка нажатий клавиш"""
    for event in pygame.event.get():  # перебираем события в игре (действия)
        if event.type == pygame.QUIT:  # если тип события == закрыть
            sys.exit()  # закрываем
        elif event.type == pygame.KEYDOWN:  # если тип события (event.type) это нажатая клавиша (pygame.KEYDOWN)
            if event.key == pygame.K_RIGHT:  # если клавиша нашего события (event.key) и указваем клавишу (pygame.K_RIGHT) стрелка вправо
                gun.mright = True  # если тру значит будет выполняться метод update_gun с модуля gun
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:  # при нажатии на пробел
                new_bullet = Bullet(screen, gun)  # создается объект класса Bullet - пуля
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:  # если тип события (event.type) это клавиша отжата (pygame.KEYUP)
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)  # screen это наш графический, заливаем его черным цветом
    sc.show_score()
    for bullet in bullets.sprites():  # после каждого пробела появляется пулька и перемещается в bulets, в цикле берется каждая созданная пулька и прорисовывается
        bullet.draw_bullet()  # прорисовывается каждая пулька
    gun.output()  # blit отрисовывает объект на фоне экрана
    inos.draw(screen)  # blit отрисовывает объект на фоне экрана, прорисовка группы пришельцев
    pygame.display.flip()  # прорисовываем последний экран, после окончания игры

def update_bullets(screen, stats, sc, inos, bullets):
    """обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # удаляем пулю которая вышла за пределы экрана
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)  # при контакте пуль и пришельцев оба исчезают, если True и True оба исчезают, если False и True, то исчезает только один объект(создается словарь)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)  # меняется рекорд
        sc.image_guns()
    if len(inos) == 0:  # если все пришельцы закончились
        bullets.empty()  # очищаем все пули
        create_army(screen, inos)  # создаем новую армию

def gun_kill(stats, screen, sc, gun, inos, bullets):
    """столкновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1  # при столкновении отнимается одна жизнь
        sc.image_guns()
        inos.empty()  # очищается экран от всех пришельцев
        bullets.empty()  # очищается экран от всех пуль
        create_army(screen, inos)  # создаем армию пришельцев заново
        gun.create_gun()  # ставим пушку в центр, после столкновения
        time.sleep(1)  # перезагрузка 1 секунды
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, gun, inos, bullets):
    """обновляет позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):  # при столкновении пушки с инопланетянами игра обновляется
        gun_kill(stats, screen, sc,  gun, inos, bullets)  # игра обновляется
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc,gun, inos, bullets):
    """проверка, добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)  # игра обновляется
            break

def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)  # создание одного пришельца
    ino_width = ino.rect.width  # узнаем ширину нашего пришельца (ширина rect(прямоугольника))
    number_ino_x = int((700 - 2 * ino_width) / ino_width) # узнаем количество пришельцев в один ряд нашего экрана
    ino_height = ino.rect.height  # узнаем высоту пришельца (высота rect(прямоугольника))
    number_ino_y = int((800 - 150 - 2 * ino_height) / ino_height)  # узнаем количество строк пришельцев на экране

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):  # в цикл подставляем это количество, чтобы поэтапно заполнился весь ряд пришельцами
            ino = Ino(screen)  # создаем пришельца
            ino.x = ino_width + (ino_width * ino_number)  # показывает поэтапное заполнение ширины (нахождения х) каждого нового пришельца
            ino.y = ino_height + (ino_height * row_number)  # показывает поэтапное заполнение длинны (нахождения у) каждого нового пришельца
            ino.rect.x = ino.x # положение пришельца по оси х
            ino.rect.y = ino.y  # положение пришельца по оси у
            inos.add(ino)  # добавляем пришельцев в контейнер (inoplanats = Group())

def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
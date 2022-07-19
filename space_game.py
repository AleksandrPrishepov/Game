import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()   # инициализируем игру
    screen = pygame.display.set_mode((700, 800))  # создаем экран указываем его размер
    pygame.display.set_caption("Космические защитники")  # название экрана
    bg_color = (0, 0, 0)  # переменная с черным цветом
    gun = Gun(screen)  # создана пушка
    bullets = Group()  # контейнер в который будут собираться пульки созданные при нажатии пробел и отправленные в  этот контейнер
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:  # с помощью этого цикла происходят действия в игре
        controls.events(screen, gun, bullets)  # перекидываем все события, которые призойдут, через модуль control, с помощью функции, которая там нвходится event
        if stats.run_game:
            gun.update_gun()  # двигаем нашу пушку, определяем координаты нашего объекта
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)  # обновление экрана
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

run()
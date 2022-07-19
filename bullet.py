import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю"""
        super(Bullet, self).__init__()
        self.screen = screen  # загрузили экран где будут отображаться пули
        self.rect = pygame.Rect(0, 0, 2, 12)  # создаем пулю в виде прямоугольника, создаем объект класса Rect
        self.color = 139, 195, 74  # красим пулю в цвет
        self.speed = 4.5  # шаг нашей пули на оси у
        self.rect.centerx = gun.rect.centerx  # установления место пули, там где центр пушки
        self.rect.top = gun.rect.top  # верхняя точка пули там где верхняя точка пушки
        self.y = float(self.rect.y)  # определяем тип значения у как вещественное и начало координаты у от куда пуля будет лететь

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed  # движение координаты у (пули) вверх
        self.rect.y = self.y  # обновляем координату у

    def draw_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
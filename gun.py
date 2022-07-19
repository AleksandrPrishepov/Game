import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen  # экран на катором будет наша пушка
        self.image = pygame.image.load('images/gun.png')  # в переменную загрузили файл с изображением
        self.rect = self.image.get_rect()  # получакм нашу пушку(картинку) как прямоугольник
        self.screen_rect = screen.get_rect()  # получакм нашу экран как прямоугольник
        self.rect.centerx = self.screen_rect.centerx  # centrx ищет центр координат нашего объета, здесь мы сравниваем центр координат нашей пушки и экрана
        self.center = float(self.rect.centerx)  # rect.centerx этим методом мы находим координату, по умолчании они всегда целочисленные, здесь мы делаем их (координаты) вещественными
        self.rect.bottom = self.screen_rect.bottom  # координата низа пушки
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)  # blit отобразили объект на фоне экрана

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5  # координата нашей пушки найденная п методу (rect.centerx) идет по оси х вправо
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5  # координата нашей пушки найденная п методу (rect.centerx) идет по оси х влево
        self.rect.centerx = self.center

    def create_gun(self):
        """размещение пушки по центру внизу экрана"""
        self.center = self.screen_rect.centerx
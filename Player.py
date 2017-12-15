import pygame as pg
from settings import *
import os

vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

player_img = pg.image.load(os.path.join(img_folder, 'Player.png'))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0.2)

    def update(self):
        self.vel += self.acc

        if self.rect.bottom > HEIGHT:
            self.pos.y = HEIGHT
            self.acc.y = 0
            self.vel.y = 0

        self.pos += self.vel
        self.rect.midbottom = self.pos

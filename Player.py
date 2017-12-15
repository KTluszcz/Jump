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
        self.move()

    def move(self):
        self.acc.x = 0

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.vel += self.acc

        # dolne ograniczenie
        if self.pos.y > HEIGHT - self.rect.height / 2:
            self.pos.y = HEIGHT - self.rect.height / 2
            self.acc.y = 0
            self.vel.y = 0

        # prawe ograniczenie
        if self.pos.x < 0 + self.rect.width / 2:
            self.pos.x = 0 + self.rect.width / 2
            self.acc.x = 0
            self.vel.x = 0

        # prawe ograniczenie
        if self.pos.x > WIDTH - self.rect.width / 2:
            self.pos.x = WIDTH - self.rect.width / 2
            self.acc.x = 0
            self.vel.x = 0

        self.pos += self.vel
        self.rect.center = self.pos

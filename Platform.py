import pygame as pg
from settings import *
import os

vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

player_img = pg.image.load(os.path.join(img_folder, 'Player.png'))

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.game.platforms.add(self)
        self.game.all_sprites.add(self)
        self.image = pg.Surface((w, h))
        self.image.fill(DARKGREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
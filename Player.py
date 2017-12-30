import pygame as pg
from settings import *
import os

vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

player_img = pg.image.load(os.path.join(img_folder, 'Player.png'))
player_left_img = pg.image.load(os.path.join(img_folder, 'Player_wall_left.png'))
player_right_img = pg.image.load(os.path.join(img_folder, 'Player_wall_right.png'))
player_walk_r_img = pg.image.load(os.path.join(img_folder, 'Player_move_right.png'))
player_walk_l_img = pg.image.load(os.path.join(img_folder, 'Player_move_left.png'))
player_jump_up = pg.image.load(os.path.join(img_folder, 'jump_up.png'))
player_jump_down = pg.image.load(os.path.join(img_folder, 'jump_down.png'))
player_jump_lu = pg.image.load(os.path.join(img_folder, 'lu.png'))
player_jump_ru = pg.image.load(os.path.join(img_folder, 'ru.png'))
player_jump_ld = pg.image.load(os.path.join(img_folder, 'ld.png'))
player_jump_rd = pg.image.load(os.path.join(img_folder, 'rd.png'))

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.game.all_sprites.add(self)
        self.image = pg.transform.scale(player_img, (35, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(45, HEIGHT - (20 + self.rect.height / 2))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.wall_jump = 0

    def update(self):
        self.move()
        self.position()

    def jump(self):
        # jump only if standing on a platform
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if hits and self.vel.y == 0:
            self.acc.y += JUMP_POWER

    def walljump(self):
        if self.wall_jump == 1:
            self.acc.y += JUMP_POWER
            self.acc.x += 15
            self.wall_jump = 0

        if self.wall_jump == 2:
            self.acc.y += JUMP_POWER
            self.acc.x += -15
            self.wall_jump = 0

    def position(self):
        if self.pos.x <= 0 + self.rect.width / 2:
            self.image = pg.transform.scale(player_left_img, (35, 38))
            self.wall_jump = 1
        elif self.pos.x >= WIDTH - self.rect.width / 2:
            self.image = pg.transform.scale(player_right_img, (35, 38))
            self.wall_jump = 2
        else:
            self.image = pg.transform.scale(player_img, (35, 30))
            self.wall_jump = 0

        hits = pg.sprite.spritecollide(self, self.game.platforms, False)

        if hits and self.vel.x > 0:
            self.image = pg.transform.scale(player_walk_r_img, (45, 30))
        elif hits and self.vel.x < 0:
            self.image = pg.transform.scale(player_walk_l_img, (45, 30))

        if self.vel.y > 0 and not self.pos.x >= WIDTH - self.rect.width / 2 and not self.pos.x <= 0 + self.rect.width / 2:
            self.image = pg.transform.scale(player_jump_down, (30, 50))
        elif self.vel.y < 0 and not self.pos.x >= WIDTH - self.rect.width / 2 and not self.pos.x <= 0 + self.rect.width / 2:
            self.image = pg.transform.scale(player_jump_up, (30, 50))

        if self.vel.x > 0 and self.vel.y < 0:
            self.image = pg.transform.scale(player_jump_ru, (45, 40))
        elif self.vel.x < 0 and self.vel.y < 0:
            self.image = pg.transform.scale(player_jump_lu, (45, 40))

        if self.vel.x > 0 and self.vel.y > 0:
            self.image = pg.transform.scale(player_jump_rd, (45, 40))
        elif self.vel.x < 0 and self.vel.y > 0:
            self.image = pg.transform.scale(player_jump_ld, (45, 40))


    def move(self):
        if self.vel.y > 0:
            if self.wall_jump > 0:
                self.vel.y = WALL_FRICTION
            else:
                self.acc = vec(0, PLAYER_GRAVITY)
        else:
            self.acc = vec(0, PLAYER_GRAVITY)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.jump()
            self.walljump()

        # tarcie
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # ogranicznik predkosci
        if self.vel.y > 17:
            self.vel.y = 17
        if self.vel.y < -27:
            self.vel.y = -27

        self.vel += self.acc
        if abs(self.vel.x) < 1:
            self.vel.x = 0

        self.pos += self.vel

        # lewe ograniczenie
        if self.pos.x < 0 + self.rect.width / 2:
            self.pos.x = 0 + self.rect.width / 2
            self.vel.x = 0

        # prawe ograniczenie
        if self.pos.x > WIDTH - self.rect.width / 2:
            self.pos.x = WIDTH - self.rect.width / 2
            self.vel.x = 0

        # kill pologa
        if self.pos.y > HEIGHT + 300:
            pg.event.post(pg.event.Event(pg.QUIT))

        self.rect.center = self.pos

        hits = pg.sprite.spritecollide(self, self.game.platforms, False)

        for hit in hits:
            if self.rect.right > hit.rect.left and self.rect.left < hit.rect.right:
                if self.vel.y > 0:
                    self.pos.y = hit.rect.top - self.rect.height / 2 + 1
                    self.vel.y = 0
                elif self.vel.y < 0:
                    self.pos.y = hit.rect.bottom + self.rect.height / 2
                    self.vel.y = 0
            elif self.rect.bottom > hit.rect.top and self.rect.top < hit.rect.bottom:
                if self.vel.x > 0:
                    self.pos.x = hit.rect.left - self.rect.width / 2
                    self.vel.x = 0
                elif self.vel.x < 0:
                    self.pos.x = hit.rect.right + self.rect.width / 2
                    self.vel.x = 0

        self.rect.center = self.pos

        # y_hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        #
        # if y_hits:
        #     if self.vel.y > 0 and self.rect.bottom >= y_hits[0].rect.top:
        #         self.pos.y = y_hits[0].rect.top - self.rect.height / 2 + 1
        #         self.vel.y = 0
        #     elif self.vel.y < 0 and self.rect.top <= y_hits[0].rect.bottom:
        #         self.pos.y = y_hits[0].rect.bottom + self.rect.height / 2
        #         self.vel.y = 0
        #
        # x_hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        #
        # if x_hits:
        #     if self.vel.x > 0 and self.rect.right >= x_hits[0].rect.left:
        #         self.pos.x = x_hits[0].rect.left - self.rect.width / 2
        #         self.vel.x = 0
        #         self.wall_jump = 2
        #     elif self.vel.x < 0 and self.rect.left <= x_hits[0].rect.right:
        #         self.pos.x = x_hits[0].rect.right + self.rect.width / 2
        #         self.vel.x = 0
        #         self.wall_jump = 1
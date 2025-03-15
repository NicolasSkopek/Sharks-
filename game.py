import pygame.mixer

from obj import Obj, Octopus, Text
import random

pygame.font.init()

class Game:
    def __init__(self):
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.shark = Obj("assets/shark1.png", random.randrange(0, 290), -10, 74 / 1.1, 111 / 1.1)
        self.shark2 = Obj("assets/shark1.png", random.randrange(0, 290), -150, 74 / 1.1, 111 / 1.1)
        self.coin = Obj("assets/coin1.png", random.randrange(0, 290), -20)
        self.octopus = Octopus("assets/octopus1.png", 150, 600, 36*1.2, 35*1.2)

        self.change_scene = False

        self.score = Text(70, "0", 255, 255, 255)
        self.lifes = Text(50, "3", 255, 0, 0)

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.octopus.drawing(window)
        self.shark.drawing(window)
        self.shark2.drawing(window)
        self.coin.drawing(window)
        self.score.draw(window, 150, 30)
        self.lifes.draw(window, 10, 10)

    def update(self):
        self.move_bg()
        self.octopus.anim("octopus", 3, 6)
        self.shark.anim("shark", 3, 6)
        self.shark2.anim("shark", 3, 6)
        self.move_sharks()
        self.coin.anim("coin", 1.7, 8)
        self.move_coin()
        self.octopus.collision(self.shark.group, "Shark")
        self.octopus.collision(self.shark2.group, "Shark")
        self.octopus.collision(self.coin.group, "Coin")
        self.gameover()
        self.score.update_text(str(self.octopus.pts), 255, 255, 255)
        self.lifes.update_text(str(self.octopus.life), 255, 0, 0)

    def move_bg(self):
        self.bg.sprite.rect.y += 6
        self.bg2.sprite.rect.y += 6

        if self.bg.sprite.rect.y >= 640:
            self.bg.sprite.rect.y = 0

        if self.bg2.sprite.rect.y >= 0:
            self.bg2.sprite.rect.y = -640

        self.bg.group.update()
        self.bg2.group.update()

    def move_sharks(self):
        self.shark.sprite.rect.y += 10
        self.shark2.sprite.rect.y += 10

        if self.shark.sprite.rect.y >= 700:
            self.shark.sprite.kill()
            self.shark = Obj("assets/shark1.png", random.randrange(0, 290), -100, 74 / 1.1, 111 / 1.1)

        if self.shark2.sprite.rect.y >= 700:
            self.shark2.sprite.kill()
            self.shark2 = Obj("assets/shark1.png", random.randrange(0, 290), -100, 74 / 1.1, 111 / 1.1)

    def move_coin(self):
        self.coin.sprite.rect.y += 13

        if self.coin.sprite.rect.y >= 750:
            self.coin.sprite.kill()
            self.coin = Obj("assets/coin1.png", random.randrange(0, 290), -10)

    def gameover(self):
        if self.octopus.life <= 0:
            self.change_scene = True
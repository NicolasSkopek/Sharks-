from obj import Obj

class Game:
    def __init__(self):
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)
        self.change_scene = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)

    def update(self):
        self.bg.sprite.rect.y += 0.1
        self.bg2.sprite.rect.y += 0.1

        if self.bg.sprite.rect.y >= 640:
            self.bg.sprite.rect.y = -640

        if self.bg2.sprite.rect.y >= 640:
            self.bg2.sprite.rect.y = -640

        self.bg.group.update()
        self.bg2.group.update()

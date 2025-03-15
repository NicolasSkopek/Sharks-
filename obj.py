import pygame

class Obj:
    def __init__(self, image, x, y, width = None, height = None):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.original_image = pygame.image.load(image)

        if width and height:
            self.original_image = pygame.transform.scale(self.original_image, (width, height))

        self.sprite.image = self.original_image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y

        self.frame = 1
        self.tick = 0
        self.width = width
        self.height = height

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, name, speed, num_frames):
        self.tick += 1
        if self.tick >= speed:
            self.tick = 0
            self.frame += 1

        if self.frame > num_frames:
            self.frame = 1

        new_image = pygame.image.load(f"assets/{name}{self.frame}.PNG")

        if self.width and self.height:
            new_image = pygame.transform.scale(new_image, (self.width, self.height))

        self.sprite.image = new_image

class Octopus(Obj):
        def __init__(self, image, x, y, width, height):
            super().__init__(image, x, y, width, height)

            pygame.mixer.init()

            self.sound_pts = pygame.mixer.Sound("assets/sounds/point.mp3")
            self.sound_hit = pygame.mixer.Sound("assets/sounds/hurt.mp3")

            self.life = 3
            self.pts = 0



        def move_octopus(self, event):
            if event.type == pygame.MOUSEMOTION:
                self.sprite.rect.x = pygame.mouse.get_pos()[0]
                self.sprite.rect.y = pygame.mouse.get_pos()[1]

        def collision(self, group, name):

            name = name

            colision = pygame.sprite.spritecollide(self.sprite, group, True)

            if name == "Coin" and colision:
                self.pts += 1
                self.sound_pts.play()
            if name == "Shark" and colision:
                self.life -= 1
                self.sound_hit.play()

class Text:

    def __init__(self, size, text, r, g, b):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, True, (r,g,b))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update, r ,g ,b):
        self.render = self.font.render(update, True, (r,g,b))

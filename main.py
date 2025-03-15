import pygame
from menu import Menu, GameOver
from game import Game



class Main:
    def __init__(self, width, height, title):
        pygame.init()
        pygame.mixer.init()

        self.sound_hit = pygame.mixer.Sound("assets/sounds/hurt.mp3")

        self.window = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

        icon = pygame.image.load("assets/icon.PNG")
        pygame.display.set_icon(icon)

        pygame.mixer_music.load("assets/sounds/aquatic.mp3")


        self.menu = Menu("assets/menu.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()


    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.play(-1)
                ## pygame.mixer.music.set_volume(0.05)
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            pygame.mixer_music.stop()
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.octopus.life = 3
            self.game.octopus.pts = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(event)
            elif not self.game.change_scene:
                self.game.octopus.move_octopus(event)
            else:
                self.gameover.events(event)


    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


game = Main(320, 640, "Sharks!")
game.update()

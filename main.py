import pygame
from obj import Obj
from menu import Menu

class Main:
    def __init__(self, width, height, title):

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.menu = Menu()

        self.loop = True


    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            self.menu.events(event)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


game = Main(320, 640, "Sharks!")
game.update()

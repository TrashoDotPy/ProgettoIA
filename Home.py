import pygame
from Game import Game
from Button import Button

class Home:
    def __init__(self, display, stateManager, game:Game):
        self.__display = display
        self.__stateManager = stateManager
        self.__game = game

        self.facile = pygame.Rect(0,0,200,50)
        self.medio = pygame.Rect(0,0,200,50)
        self.difficile = pygame.Rect(0,0,200,50)

        self.hoverFacile = False
        self.hoverMedio = False
        self.hoverDifficile = False

    def run(self, events):
        self.__display.fill((235,175,235))
        Button.draw_dark(self.__display, self.facile, "FACILE", self.hoverFacile, self.__display.get_width() // 2, self.__display.get_height() // 2)
        Button.draw_light(self.__display, self.medio, "MEDIO", self.hoverMedio, self.__display.get_width() // 2, self.__display.get_height() // 2 + 70)
        Button.draw_red(self.__display, self.difficile, "DIFFICILE", self.hoverDifficile, self.__display.get_width() // 2, self.__display.get_height() // 2 + 140)

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.hoverFacile = self.facile.collidepoint(event.pos)
                self.hoverMedio = self.medio.collidepoint(event.pos)
                self.hoverDifficile = self.difficile.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.hoverFacile:
                    self.__game.setLevel(0)
                    self.__stateManager.setState("Game")
                elif self.hoverMedio:
                    self.__game.setLevel(1)
                    self.__stateManager.setState("Game")
                else:
                    self.__game.setLevel(2)
                    self.__stateManager.setState("Game")
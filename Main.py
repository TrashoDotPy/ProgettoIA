import pygame
from StateManager import StateManager
from Home import Home
from Game import Game
 
HIGH = 900
WIDTH = 900

MATRIX = [[150,200,250],[250,200,150],[2,1,3]]

pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGH))
clock = pygame.time.Clock()

stateManager = StateManager("Home")

game = Game(screen, stateManager)
home = Home(screen, stateManager, game)

states = {
            "Home" : home,
            "Game" : game
        }

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    states[stateManager.getState()].run(events)
    pygame.display.update()
    pygame.display.flip()


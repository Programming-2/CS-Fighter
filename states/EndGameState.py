import pygame
from states.State import State


class EndGameState(State):

    def __init__(self, name):
        super().__init__(name)

    def resetState(self):
        pass

    def update(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)

import pygame
from states.State import State
from utils.Rect import Rect
from levels.GrassLevel import GrassLevel
from levels.IceLevel import IceLevel
from levels.LavaLevel import LavaLevel
from levels.RandomLevel import RandomLevel
from utils.Colors import colors


class MapSelectionState(State):

    def __init__(self, name, handler, screen, img):
        super().__init__(name)
        self.img = img
        self.handler = handler
        self.map = None

        # TODO Fix bug with duplicated players or made it so same player cannot be selected twice

        # Rectangle Dict
        self.rects = {
            Rect(18, 18, 1064, 114): GrassLevel(screen),
            Rect(18, 160, 1064, 115): IceLevel(screen),
            Rect(18, 304, 1064, 114): LavaLevel(screen),
            Rect(18, 464, 1064, 114): RandomLevel(screen)
        }

    def resetState(self):
        self.map = None

    def update(self, screen):
        pressed = False

        # Event look
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        # Drawing background image
        screen.blit(self.img, [0, 0])

        # TODO Make going to main menu reset selections

        # Button to return to the main menu
        if (715 < pygame.mouse.get_pos()[0] < 1055 and pressed) and (600 < pygame.mouse.get_pos()[1] < 750 and pressed):
            self.handler.getStateManager().resetStates()
            self.handler.getStateManager().setCurrentState("MainMenuState")

        # Looks at keys in rects dict, and determines if the mouse if clicking that rect
        for key in self.rects:
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                if pressed:
                    self.handler.setLevel(self.rects[key])
                    self.handler.getStateManager().getState("GameState").reloadLevel()
                    self.handler.getStateManager().setCurrentState("GameState")
                else:
                    pygame.draw.rect(screen, colors["GREEN"], key)

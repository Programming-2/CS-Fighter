import pygame
from states.State import State
from utils.Sound import Sound
from user.settings import Settings


class MainMenuState(State):

    def __init__(self, name, mainMenu, handler):
        super().__init__(name)
        self.menuImage = mainMenu
        self.handler = handler
        self.theme = Sound("Track1")
        self.settings = Settings()
        if self.settings.useMusic():
            self.theme.playSound()

    def resetState(self):
        pass

    def update(self, screen):
        if not self.settings.useMusic():
            self.theme.stopSound()

        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.menuImage, [0, 0])

        if (400 < pygame.mouse.get_pos()[0] < 650 and pressed) and (440 < pygame.mouse.get_pos()[1] < 520 and pressed):
            self.handler.getStateManager().setCurrentState("PlayerSelectionState")

        if (400 < pygame.mouse.get_pos()[0] < 650 and pressed) and (530 < pygame.mouse.get_pos()[1] < 610 and pressed):
            self.handler.getStateManager().setCurrentState("SettingsState")

        if (400 < pygame.mouse.get_pos()[0] < 650 and pressed) and (620 < pygame.mouse.get_pos()[1] < 700 and pressed):
            self.handler.getStateManager().setCurrentState("ControlState")

        if (403 < pygame.mouse.get_pos()[0] < 646 and pressed) and (717 < pygame.mouse.get_pos()[1] < 784 and pressed):
            self.handler.setDone(True)

        if (1050 < pygame.mouse.get_pos()[0] < 1100 and pressed) and (750 < pygame.mouse.get_pos()[1] < 800 and pressed):
            self.handler.getStateManager().setCurrentState("MinigameMenu")

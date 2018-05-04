# Parent Level Class
from abc import abstractmethod
import pygame
from src.Platform import Platform

pygame.init()


class Level():
    def __init__(self, screen, backImg):
        self.__screen = screen
        self.__backImg = backImg
        self.lWall = Platform(screen, -500, -1000, 500, 1800, -1)
        self.rWall = Platform(screen, 1100, -1000, 500, 1800, -1)
        self.ceiling = Platform(screen, -500, -1500, 2100, 500, -1)
        self.healthBar1 = Platform(screen, 10, 40, 510, 60, -1)
        self.healthBar2 = Platform(screen, 590, 40, 1090, 60, -1)
        self.platformGroup = pygame.sprite.Group()
        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.healthBar1)
        self.platformGroup.add(self.healthBar2)
        self.platformGroup.add(self.ceiling)

    def getBackImg(self):
        return self.__backImg

    @abstractmethod
    def update(self):
        pass

# Platform class
import pygame
from src.Cooldown import Cooldown
from utils.Colors import colors

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, length, height, duration=-1, speed=0):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = pygame.Surface([self.length, self.height])
        self.rect = self.image.get_rect()
        self.duration = duration
        self.speed = speed
        self.platform_cooldown = Cooldown(duration)

    def entMove(self, entity):
        entity.xchange += self.speed

    def drawPlat(self, screen):
        pygame.draw.rect(screen, colors.get("PINK"), self.rect)

    def update(self):
        self.rect.topleft = self.x, self.y
        if self.duration != -1:
            self.platform_cooldown.update()

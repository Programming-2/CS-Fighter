import random
from levels.Level import Level
from src.Platform import Platform
from utils.Colors import colors


class RandomLevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/random_map.png", handler)
        for i in range(0, 11):
            self.p1 = Platform(screen, (random.randint(0, (i * 100))), (random.randint(300, 600)), (random.randint((i * 100), (i * 100 + 50))), (random.randint(300, 600)), -1)
            self.platformGroup.add(self.p1)

    def update(self, screen):
        for plat in self.platformGroup:
            plat.drawPlat(screen)

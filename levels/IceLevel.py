from levels.Level import Level
from src.Platform import Platform


class IceLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/SnowMap.png")

        # TODO Add platforms
        self.ground1 = Platform(screen, 0, 473, 225, 200, -1)
        self.ground2 = Platform(screen, 224, 576, 616, 200, -1)
        self.ground3 = Platform(screen, 841, 394, 259, 200, -1)
        self.platformGroup.add(self.ground1)
        self.platformGroup.add(self.ground2)
        self.platformGroup.add(self.ground3)

    def update(self):
        pass

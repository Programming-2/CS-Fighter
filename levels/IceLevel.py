from levels.Level import Level
from src.Platform import Platform


class IceLevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/SnowMap.png", handler)

        self.ground1 = Platform(screen, 0, 394, 225, 406)
        self.ground2 = Platform(screen, 224, 576, 616, 224)
        self.ground3 = Platform(screen, 841, 394, 259, 406)
        self.platformGroup.add(self.ground1)
        self.platformGroup.add(self.ground2)
        self.platformGroup.add(self.ground3)

    def update(self, screen):
        pass

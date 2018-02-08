import pygame
from player import Player
from testLevel import TestLevel
from healthbar import HealthBar

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

level = TestLevel(screen)

background_image = pygame.image.load(level.getBackImg()).convert()
testSprite = pygame.image.load("media/BaseSprite.png").convert()
testProjectile = pygame.image.load("media/projectileTest.png").convert()

platformArray = pygame.sprite.Group()

platformArray.add(level.ground)

player1 = Player(testSprite, 100, 20, "Yes", "No", "Will", 200, 100, platformArray, screen, testProjectile)
player2 = Player(testSprite, 100, 20, "Yes", "No", "Jaccob Bonkley", 850, 100, platformArray, screen, testProjectile)

p1hpbar = HealthBar(screen, "topleft", player1.health)
p2hpbar = HealthBar(screen, "topright", player2.health)

pygame.display.set_caption("Lil' Shed's Get Good In™")

clock = pygame.time.Clock()

p1HitList = []
p2HitList = []

done = False
while not done:
    screen.blit(background_image, [0, 0])  # Jakob's mistake

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.jump()
            elif event.key == pygame.K_a:
                player1.xchange = -5
            elif event.key == pygame.K_d:
                player1.xchange = 5
            elif event.key == pygame.K_s:
                player1.health -= 10
                pass  # player1.duck()
            elif event.key == pygame.K_e:
                player1.getAttack().ranged_attack(screen)
            elif event.key == pygame.K_UP:
                player2.jump()
            elif event.key == pygame.K_LEFT:
                player2.xchange = -5
            elif event.key == pygame.K_RIGHT:
                player2.xchange = 5
            elif event.key == pygame.K_DOWN:
                player2.health -= 10
                pass  # player2.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.xchange = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.xchange = 0
            elif event.key == pygame.K_s:
                pass  # player1.unduck()
            elif event.key == pygame.K_DOWN:
                pass  # player2.unduck()

    player1.update(screen)
    player2.update(screen)
    p2hpbar.update(player2.health)
    p1hpbar.update(player1.health)
    player1.getAttack().update()
    level.ground.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

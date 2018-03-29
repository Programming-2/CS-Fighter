import pygame
from players.Player import Player\

class David(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 150
        damage = 10
        winQuote = "I always start the party"
        loseQuote = "Zzz"
        name = "David"
        defense = .5
        movespeed = 5
        self.handler = handler

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, movespeed, handler.getPlatformArray(), handler.getAttackList(), handler,
                         defense)
        self.count = 0
        self.start_time = 0
        self.attacksprite = pygame.image.load("media/DavidAttack.png")
        self.special_cooldown = self.special_total_cooldown
        self.special_total_cooldown = 5
        self.special_start_time = 0
        self.special_count = 0
        self.special_active = False
        self.special_available = True
        self.playNum = playNum
        self.targetMoveSpeed = 0
        self.ticks = pygame.time.get_ticks()

    def special(self):
        if self.special_available:
            self.special_active = True

    def update(self, screen):
        self.moveX()
        self.moveY()
        self.gravityUpdate()

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        self.attackUpdate(screen)

        if not self.special_available:
            self.special_cooldown = 0
            if self.special_count == 0:
                self.special_start_time = pygame.time.get_ticks()
                self.special_count = 1
            self.special_cooldown = (pygame.time.get_ticks() - self.special_start_time) / 1000
            if self.special_cooldown >= self.special_total_cooldown:
                self.special_available = True
                self.special_count = 0

        if self.special_active and not self.sleeping:
            if self.count == 0:
                self.start_time = pygame.time.get_ticks()
                self.count += 1
            seconds = 0
            if seconds <= 1:
                seconds = (pygame.time.get_ticks() - self.start_time) / 1000
                if self.playNum == 1:
                    self.special_available = False
                    self.targetMoveSpeed = self.handler.getPlayer2MoveSpeed()
                    self.handler.setPlayer2MoveSpeed(0)
                if self.playNum == 2:
                    self.special_available = False
                    self.targetMoveSpeed = self.handler.getPlayer1MoveSpeed()
                    self.handler.setPlayer1MoveSpeed(0)

            if seconds > 1:
                if self.playNum == 1:
                    self.handler.setPlayer2MoveSpeed(self.targetMoveSpeed)
                    self.special_active = False
                    self.count = 0
                if self.playNum == 2:
                    self.handler.setPlayer1MoveSpeed(self.targetMoveSpeed)
                    self.special_active = False
                    self.count = 0

        screen.blit(self.sprite, [self.rect.x, self.rect.y])
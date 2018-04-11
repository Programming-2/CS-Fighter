import pygame
from src.Attack import Attack


class CustomAttack(Attack):
    def __init__(self, player, damage, handler, x_speed, y_speed):
        self.player = player
        self.damage = damage
        self.handler = handler
        super().__init__(self.player, self.damage, self.handler)

        self.changex = x_speed
        self.changey = y_speed
        self.rect.x = self.player.rect.x + (self.player.width * .5) - (self.attacksprite.get_width() * .5)
        self.rect.y = self.player.rect.y + (self.player.height * .5) - (self.attacksprite.get_height() * .5)

    def update(self, screen):
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.direction == -1:
            screen.blit(self.left_attack, (self.rect.x, self.rect.y))
        if self.direction == 1:
            screen.blit(self.right_attack, (self.rect.x, self.rect.y))
        if self.handler.getPlayer1().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer2(), self):
                self.handler.getPlayer2().takeDamage(self.damage)
                self.handler.getAttackList().remove(self)
        if self.handler.getPlayer2().name == self.name:
            if pygame.sprite.collide_rect(self.handler.getPlayer1(), self):
                self.handler.getAttackList().remove(self)
                self.handler.getPlayer1().takeDamage(self.damage)

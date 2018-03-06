import pygame
from players.Will import Will


class Handler:

    def __init__(self, attackList, stateManager, platformArray, level):
        self.attackList = attackList
        self.stateManager = stateManager
        self.platformArray = platformArray
        self.done = False
        self.player1 = Will(0, 0, self)
        self.player2 = Will(0, 0, self)
        self.level = level
        self.projectileimage = pygame.image.load("media/projectileTest.png")

    def getAttackList(self):
        return self.attackList

    def setAttackList(self, list):
        self.attackList = list

    def getPlayer1(self):
        return self.player1

    def setPlayer1(self, player1):
        self.player1 = player1

    def getPlayer2(self):
        return self.player2

    def setPlayer2(self, player2):
        self.player2 = player2

    def getStateManager(self):
        return self.stateManager

    def getDone(self):
        return self.done

    def setDone(self, done):
        self.done = done

    def setPlatformArray(self, array):
        self.platformArray = array

    def getPlatformArray(self):
        return self.platformArray

    def getProjectileImage(self):
        return self.projectileimage

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def setMoveSpeed(self, movespeed):
        pass
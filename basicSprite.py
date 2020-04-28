import pygame
from helpers import *

class singleSprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, image):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.image = image
        self.rect = image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint

class multipleSprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, images):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint

class Heart(multipleSprite):
    """
    This is the class that will make sure that heart appear in the inventory
    """
    def __init__(self, centerPoint, images):
        multipleSprite.__init__(self, centerPoint, images)

    def update(self, level):
        if level >= 4:
            self.image = self.images[0]
        elif level == 3:
            self.image = self.images[1]
        elif level == 2:
            self.image = self.images[2]
        elif level == 1:
            self.image = self.images[3]
        elif level == 0:
            self.image = self.images[4]

class Bomb(singleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images):
        singleSprite.__init__(self, centerPoint, images)
        self.timer = 10
        self.gone = False

    def update(self, breakable_group, troll_group, shooter_group, bat_group, boss_group):
        self.timer -= 1
        if self.timer == 0:
            enemies = self.blow(breakable_group, troll_group, shooter_group, bat_group, boss_group)
            return enemies

    def blow(self, breakable_group, troll_group, shooter_group, bat_group, boss_group):
        self.gone = True
        """
        Go through the 8 adjoining squares, make sure that: if it hits an enemy, the enemy dies. If it hits a breakable wall, open the wall
        """
        R = (64,0)
        U = (0,64)
        L = (-64,0)
        D = (0, -64)
        move = [R, U, L, L, D, D, R, R]
        enemies = []
        boss = 0

        for i in range(0,7):
            x = move[i]
            self.rect.move_ip(x[0], x[1])

            lstBreakable = pygame.sprite.spritecollide(self, breakable_group, False)
            if len(lstBreakable) > 0:
                for wall in lstBreakable:
                    wall.destroy()

            step = []
            lstTroll = pygame.sprite.spritecollide(self, troll_group, False)
            step.append(lstTroll)
            lstShooter = pygame.sprite.spritecollide(self, shooter_group, False)
            step.append(lstShooter)
            lstBat = pygame.sprite.spritecollide(self, bat_group, False)
            step.append(lstBat)
            if len(step) > 0:
                flag = "Enemy"
            enemies.append(step)

            boss = pygame.sprite.spritecollide(self, boss_group, False)
            if len(boss) > 0:
                boss = 1
                flag = "Boss"

        if flag == "Enemy":
            return (flag, enemies)
        elif flag == "Boss":
            return (flag, boss)

class Potion(singleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images):
        singleSprite.__init__(self, centerPoint, images)
        self.timer = 5
        self.gone = False

class Numbers(multipleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images, number):
        multipleSprite.__init__(self, centerPoint, images)

    def update(self, number):
        """gets a new number and changes the display to that number (0-9)"""
        if number == 0:
            self.image = self.images[0]
        elif number == 1:
            self.image = self.images[1]
        elif number == 2:
            self.image = self.images[2]
        elif number == 3:
            self.image = self.images[3]
        elif number == 4:
            self.image = self.images[4]
        elif number == 5:
            self.image = self.images[5]
        elif number == 6:
            self.image = self.images[6]
        elif number == 7:
            self.image = self.images[7]
        elif number == 8:
            self.image = self.images[8]
        elif number == 9:
            self.image = self.images[9]

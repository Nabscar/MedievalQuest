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
        if level == 3:
            self.image = self.images[0]
        elif level == 2:
            self.image = self.images[1]
        elif level == 1:
            self.image = self.images[2]

class Bomb(singleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images):
        singleSprite.__init__(self, centerPoint, images)
        self.timer = 20
        self.gone = False

    def update(self):
        print(self.timer)
        self.timer -= 1
        if self.timer == 0:
            self.blow()
            return True

    def blow(self):
        self.gone = True
        """
        Go through the 8 adjoining squares, make sure that: if it hits an enemy, the enemy dies. If it hits a breakable wall, open the wall
        """

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

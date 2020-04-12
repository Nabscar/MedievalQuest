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

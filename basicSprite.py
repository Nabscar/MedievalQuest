import pygame
from helpers import *

class Sprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, images):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.images = images
        print(self.images)
        self.image = self.images[0]

        print(self.images)
        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint

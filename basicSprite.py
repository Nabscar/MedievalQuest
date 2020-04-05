import pygame
from helpers import *

class Sprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, image):
        """
        This will be the class that will initialize all of these basic values that were mentioned above
        """
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.image = image
        self.rect = image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint


class Background(pygame.sprite.Sprite):
    """
    This class will initialize the Background
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)


class Passage(Background):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image, next_screen):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)
        self.next_screen = next_screen

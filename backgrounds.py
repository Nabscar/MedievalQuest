import pygame
import basicSprite

class Block_Background(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)

        pass


class Passage(basicSprite.Sprite):
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

        pass


class CrossableBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)

        pass


class BreakableBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image, broken = False):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)
        self.broken = broken

        pass

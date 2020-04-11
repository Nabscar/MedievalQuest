import pygame
import basicSprite
"""
This python script creates classes for all 2 types of backgrounds:
    - Breakable Background (Like Walls with cracks in them)
    - Passages (the backgrounds on the borders that lead to new screens)
All the other types are used as a siple Sprite
"""


class Passage(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self, centerPoint, images, next_screen):
        """
        Initializes Passage
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.next_screen = next_screen

class BreakableBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self, centerPoint, images, cave, broken = False):
        """
        Initializes breakableBackground
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.broken = broken
        self.image_order = ["Unbroken", "Broken"]
        #self.image = self.images[0]
        self.cave = cave

    def destroy(self):
        """
        activates when a bomb is placed and the wall is broken
        """
        self.image = self.images[1]
        self.broken = True

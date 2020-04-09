import pygame
import basicSprite
"""
This python script creates classes for all 4 types of backgrounds:
    - Crossable Backgrounds (like ground)
    - Block Backgrounds (like walls and Trees)
    - Breakable Background (Like Walls with cracks in them)
    - Passages (the backgrounds on the borders that lead to new screens)
"""
class BlockBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, images):
        """
        Initializes the Blockable wall
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.next_screen = next_screen
        self.image = self.images[0]
        pass


class Passage(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, images, next_screen):
        """
        Initializes Passage
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.next_screen = next_screen
        self.image = self.images[0]

        pass


class CrossableBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, image):
        """
        Initializes Crossable Background
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.next_screen = next_screen
        self.image = self.images[0]
        pass


class BreakableBackground(basicSprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player chagnes Screen
    """
    def __init__ (self.centerPoint, images, broken = False, cave):
        """
        Initializes breakableBackground
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.broken = broken
        self.image_order = ["Unbroken", "Broken"]
        selg.image = self.images[0]
        self.cave = cave

    def destroy(self):
    """
    activates when a bomb is placed and the wall is broken
    """
        self.image = self.images[1]
        self.broken = True
        pass

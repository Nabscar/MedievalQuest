import pygame
import basicSprite

class Monster1(basicSprite.Sprite):
    """
    This is where we create the first type of monster
    """
    def __init__(self, centerPoint, image):
        """
        use the initialization of the basic Sprite and the initialize any specific thigns for this enemy
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)
        """start the basic initialization"""

        pass

    def update(self, block_group):
        """
        This function is the one that will move an dupdate the position of the monsters
        It is called each "cycle" of gameplay to show that they move
        """

        pass

    def die(self):
        """
        This function establishes what happens when a enemy is killed
        it will probably mean that the enemy is deleted and his spot in the game is replaced with a blank background spot
        """

        pass

"""
There is the possibility of creating more classes for more monsters
But without the actual implementation fo the code there is no reason to
Since the differences between them would not be seen in pseudocode
"""

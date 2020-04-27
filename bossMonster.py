import pygame
import basicSprite
import random

"""Class that creates and controls the Boss"""

class Boss(pygame.sprite.Sprite):
    """
    This is where we create the Green Monsters
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, images, coords, direction = 0):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.images = images
        self.image = self.images[0][1]
        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint
        """0 is left, 1 is right, gona have him onle bounce around horizontally"""
        self.original_rect = pygame.Rect(self.rect)

        self.coords = coords
        """
        THe way the boss images work are the following:
        There is one list of images, the list is 6 items long, each of these items is another list.
        This new list is a collection of the images for each level of the boss
        """
        self.direction = direction

        self.dist = 64

        """
        For attacks:
            0 is none
            1 is forward
            2 is sideways
            3 is preping and 4 is sweeping
        """
        self.attack = 0

        self.health = 30

    def update(self, block_group, passage_group, player_group):

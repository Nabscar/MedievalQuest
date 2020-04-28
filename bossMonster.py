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
        """
        For attacks:
            0 is forward
            1 is none
            2 is preping
            3 is sideways
            4 is sweeping
        """
        self.attack = 1
        self.level = 0
        self.image = self.images[self.level][self.attack]
        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint
        self.centerPoint = centerPoint
        """0 is left, 1 is right, gona have him onle bounce around horizontally"""

        self.coords = coords
        """
        THe way the boss images work are the following:
        There is one list of images, the list is 6 items long, each of these items is another list.
        This new list is a collection of the images for each level of the boss
        """
        self.direction = direction

        self.dist = 64
        self.xMove = self.dist
        self.yMove = 0

        self.health = 1

    def update(self, block_group, passage_group):
        """Updates Image and location to center after previous update"""
        if self.attack == 0 or self.attack == 4:
            self.rect.move_ip(0,-self.dist/2)
            self.centerPoint = self.rect.center
        elif self.attack == 1 or self.attack == 3:
            self.rect.move_ip(0,0)
            self.centerPoint = self.rect.center
        elif self.attack == 2:
            self.rect.move_ip(-self.dist/2, 0)
            self.centerPoint = self.rect.center

        """Change to new attack"""
        if self.attack == 2:#If it prepped, then attack
            self.attack = 4
        elif self.attack == 0 or self.attack == 3 or self.attack == 4:#If it attacked then neutral
            self.attack = 1
        else:#If it didnt attack and didnt prep then in neutraled, so reandomize new thing (either move or attack)
            if random.randint(1,10) == 1:
                self.attack = random.randint(0, 3)
            else:
                self.attack = 1
                if random.randint(1,2) == 1:
                    self.rect.move_ip(self.xMove,self.yMove) #This is 2what actually moves the character
                    if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, passage_group):
                        """If we hit a block, don’t move – reverse the movement"""
                        self.rect.move_ip(-self.xMove,-self.yMove)
                        self.xMove = -self.xMove


        """Update level based on current health"""
        if self.health > 25:
            self.level = 0
        elif self.health > 20:
            self.level = 1
        elif self.health > 15:
            self.level = 2
        elif self.health > 20:
            self.level = 3
        elif self.health > 5:
            self.level = 4
        elif self.health > 0:
            self.level = 5

        """Update Image and location"""
        if self.attack == 0 or self.attack == 4:
            self.rect.move_ip(0,self.dist/2)
            self.centerPoint = self.rect.center
        elif self.attack == 1 or self.attack == 3:
            self.rect.move_ip(0,0)
            self.centerPoint = self.rect.center
        elif self.attack == 2:
            self.rect.move_ip(self.dist/2, 0)
            self.centerPoint = self.rect.center

        self.image = self.images[self.level][self.attack]

        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = self.centerPoint

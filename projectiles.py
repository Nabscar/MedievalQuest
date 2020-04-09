import pygame
import basicSprite
"""
This is the python script that creates teh main projectile class and the children calsses for all three types of projectiles
It should be done
"""
class Projectile(pygame.sprite.Sprite):
    """
    This class will initialize the Passages. these are specific backgrounds that take you to the next screen
    we consider them sprites so that we can easily change them when the player changes Screen
    """
    def __init__ (self.centerPoint, images, counter):
        """
        Initializes the special characteristics of the basic projectile
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)
        self.counter = counter
        self.direction = direction
        self.done = False
        self.damage = damage
        pass

    def countdown(self):
        """
        Decreases the counter by one
        """
        self.counter -= 1
        pass

    def update(self, block_group, breakable_group, character_group, projectile_group):
        if self.direction==1:#down
            yMove = self.dist
        elif self.direction==2:#Left
            xMove = -self.dist
        elif self.direction==3:#right
            xMove = -self.dist
        elif self.direction==4:#up
            yMove = -self.dist

        self.rect.move_ip(xMove,yMove) #This is what actually moves the projectile
        if (pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group)
            or pygame.sprite.spritecollideany(self, character_group), or pygame.sprite.spritecollideany(self, passage_group):
            """If we hit a block or a the player, its done, projectile should disappear"""
            self.disappear()

        if (pygame.sprite.spritecollideany(self, projectile_group):
            """
            If we hit a projectile, we want to have different effects depending on which projectiles
            For now, we have decided that it is easier (as a start point) to just have it disappear
            """
            self.disappear()
        pass

    def disappear(self, ground_image):
        """
        This function establishes what happens when a projectile should disappear
        this means it is gone and the image is set as a ground image
        it is also removed from the projectile_group list
        """
        self.done = True
        self.images = ground_image

        pass

class Ball(Projectile):

    def __init__ (self.centerPoint, images, direction, counter = 6, damage = 1):
        """
        Initializes the special characteristics of the ball projectile
        """
        Projectile.__init__(self, centerPoint, images, counter, direction, damage)
        self.image = self.images[0]

        pass

class Javelin(Projectile):

        def __init__ (self.centerPoint, images, direction counter = 10, damage = 1):
            """
            Initializes the special characteristics of the javelin projectile
            """
            Projectile.__init__(self, centerPoint, images, counter, direction)
            self.damage = damage
            self.image_order = ["Down", "Left", "Right", "Up"]
            """
            directions go in same order as image order
            """
            self.image = self.images[self.direction - 1]

            pass

class Arrow(Projectile):

        def __init__ (self.centerPoint, image, counter = 15, damage = 1):
            """
            Initializes the special characteristics of the arrow projectile
            """
            Projectile.__init__(self, centerPoint, images, counter, direction)
            self.damage = damage
            self.image_order = ["Down", "Left", "Right", "Up"]
            """
            directions go in same order as image order
            """
            self.image = self.images[self.direction - 1]

            pass

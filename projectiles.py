import pygame
import basicSprite

class Projectile(pygame.sprite.Sprite):
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

class Ball(Projectile):

    def __init__ (self.centerPoint, image, counter = 6, damage = 1):
        """
        Initializes the special characteristics of the playable character
        """
        Projectile.__init__(self, centerPoint, image)
        self.counter = counter

        pass


class Javelin(Projectile):

        def __init__ (self.centerPoint, image, counter = 10, damage = 1):
            """
            Initializes the special characteristics of the playable character
            """
            Projectile.__init__(self, centerPoint, image)
            self.counter = counter

            pass

class Arrow(Projectile):

        def __init__ (self.centerPoint, image, counter = 15, damage = 1):
            """
            Initializes the special characteristics of the playable character
            """
            Projectile.__init__(self, centerPoint, image)
            self.counter = counter

            pass

import pygame
import basicSprite
from helpers import *
import time

POWER_UP_ONE_START = pygame.USEREVENT + 1
POWER_UP_ONE_END = POWER_UP_ONE_START + 1
POWER_UP_TWO_START = POWER_UP_ONE_END + 1
POWER_UP_TWO_END = POWER_UP_TWO_START + 1
PLAYER_DEAD = POWER_UP_TWO_END + 1

class player(basicSprite.Sprite):
    """
    This is the sprite or the playable character
    """

    def __init__ (self.centerPoint, image):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, image)

        """
        Initialize score, distance moved per turn, and how much is the current movement
        """
        self.score = 0

        self.x_dist = 1
        self.y_dist = 1

        self.xMove = 0
        self.yMove = 0

        pass

    def MoveKeyDown(self, key):
        """
        This is the function that moves the x and y position of the player
        depending on what hey they pressed, it will move once update() is called.
        """

        if (key == K_RIGHT):
            self.xMove += self.x_dist
        elif (key == K_LEFT):
            self.xMove += -self.x_dist
        elif (key == K_UP):
            self.yMove += -self.y_dist
        elif (key == K_DOWN):
            self.yMove += self.y_dist

        pass

    def MoveKeyUp(self, key):
        """
        This is the function that moves the x and y movement of the player to 0
        after they let go of the key this movement ends
        """

        if (key == K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == K_LEFT):
            self.xMove += self.x_dist
        elif (key == K_UP):
            self.yMove += self.y_dist
        elif (key == K_DOWN):
            self.yMove += -self.y_dist

        pass


    def update(self, groups of sprites):
        """
        Called to update the player sprite's position and state
        (state only if we choose to have power-ups)
        """
        if ((self.xMove == 0) and (self.yMove == 0)):
            """
            If we aren't moveing just get out of here
            """
            return

        """
        We're moving!
        """
        self.rect.move_ip(self.xMove,self.yMove)

        if pygame.sprite.spritecollideany(self, block_group):
            """
            If we hit a block, dont moved
            """
            self.rect.move_ip(0, 0)

        lstEnemies = pygame.sprite.spritecollide(self, enemy_group, False)
        if(len(lstEnemies) > 0):
            """
            We hit an Enemy!
            """
            self.EnemyCollide(lstEnemies)
        else:
            """
            So we move, we need to define if we hit super-power items first though
            """
            lstCols = pygame.sprite.spritecollide(self, power_group, True)

            if (len(lstCols) > 0):
                """
                We hit a power-up!
                """
                """
                1. define which type of power-up we hit
                2. run this depending on what powerup we hit
                    self.powerUpX = True
                    pygame.event.post(pygame.event.Event(POWER_UP_X_START,{}))
                3. Set a timer to figure out when the power-up ends, if it does
                    pygame.time.set_timer(POWER_UP_X_END, 0)
                    pygame.time.set_timer(POWER_UP_X_END, 3000)
                """
        pass

    def EnemyCollide(self, lstEnemiesHit):
        """
        This is the function when the player collides into an Enemy
        lstEnemiesHit is a list of Enemies the player has hit
        """

        if (len(lstEnemiesHit)<=0):
            """If the list is empty, just get out of here"""
            return

        for enemy in lstEnemiesHit:
            """
            Just in case we somehow hit more than one enemy, we loop through the list

            Here, we need to figure out a couple of things:
                1. on which direction did we hit the enemy
                    If hit from top:
                        Enemy Dies
                    If hit from side:
                        If the user in power_up_mode:
                            Depending on power-up either
                                - the enemy dies
                                - the user loses the power-up
                        If not in power-up mode:
                            The player dies
            """
        pass

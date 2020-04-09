import pygame
import basicSprite
from helpers import *
import time

class player(basicSprite.Sprite):
    """
    This is the sprite or the playable character
    """

    def __init__ (self.centerPoint, images):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.Sprite.__init__(self, centerPoint, images)

        """
        Initialize score, distance moved per turn, and how much is the current movement
        """
        self.score = 0

        self.x_dist = 1
        self.y_dist = 1

        self.xMove = 0
        self.yMove = 0

        """
        Initializes values for:
        self.maxHealth = 3
        self.currentHealth = 3
        self.damage     = 1
        self.quiver = False
        self.bombs = 0
        self.potions = 0
        """

    def MoveKeyDown(self, key):
        """
        This is the function that moves the x and y position of the player
        depending on what hey they pressed, it will move once update() is called.
        """

        if (key == D_DOWN):
            self.xMove += self.x_dist
        elif (key == A_DOWN):
            self.xMove += -self.x_dist
        elif (key == W_DOWN):
            self.yMove += -self.y_dist
        elif (key == S_DOWN):
            self.yMove += self.y_dist
        elif (key == J_DOWN):
            sword_Attack()
        elif (key == K_DOWN):
            shoot_Arrow()
        elif (key == L_DOWN):
            place_Bomb()
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

        lstEnemies = pygame.sprite.spritecollide(self, enemy_group, False)
        lstBackground = pygame.sprite.spritecollide(self, background_group, False)
        lstPassages = pygame.sprite.spritecollide(self, passage_group, False)
        if(len(lstEnemies) > 0):
            """
            We hit an Enemy!
            """
            self.EnemyCollide(lstEnemies)
        else:
            """
            define naythnig else we can hit
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
                if it has been hit, check if the user was atacking at to which side
                    if it was an attack that hit then kill monster
                    else take one healthpoint out of the player

                    if the players health reaches 0 hes dead
            """
        pass

    def sword_Attack(self):
        """
        This the function that has the character attack with his sword_Attack
        """
        pass

    def shoot_Arrow(self):
        """
        This the function that has the character shoots his arrow (if he has acquired them)
        """
        pass

    def place_Bomb(self):
        """
        This the function that has the character place his bomb (if he has)
        """
        pass

import pygame
import basicSprite
from helpers import *
import time

class Player(basicSprite.multipleSprite):
    """
    This is the sprite or the playable character
    """

    def __init__ (self, centerPoint, images, coords, direction):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, images)
        self.image_order = ['Basic_Down', 'Basic_Left', 'Basic_Right', 'Basic_Up']
        self.direction = direction
        self.coords = coords
        """
        if direction == 1:
            self.current_image = self.images[0]
        elif direction == 2:
            self.current_image = self.images[1]
        elif direction == 3:
            self.current_image = self.images[2]
        elif direction == 4:
            self.current_image = self.images[3]
            """
        self.x_dist = 68
        self.y_dist = 68

        self.xMove = 0
        self.yMove = 0

        self.maxHealth = 3
        self.currentHealth = 3
        self.damage = 1
        self.quiver = False
        self.bombs = 0
        self.potions = 0


    def MoveKeyDown(self, key):
        """
        This is the function that moves the x and y position of the player
        depending on what hey they pressed, it will move once update() is called.
        """

        if (key == K_d):
            self.xMove += self.x_dist
            self.image = self.images[2]
            self.coords = (self.coords[0] + 1, self.coords[1])
        elif (key == K_a):
            self.xMove += -self.x_dist
            self.image = self.images[1]
            self.coords = (self.coords[0] - 1, self.coords[1])
        elif (key == K_w):
            self.yMove += -self.y_dist
            self.image = self.images[3]
            self.coords = (self.coords[0], self.coords[1] - 1)
        elif (key == K_s):
            self.yMove += self.y_dist
            self.image = self.images[0]
            self.coords = (self.coords[0], self.coords[1] + 1)
        elif (key == K_j):
            sword_Attack()
        elif (key == K_k):
            shoot_Arrow()
        elif (key == K_l):
            place_Bomb()
        elif (key == K_i):
            drink_potion()


    def update(self, block_group, passage_group, breakable_group, troll_group, shooter_group, bat_group, projectile_group):
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

        lstEnemies = pygame.sprite.spritecollide(self, troll_group, False) + pygame.sprite.spritecollide(self, shooter_group, False) + pygame.sprite.spritecollide(self, bat_group, False)
        if(len(lstEnemies) > 0):
            """
            We hit an Enemy!
            """
            self.EnemyCollide(lstEnemies)


        if pygame.sprite.spritecollideany(self,block_group):
            """If we hit a block, stop movement"""
            self.rect.move_ip(-self.xMove,-self.yMove)

        lstPassages = pygame.sprite.spritecollide(self, passage_group, False)
        if (len(lstPassages) > 0):
            """If we hit a passage, move player"""
            print("PASSAGE")
            return lstPassages[0].next_screen, lstPassages[0].side


        lstBreakable = pygame.sprite.spritecollide(self, breakable_group, False)
        if (len(lstBreakable) > 0):
            if lstBreakable[0].broken:
                return lstBreakable[0].next_screen
            else:
                self.rect.move_ip(-self.xMove,-self.yMove)

        lstProjectiles = pygame.sprite.spritecollide(self, projectile_group, False)
        if (len(lstProjectiles) > 0):
           self.rect.move_ip(-self.xMove,-self.yMove)
           self.currentHealth -= 1

        self.xMove = 0
        self.yMove = 0


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

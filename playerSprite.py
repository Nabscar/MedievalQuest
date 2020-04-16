import pygame
import basicSprite
from helpers import *
import time

class Player(basicSprite.multipleSprite):
    """
    This is the sprite or the playable character
    """

    def __init__ (self, centerPoint, images, coords, direction, bombs = 0, potions = 0, health = 6):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, images)
        self.image_order = ['Basic_Down', 'Basic_Left', 'Basic_Right', 'Basic_Up']
        self.direction = direction
        self.coords = coords

        """distance moved with each keystroke"""
        self.x_dist = 64
        self.y_dist = 64
        """Current movement of player"""
        self.xMove = 0
        self.yMove = 0
        """King Characteristics"""
        self.maxHealth = 6
        self.currentHealth = health
        self.damage = 1
        self.quiver = 0 #Once he gets the quiver this becomes 8
        self.bombs = bombs
        self.potions = potions
        self.index = 0


    def MoveKeyDown(self, key):
        """
        This is the function that moves the x and y position of the player
        depending on what they they pressed, it will move once update() is called.
        """
        self.attacking = 0

        if (key == K_d):
            self.xMove += self.x_dist
            self.index = 2 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0] + 1, self.coords[1])
        elif (key == K_a):
            self.xMove += -self.x_dist
            self.index = 1 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0] - 1, self.coords[1])
        elif (key == K_w):
            self.yMove += -self.y_dist
            self.index = 3 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0], self.coords[1] - 1)
        elif (key == K_s):
            self.yMove += self.y_dist
            self.index = 0 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0], self.coords[1] + 1)
        elif (key == K_j):
            self.swordAttack()
        elif (key == K_k):
            self.shootArrow()
        elif (key == K_l):
            self.placeBomb()
        elif (key == K_i):
            self.drinkPotion()



    def update(self, block_group, passage_group, breakable_group, troll_group, shooter_group, bat_group, projectile_group, potion_group, bomb_group):
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
            return lstPassages[0].next_screen, lstPassages[0].side


        lstBreakable = pygame.sprite.spritecollide(self, breakable_group, False)
        if (len(lstBreakable) > 0):
            """We hit a breakable wall, if it is solid, treat as wall, if it is broken, treat as passage"""
            if lstBreakable[0].broken:
                return lstBreakable[0].next_screen, lstBreakable[0].side
            else:
                self.rect.move_ip(-self.xMove,-self.yMove)

        lstProjectiles = pygame.sprite.spritecollide(self, projectile_group, False)
        if (len(lstProjectiles) > 0):
            """If we are hit by a projectile, decrease life by one"""
           self.rect.move_ip(-self.xMove,-self.yMove)
           self.currentHealth -= 1

        lstPotions = pygame.sprite.spritecollide(self, potion_group, False)
        """IF we hit potion we add 3 potions to our inventory (unless we hit max, in which case we stop at 9)
        Also retunr flag so that the potion disappears from map"""
        if(len(lstPotions) > 0):
            if self.potions < 6:
                self.potions += 3
            else:
                self.potions = 9
            self.rect.move_ip(- self.xMove,-self.yMove)
            return "Potion"

        lstBombs = pygame.sprite.spritecollide(self, bomb_group, False)
        """IF we hit potion we add 3 bombs to our inventory (unless we hit max, in which case we stop at 9)
        Also retunr flag so that the potion disappears from map"""
        if(len(lstBombs) > 0):
            if self.bombs < 6:
                self.bombs += 3
            else:
                self.bombs = 9
            self.rect.move_ip(- self.xMove,-self.yMove)
            return "Bomb"

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
            if self.attacking == 0:
                self.currentHealth -= 1


    def swordAttack(self):
        """
        This the function that has the character attack with his sword_Attack
        """
        self.image = self.images[self.index + 4]
        self.attacking == self.index + 1

    def shootArrow(self):
        """
        This the function that has the character shoots his arrow (if he has acquired them)
        """
        if not self.quiver:
            return
        """
        Here we create the arrow, still need to figure it out
        """


    def placeBomb(self):
        """
        This the function that has the character place his bomb (if he has)
        """
        if self.bombs == 0:
            return
        else:
            self.bombs -= 1
        """
        Here we create the bomb, still need to figure it out
        """

    def drinkPotion(self):
        """
        If the player has potions, then drink one
        Reduce number of potions by one
        Increase health by one
        """
        if self.potions > 0 and self.currentHealth < self.maxHealth:
            self.currentHealth += 1
            self.potions -= 1

import pygame
import basicSprite
from helpers import *
import time

class Player(basicSprite.multipleSprite):
    """
    This is the sprite or the playable character
    """

    def __init__ (self, centerPoint, images, coords, direction, bombs = 1, potions = 0, health = 6):
        """
        Initializes the special characteristics of the playable character
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, images)
        self.image_order = ['Basic_Down', 'Basic_Left', 'Basic_Right', 'Basic_Up']
        self.direction = direction
        self.coords = coords

        """distance moved with each keystroke"""
        self.dist = 64
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
        self.bomb = None
        self.arrow = None
        self.placingBomb = False
        self.shooting = False
        self.attacking = 0


    def MoveKeyDown(self, key):
        """
        This is the function that moves the x and y position of the player
        depending on what they they pressed, it will move once update() is called.
        """
        self.attacking = 0

        if (key == K_d):
            self.xMove += self.dist
            self.index = 2 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0] + 1, self.coords[1])
        elif (key == K_a):
            self.xMove -= self.dist
            self.index = 1 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0] - 1, self.coords[1])
        elif (key == K_w):
            self.yMove -= self.dist
            self.index = 3 + self.quiver
            self.image = self.images[self.index]
            self.coords = (self.coords[0], self.coords[1] - 1)
        elif (key == K_s):
            self.yMove += self.dist
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

    def update(self, block_group, door_group, passage_group, breakable_group, troll_group, shooter_group, bat_group, projectile_group, potion_group, bomb_group, bowandquiver_group, boss_group):
        """
        Called to update the player sprite's position and state
        """
        if self.placingBomb == True:
            self.placingBomb = False
            return ("PlaceBomb", "bomb")

        if self.shooting == True:
            self.shooting = False
            return("Arrow", "arrow")

        if ((self.xMove == 0) and (self.yMove == 0) and (self.attacking == 0)):
            """
            If we aren't moveing just get out of here
            """
            return
        """
        We're moving!
        These if-eliffs are if they are attacking
        """
        if self.attacking == 1:
            self.yMove += self.dist
        elif self.attacking == 2:
            self.xMove -= self.dist
        elif self.attacking == 3:
            self.xMove += self.dist
        elif self.attacking == 4:
            self.yMove -= self.dist

        self.rect.move_ip(self.xMove,self.yMove)

        if pygame.sprite.spritecollideany(self,block_group) or pygame.sprite.spritecollideany(self, door_group):
            """If we hit a block, stop movement"""
            self.rect.move_ip(-self.xMove,-self.yMove)


        lstTrolls = pygame.sprite.spritecollide(self, troll_group, False)
        enemies = []
        if(len(lstTrolls) > 0):
            enemies.append(self.EnemyCollide(lstTrolls))
        else:
            enemies.append([])

        lstShooters = pygame.sprite.spritecollide(self, shooter_group, False)
        if(len(lstShooters) > 0):
            enemies.append(self.EnemyCollide(lstShooters))
        else:
            enemies.append([])

        lstBats = pygame.sprite.spritecollide(self, bat_group, False)
        if(len(lstBats) > 0):
            enemies.append(self.EnemyCollide(lstBats))
        else:
            enemies.append([])

        Boss = pygame.sprite.spritecollide(self, boss_group, False)
        boss_hit = []
        if(len(Boss) > 0):
            boss_hit.append(self.EnemyCollide(Boss))
        """
        This moves the player back if he Attacked
        """
        if self.attacking != 0:
            self.rect.move_ip(-self.xMove,-self.yMove)

        if len(boss_hit) > 0 and self.attacking != 0 :
            self.xMove = 0
            self.yMove = 0
            self.attacking = 0
            return ("BossHit", boss_hit)

        if len(enemies) > 0 and self.attacking != 0 :
            self.xMove = 0
            self.yMove = 0
            self.attacking = 0
            return ("Attacked", enemies)


        lstPassages = pygame.sprite.spritecollide(self, passage_group, False)
        if (len(lstPassages) > 0):
            """If we hit a passage, move player"""
            return ("Passage", lstPassages[0].next_screen, lstPassages[0].side)


        lstBreakable = pygame.sprite.spritecollide(self, breakable_group, False)
        if (len(lstBreakable) > 0):
            """We hit a breakable wall, if it is solid, treat as wall, if it is broken, treat as passage"""
            if lstBreakable[0].broken:
                return ("Passage", lstBreakable[0].next_screen, lstBreakable[0].side)
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
            self.rect.move_ip(-self.xMove,-self.yMove)
            return ("Potion", lstPotions[0])

        lstBombs = pygame.sprite.spritecollide(self, bomb_group, False)
        """IF we hit bomb we add 3 bombs to our inventory (unless we hit max, in which case we stop at 9)
        Also retunr flag so that the potion disappears from map"""
        if(len(lstBombs) > 0):
            if self.bombs < 6:
                self.bombs += 3
            else:
                self.bombs = 9
            self.rect.move_ip(-self.xMove,-self.yMove)
            return ("Bomb", lstBombs[0])

        BowAndQuiver = pygame.sprite.spritecollide(self, bowandquiver_group, False)
        """if we hit the bow and quiver, we change images and unlock the arrow"""
        if(len(BowAndQuiver) > 0):
            self.quiver = 8

        self.xMove = 0
        self.yMove = 0
        return ("None", "None")

    def EnemyCollide(self, lstEnemiesHit):
        """
        This is the function when the player collides into an Enemy
        lstEnemiesHit is a list of Enemies the player has hit
        """
        if (len(lstEnemiesHit)<=0):
            """If the list is empty, just get out of here"""
            return
        enemies = []

        for enemy in lstEnemiesHit:
            """
            Just in case we somehow hit more than one enemy, we loop through the list
            """
            if self.attacking == 0:
                self.currentHealth -= 1
            else:
                enemies.append(enemy)
        return enemies

    def swordAttack(self):
        """
        This the function that has the character attack with his sword_Attack
        """
        self.image = self.images[self.index + 4]
        self.attacking = self.index + 1

    def shootArrow(self):
        """
        This the function that has the character shoots his arrow (if he has acquired them)
        """
        if self.quiver == 0:
            return
        else:
            self.shooting = True


    def placeBomb(self):
        """
        This the function that has the character place his bomb (if he has)
        """
        if self.bombs > 0 and self.bomb == None:
            self.bombs -= 1
            self.placingBomb = True



    def drinkPotion(self):
        """
        If the player has potions, then drink one
        Reduce number of potions by one
        Increase health by one
        """
        if self.potions > 0 and self.currentHealth < self.maxHealth:
            self.currentHealth += 1
            self.potions -= 1

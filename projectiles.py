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
    def __init__ (self,centerPoint, images, direction, counter = 7, damage = 1):
        """
        Initializes the special characteristics of the basic projectile
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, images)
        self.counter = counter
        self.direction = direction
        self.done = False
        self.damage = damage
        self.dist = 64
        """Current movement of projectile"""
        self.xMove = 0
        self.yMove = 0
        if self.direction==0:#down
            self.yMove = self.dist
        elif self.direction==1:#Left
            self.xMove = -self.dist
        elif self.direction==2:#right
            self.xMove = self.dist
        elif self.direction==3:#up
            self.yMove = -self.dist

    def update(self, block_group, breakable_group, player_group, projectile_group, troll_group, shooter_group, bat_group, boss_group):
        flag = "done"
        self.counter -= 1
        if self.counter == 0:
            return(flag, "done")

        lstPlayer = pygame.sprite.spritecollide(self, player_group, False)
        if len(lstPlayer) > 0:
            return ("Player", lstPlayer)

        self.rect.move_ip(self.xMove,self.yMove) #This is what actually moves the projectile

        if (pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group)):
            """If we hit a block or a the player, its done, projectile should disappear"""
            return ("Wall", "done")

        lstProjectiles = pygame.sprite.spritecollide(self, projectile_group, False)
        if len(lstProjectiles) > self.projectile:
            return ("Projectile", lstProjectiles)

        enemies = []
        lstTroll = pygame.sprite.spritecollide(self, troll_group, False)
        if len(lstTroll) > 0:
            flag = "Enemy"
        enemies.append(lstTroll)
        lstShooter = pygame.sprite.spritecollide(self, shooter_group, False)
        if len(lstShooter) > 0:
            flag = "Enemy"
        enemies.append(lstShooter)
        lstBat = pygame.sprite.spritecollide(self, bat_group, False)
        if len(lstBat) > 0:
            flag = "Enemy"
        enemies.append(lstBat)
        if flag == "Enemy":
            return(flag, enemies)

        boss = pygame.sprite.spritecollide(self, boss_group, False)
        if len(boss) > 0:
            flag = "BossHit"
        if flag == "BossHit":
            return (flag, boss)

        return None

class Ball(Projectile):

    def __init__ (self, centerPoint, images, direction, counter = 5, damage = 1):
        """
        Initializes the special characteristics of the ball projectile
        """
        Projectile.__init__(self, centerPoint, images, direction, counter, damage)
        self.image = self.images[0]
        self.projectile = 1

class Javelin(Projectile):

        def __init__ (self, centerPoint, images, direction, counter = 5, damage = 1):
            """
            Initializes the special characteristics of the javelin projectile
            """
            Projectile.__init__(self, centerPoint, images, direction, counter, damage)
            self.damage = damage
            self.image_order = ["Down", "Left", "Right", "Up"]
            """
            directions go in same order as image order
            """
            self.image = self.images[self.direction]
            self.projectile = 1

class Arrow(Projectile):

        def __init__ (self, centerPoint, images, direction, counter = 5, damage = 1):
            """
            Initializes the special characteristics of the arrow projectile
            """
            Projectile.__init__(self, centerPoint, images, direction, counter)
            self.damage = damage
            self.image_order = ["Down", "Left", "Right", "Up"]
            """
            directions go in same order as image order
            """
            self.image = self.images[self.direction ]
            self.projectile = 0

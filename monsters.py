import pygame
import basicSprite
import random
from projectiles import Javelin, Ball

"""
This python script creates three classes that create the Monsters
It should only be missing Boss
"""

class Troll(basicSprite.multipleSprite):
    """
    This is where we create the Green Monsters
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, images, coords, direction = random.randint(1,4)):
        """
        use the initialization of the basic Sprite and the initialize any specific thigns for this enemy
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, images)
        """start the basic initialization"""
        self.original_rect = pygame.Rect(self.rect)
        self.image_order = ["Down", "Left1", "Left2", "Right1", "Right2", "Up"]

        self.coords = coords


        """
        Initialize the direction
        1 = down
        2 = Left
        3 = right
        4 = up
        """
        self.direction = direction
        if self.direction == 1:
            self.image = self.images[0]
        elif self.direction == 2:
            self.image = self.images[1]
        elif self.direction == 3:
            self.image = self.images[3]
        elif self.direction == 4:
            self.image = self.images[5]

        self.dist = 64

        self.counter = 0

        self.step = 1

    def update(self, block_group, character_coords, breakable_group, passage_group):
        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        """The idea of returning the javelin is the following: if there is no throw, then it will return None, else, it will returna  javelin we can add to the update group"""

        if self.counter != 0:
            self.counter -= 1

        xMove,yMove = 0,0

        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        if character_coords[0] == self.coords[0]:#they are in th esame vertical
            diff = character_coords[1] - self.coords[1]
            if diff > 0 and  self.counter == 0:#right
                self.counter = 5
                return ("Shoot", (self.rect.center, 2))
            elif diff < 0 and  self.counter == 0:#left
                self.counter = 5
                return ("Shoot", (self.rect.center, 1))
        if character_coords[1] == self.coords[1]:#they are in teh same horizaontal
            diff = character_coords[0] - self.coords[0]
            if diff < 0 and  self.counter == 0:#down
                self.counter = 5
                return ("Shoot", (self.rect.center, 3))
            elif diff > 0 and  self.counter == 0:#up
                self.counter = 5
                return ("Shoot", (self.rect.center, 0))

        if self.counter == 0:
            if self.direction==1:#down
                yMove = self.dist
                self.coords = (self.coords[0], self.coords[1] + 1)
            elif self.direction==2:#Left
                xMove = -self.dist
                self.coords = (self.coords[0] - 1, self.coords[1])
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[1]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[2]
            elif self.direction==3:#right
                xMove = self.dist
                self.coords = (self.coords[0] + 1, self.coords[1])
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[3]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[4]
            elif self.direction==4:#up
                yMove = -self.dist
                self.coords = (self.coords[0], self.coords[1] - 1)
            self.rect.move_ip(xMove,yMove) #This is 2what actually moves the character
            if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group) or pygame.sprite.spritecollideany(self, passage_group):
                """If we hit a block, don’t move – reverse the movement"""
                self.rect.move_ip(-xMove,-yMove)
                if self.direction == 1:
                    self.direction = 4
                elif self.direction == 2:
                    self.direction = 3
                elif self.direction == 3:
                    self.direction = 2
                elif self.direction == 4:
                    self.direction = 1

class Bat(basicSprite.multipleSprite):
    """
    This is where we create the Bats
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, image, coords, direction = random.randint(1,4)):
        """
        use the initialization of the basic Sprite and the initialize any specific thigns for this enemy
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, image)
        """start the basic initialization"""
        self.original_rect = pygame.Rect(self.rect)
        self.image_order = ["Down1", "Down2", "Left1", "Left2", "Right1", "Right2", "Up1", "Up2"]

        self.coords = coords

        self.dead = False

        """
        Initialize the direction
        1 = down
        2 = Left
        3 = right
        4 = up
        """
        self.direction = direction
        if self.direction == 1:
            self.image = self.images[0]
        elif self.direction == 2:
            self.image = self.images[2]
        elif self.direction == 3:
            self.image = self.images[4]
        elif self.direction == 4:
            self.image = self.images[6]

        self.dist = 64

        self.step = 1

    def update(self, block_group, character_coords, breakable_group, passage_group):
        """
        This function is the one that will move an dupdate the position of the monsters
        It is called each "cycle" of gameplay to show that they move
        """
        if self.dead:
            return
        xMove,yMove = 0,0


        """First it check is the enemy can see the player. If he can, then he will move towards the character"""
        if character_coords[0] == self.coords[0] :#Check if enemy sees character horizontally
            diff = character_coords[0] - self.coords[0]
            if diff > 0:#Enemy looking left and character is on the Left
                self.direction = 2
            elif diff < 0:#Enemy looking right and character is on the right
                self.direction = 4
        elif character_coords[1] == self.coords[1]:#Check if enemy sees character vertically
            diff = character_coords[1] - self.coords[1]
            if diff < 0:#Enemy looking up and character is up
                self.direction = 1
            elif  diff > 0:#Enemy looking down and character is down
                self.direction = 3

        #either we move towards the character or we move randomly
        if self.direction==1:#down
            yMove = self.dist
            self.coords = (self.coords[0], self.coords[1] + 1)
            if self.step == 1:
                step = 2
                self.image = self.images[0]
            elif self.step == 2:
                step = 1
                self.image = self.images[1]
        elif self.direction==2:#Left
            xMove = self.dist
            self.coords = (self.coords[0] - 1, self.coords[1])
            if self.step == 1:
                step = 2
                self.image = self.images[2]
            elif self.step == 2:
                step = 1
                self.image = self.images[3]
        elif self.direction==3:#right
            xMove = -self.dist
            self.coords = (self.coords[0] + 1, self.coords[1])
            if self.step == 1:
                step = 2
                self.image = self.images[4]
            elif self.step == 2:
                step = 1
                self.image = self.images[5]
        elif self.direction==4:#up
            yMove = -self.dist
            self.coords = (self.coords[0], self.coords[1] - 1)
            if self.step == 1:
                step = 2
                self.image = self.images[6]
            elif self.step == 2:
                step = 1
                self.image = self.images[7]

        self.rect.move_ip(xMove,yMove) #This is what actually moves the character
        if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group) or pygame.sprite.spritecollideany(self, passage_group):
            """If we hit a block, don’t move – reverse the movement"""
            self.rect.move_ip(-xMove,-yMove)
            if self.direction == 1:
                self.direction = 4
            elif self.direction == 2:
                self.direction = 3
            elif self.direction == 3:
                self.direction = 2
            elif self.direction == 4:
                self.direction = 1

    def die(self, ground_image):
        """
        This function establishes what happens when a enemy is killed
        this means he is set do dead (so update cant be called) and the image is set as a ground image
        """
        self.dead = True
        self.images = ground_image

class Shooter(basicSprite.multipleSprite):
    """
    This is where we create the Shooters
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, image, coords, direction = random.randint(1,4)):
        """
        use the initialization of the basic Sprite and the initialize any specific thigns for this enemy
        """
        basicSprite.multipleSprite.__init__(self, centerPoint, image)
        """start the basic initialization"""
        self.original_rect = pygame.Rect(self.rect)
        self.image_order = ["Down1", "Down2", "Left1", "Left2", "Right1", "Right2", "Up1", "Up2"]

        self.coords = coords

        self.dead = False

        self.attacking = False
        """
        Initialize the direction
        1 = down
        2 = Left
        3 = right
        4 = up
        """
        self.direction = direction
        if self.direction == 1:
            self.image = self.images[0]
        elif self.direction == 2:
            self.image = self.images[2]
        elif self.direction == 3:
            self.image = self.images[4]
        elif self.direction == 4:
            self.image = self.images[6]

        self.dist = 64

        self.counter = False

        self.step = 1
        pass

    def update(self, block_group, character_coords, breakable_group, passage_group):
        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        """The idea of returning the javelin is the following: if there is no throw, then it will return None, else, it will returna  javelin we can add to the update group"""

        if self.counter != 0:
            self.counter -= 1

        xMove,yMove = 0,0

        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        if character_coords[0] == self.coords[0]:#they are in th esame vertical
            diff = character_coords[1] - self.coords[1]
            if diff > 0 and  self.counter == 0:#right
                self.counter = 5
                return ("Shoot", (self.rect.center, 2))
            elif diff < 0 and  self.counter == 0:#left
                self.counter = 5
                return ("Shoot", (self.rect.center, 1))
        if character_coords[1] == self.coords[1]:#they are in teh same horizaontal
            diff = character_coords[0] - self.coords[0]
            if diff < 0 and  self.counter == 0:#down
                self.counter = 5
                return ("Shoot", (self.rect.center, 3))
            elif diff > 0 and  self.counter == 0:#up
                self.counter = 5
                return ("Shoot", (self.rect.center, 0))

        if self.counter == 0:
            if self.direction==1:#down
                yMove = self.dist
                self.coords = (self.coords[0], self.coords[1] + 1)
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[0]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[1]
            elif self.direction==2:#Left
                xMove = self.dist
                self.coords = (self.coords[0] - 1, self.coords[1])
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[2]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[3]
            elif self.direction==3:#right
                xMove = -self.dist
                self.coords = (self.coords[0] + 1, self.coords[1])
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[4]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[5]
            elif self.direction==4:#up
                yMove = -self.dist
                self.coords = (self.coords[0], self.coords[1] - 1)
                if self.step == 1:
                    self.step = 2
                    self.image = self.images[6]
                elif self.step == 2:
                    self.step = 1
                    self.image = self.images[7]

            self.rect.move_ip(xMove,yMove) #This is what actually moves the character
        if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group) or pygame.sprite.spritecollideany(self, passage_group):
                """If we hit a block, don’t move – reverse the movement"""
                self.rect.move_ip(-xMove,-yMove)
                if self.direction == 1:
                    self.direction = 4
                elif self.direction == 2:
                    self.direction = 3
                elif self.direction == 3:
                    self.direction = 2
                elif self.direction == 4:
                    self.direction = 1


#class Boss(basicSprite.Sprite):

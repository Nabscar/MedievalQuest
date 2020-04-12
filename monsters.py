import pygame
import basicSprite
import random
import projectiles

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
            self.image = self.images[1]
        elif self.direction == 3:
            self.image = self.images[3]
        elif self.direction == 4:
            self.image = self.images[5]

        self.dist = 1

        self.thrown = False

        self.step = 1
        pass

    def update(self, block_group, character_coords, centerPoint, javelin_images, breakable_group, passage_group):
        """
        This function is the one that will move an dupdate the position of the monsters
        It is called each "cycle" of gameplay to show that they move
        """
        if self.dead:
            return
        xMove,yMove = 0,0

        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        if character_coords[0] == self.coords[0]:#Check if enemy sees character horizontally
            dif = character_coords[0] - self.coords[0]
            if self.direction == 2 and diff > 0 and not self.thrown:#Enemy looking left and character is on the Left
                throw_javelin(centerPoint, javelin_images, self.direction)
                self.thrown = True
            elif self.direction == 4 and diff < 0 and not self.thrown:#Enemy looking right and character is on the right
                throw_javelin(centerPoint, javelin_images, self.direction)
                self.thrown = True
        elif character_coords[1] == self.coords[1]:#Check if enemy sees character vertically
            dif = character_coords[1] - self.coords[1]
            if self.direction == 1 and diff < 0 and not self.thrown:#Enemy looking up and character is up
                throw_javelin(centerPoint, javelin_images, self.direction)
                self.thrown = True
            elif self.direction == 3 and diff > 0 and not self.thrown:#Enemy looking down and character is down
                throw_javelin(centerPoint, javelin_images, self.direction)
                self.thrown = True
        else:#If we didnt see the character, we move
            if self.direction==1:#down
                yMove = self.dist
            elif self.direction==2:#Left
                xMove = -self.dist
                if self.step == 1:
                    step = 2
                    self.image = self.images[1]
                elif self.step == 2:
                    step = 1
                    self.image = self.images[2]
            elif self.direction==3:#right
                xMove = -self.dist
                if self.step == 1:
                    step = 2
                    self.image = self.images[3]
                elif self.step == 2:
                    step = 1
                    self.image = self.images[4]
            elif self.direction==4:#up
                yMove = -self.dist

            self.rect.move_ip(xMove,yMove) #This is what actually moves the character
            if pygame.sprite.spritecollideany(self, block_group) or pygame.sprite.spritecollideany(self, breakable_group) or pygame.sprite.spritecollideany(self, passage_group):
                """If we hit a block, don’t move – reverse the movement"""
                self.rect.move_ip(-xMove,-yMove)
                self.direction += 2
                self.direction %= 4
        pass

    def throw_javelin(self, centerPoint, javelin_images, direction):
        """
        This is the function that Throws the Javelin
        """
        javelin = Javelin(centerPoint, javelin_images, direction)
        pass

    def javelin_fell(self):
        """
        This function tells the enemy he can now throw another javelin
        """
        self.thrown = False
        pass

    def die(self, ground_image):
        """
        This function establishes what happens when a enemy is killed
        this means he is set do dead (so update cant be called) and the image is set as a ground image
        it is also removed from the enemy_group list
        """
        self.dead = True
        self.images = ground_image

        pass

class Bat(basicSprite.multipleSprite):
    """
    This is where we create the Bats
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, images, coords, direction = random.randint(1,4)):
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

        self.dist = 1

        self.step = 1
        pass

    def update(self, block_group, character_coords, breakable_group, passage_group):
        """
        This function is the one that will move an dupdate the position of the monsters
        It is called each "cycle" of gameplay to show that they move
        """
        if self.dead:
            return
        xMove,yMove = 0,0

        self.direction = random.randint(1,4)#set random way to move

        """First it check is the enemy can see the player. If he can, then he will move towards the character"""
        if character_coords[0] == self.coords[0] :#Check if enemy sees character horizontally
            dif = character_coords[0] - self.coords[0]
            if diff > 0:#Enemy looking left and character is on the Left
                self.direction = 2
            elif diff < 0:#Enemy looking right and character is on the right
                self.direction = 4
        elif character_coords[1] == self.coords[1]:#Check if enemy sees character vertically
            dif = character_coords[1] - self.coords[1]
            if diff < 0:#Enemy looking up and character is up
                self.direction = 1
            elif  diff > 0:#Enemy looking down and character is down
                self.direction = 3

        #either we move towards the character or we move randomly
        if self.direction==1:#down
            yMove = self.dist
            if self.step == 1:
                step = 2
                self.image = self.images[0]
            elif self.step == 2:
                step = 1
                self.image = self.images[1]
        elif self.direction==2:#Left
            xMove = self.dist
            if self.step == 1:
                step = 2
                self.image = self.images[2]
            elif self.step == 2:
                step = 1
                self.image = self.images[3]
        elif self.direction==3:#right
            xMove = -self.dist
            if self.step == 1:
                step = 2
                self.image = self.images[4]
            elif self.step == 2:
                step = 1
                self.image = self.images[5]
        elif self.direction==4:#up
            yMove = -self.dist
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
            self.direction += 2
            self.direction %= 4
            pass

    def die(self, ground_image):
        """
        This function establishes what happens when a enemy is killed
        this means he is set do dead (so update cant be called) and the image is set as a ground image
        """
        self.dead = True
        self.images = ground_image

        pass

class Shooter(basicSprite.multipleSprite):
    """
    This is where we create the Shooters
    Pretty sure this one is done
    """
    def __init__ (self, centerPoint, images, coords, direction = random.randint(1,4)):
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

        self.dist = 1

        self.thrown = False

        self.step = 1
        pass

    def update(self, block_group, character_coords, centerPoint, ball_image, breakable_group, passage_group):
        """
        This function is the one that will move an dupdate the position of the monsters
        It is called each "cycle" of gameplay to show that they move
        """
        if self.dead:
            return
        xMove,yMove = 0,0

        """First it check is the enemy can see the player. If he can, then the character will not move, it will throw the javelin"""
        if character_coords[0] == self.coords[0]:#Check if enemy sees character horizontally
            dif = character_coords[0] - self.coords[0]
            if self.direction == 2 and diff > 0 and not self.thrown:#Enemy looking left and character is on the Left
                shoot_ball(centerPoint, ball_image, self.direction)
                self.thrown = True
            elif self.direction == 4 and diff < 0 and not self.thrown:#Enemy looking right and character is on the right
                shoot_ball(centerPoint, ball_image, self.direction)
                self.thrown = True
        elif character_coords[1] == self.coords[1]:#Check if enemy sees character vertically
            dif = character_coords[1] - self.coords[1]
            if self.direction == 1 and diff < 0 and not self.thrown:#Enemy looking up and character is up
                shoot_ball(centerPoint, ball_image, self.direction)
                self.thrown = True
            elif self.direction == 3 and diff > 0 and not self.thrown:#Enemy looking down and character is down
                shoot_ball(centerPoint, ball_image, self.direction)
                self.thrown = True
        else:#If we didnt see the character, we move
            if self.direction==1:#down
                yMove = self.dist
                if self.step == 1:
                    step = 2
                    self.image = self.images[0]
                elif self.step == 2:
                    step = 1
                    self.image = self.images[1]
            elif self.direction==2:#Left
                xMove = self.dist
                if self.step == 1:
                    step = 2
                    self.image = self.images[2]
                elif self.step == 2:
                    step = 1
                    self.image = self.images[3]
            elif self.direction==3:#right
                xMove = -self.dist
                if self.step == 1:
                    step = 2
                    self.image = self.images[4]
                elif self.step == 2:
                    step = 1
                    self.image = self.images[5]
            elif self.direction==4:#up
                yMove = -self.dist
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
                self.direction += 2
                self.direction %= 4
        pass

    def shoot_ball(self, centerPoint, ball_image, direction):
        """
        This is the function that Throws the Javelin
        """
        ball = Ball(centerPoint, ball_image, direction)
        pass

    def ball_fell(self):
        """
        This function tells the enemy he can now throw another javelin
        """
        self.thrown = False
        pass

    def die(self, ground_image):
        """
        This function establishes what happens when a enemy is killed
        this means he is set do dead (so update cant be called) and the image is set as a ground image
        """
        self.dead = True
        self.images = ground_image

        pass

#class Boss(basicSprite.Sprite):

import os, sys
sys.path.append('/home/nabih/Documents/SoftDes/MedievalQuest/levels')


import pygame
import level11
import level12
import level13
import level21
import level22
import level23
import level31
import level32
import level33
import cave22
import cave31
from basicSprite import *
from pygame.locals import *
from helpers import *
from playerSprite import Player
from monsters import Troll, Bat, Shooter
from projectiles import Javelin, Ball, Arrow
from backgrounds import BreakableBackground, Passage
from basicSprite import singleSprite, multipleSprite
import time

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

BLOCK_SIZE = 64

class MainQuest:
    """
    The Main PyGame Class – This class handles the main
    initialization and creating of the Game.
    """

    def __init__(self, width=768,height=704):
        """
        Initialize PyGame
        """
        pygame.init()
        self.started = False
        """
        Set the window Size
        """
        self.width = width
        self.height = height
        """
        Create the Screen
        """
        self.screen = pygame.display.set_mode((self.width, self.height))
        """
        Set current level
        """
        self.current_level = 22


    def MainLoop(self):
        """
        Load all of our Sprites
        """
        self.LoadSprites("T")
        """
        Create Background
        """
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        """
        We could draw here parts that would only need to be drawn once
        But since levels change there is no need for that
        """

        pygame.display.flip()
        """
        Main Loop of game
        """
        while 1:
            self.started = True

            self.player_group.clear(self.screen,self.background)
            self.troll_group.clear(self.screen,self.background)
            self.bat_group.clear(self.screen,self.background)
            self.shooter_group.clear(self.screen,self.background)
            self.projectile_group.clear(self.screen, self.background)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif self.player.currentHealth == 0:
                    """
                    What happens when the player dies
                    """
                    print("GAME OVER")
                    sys.exit()

                elif self.current_level == 13:
                    """
                    The player Won
                    Quit the Game
                    """
                    print("You Have reached the Castle! You Won!")
                    sys.exit()

                elif event.type == KEYDOWN:
                    """
                    If player didnt quit, die, or win, then he moves
                    What happens when the key is pressed
                    """
                    if ((event.key == K_a)
                    or (event.key == K_w)
                    or (event.key == K_d)
                    or (event.key == K_s)
                    or (event.key == K_j)
                    or (event.key == K_k)
                    or (event.key == K_l)
                    or (event.key == K_i)):
                        self.player.MoveKeyDown(event.key)

                """
                Update the player sprite and all other sprites
                """
                player_flag = self.player.update(self.block_group, self.passage_group, self.breakable_group, self.troll_group, self.shooter_group, self.bat_group, self.projectile_group, self.potion_group, self.pickup_bomb_group)
                if self.player.bomb != None:
                    bomb_flag = self.player.bomb.update(self.breakable_group, self.troll_group, self.shooter_group, self.bat_group)
                else:
                    bomb_flag = None
                if (len(self.troll_group.sprites()) > 0):
                    javelin = self.troll_group.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)
                    """Still dont know how to make these work
                    print(javelin)
                    print(javelin == None)
                    if not(javelin == None):
                        temp = Javelin(javelin(0), self.img_list[self.level.JAVELIN],7, javelin(1))
                        self.projectile_group.add(javelin)
                        print("He threw the javelin!")
                        """

                if (len(self.bat_group.sprites()) > 0):
                    self.bat_group.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)

                if (len(self.shooter_group.sprites()) > 0):
                    ball = self.shooter_group.update(self.block_group, self.player.coords, self.img_list[self.level.BALL], self.breakable_group, self.passage_group)

                if (len(self.projectile_group.sprites()) > 0):
                    self.projectile_group.update(self.block_group, self.breakable_group, self.player_group, self.projectile_group)



                """
                Update the inventory
                """
                self.bomb_number.update(self.player.bombs)
                self.potion_number.update(self.player.potions)
                self.heart1_group.update(self.player.currentHealth - 3)
                self.heart2_group.update(self.player.currentHealth - 1)
                self.heart3_group.update(self.player.currentHealth + 1)
                """check bomb_flag"""
                if bomb_flag == True:
                    self.player.bomb = None
                    self.bomb_group.empty()
                """If the player has collided against something specific, we get a flag as player_flag, depending on the flag, do different things"""
                if player_flag == "Potion":
                    self.potion_group.empty()
                elif player_flag == "Bomb":
                    self.pickup_bomb_group.empty()
                elif player_flag == "PlaceBomb":
                    bomb = Bomb(self.player.rect.center, self.img_list[self.level.BOMB])
                    self.player.bomb = bomb
                    self.bomb_group.add(bomb)
                elif player_flag != None:
                    self.current_level = player_flag[0]
                    """
                    Load all of our Sprites
                    """
                    self.LoadSprites(player_flag[1])
                    """
                    Create Background
                    """
                    self.background = pygame.Surface(self.screen.get_size())
                    self.background = self.background.convert()
                    self.background.fill((0,0,0))
                    """
                    We could draw here parts that would only need to be drawn once
                    But since levels change there is no need for that
                    """

                    pygame.display.flip()

                """Do the Drawing"""
                textpos = 0
                self.screen.blit(self.background, (0, 0))


                reclist = self.block_group.draw(self.screen)
                reclist += self.passage_group.draw(self.screen)
                reclist += self.crossable_group.draw(self.screen)
                reclist +=  self.breakable_group.draw(self.screen)
                reclist +=  self.troll_group.draw(self.screen)
                reclist +=  self.bat_group.draw(self.screen)
                reclist +=  self.shooter_group.draw(self.screen)
                reclist +=  self.projectile_group.draw(self.screen)
                reclist +=  self.player_group.draw(self.screen)
                reclist +=  self.inventory_group.draw(self.screen)
                reclist +=  self.bomb_number.draw(self.screen)
                reclist +=  self.potion_number.draw(self.screen)
                reclist +=  self.heart1_group.draw(self.screen)
                reclist +=  self.heart2_group.draw(self.screen)
                reclist +=  self.heart3_group.draw(self.screen)
                reclist += self.potion_group.draw(self.screen)
                reclist += self.pickup_bomb_group.draw(self.screen)
                reclist += self.bomb_group.draw(self.screen)


                pygame.display.update(reclist)

    def LoadSprites(self, side):
        """
        Load all of the sprites that we need
        Calculate the Center Point Offset
        """
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)
        """
        Load the level
        The coding for which level is happening is the following:
            The main nine level have 2 numbers, which show row and column
                for example: 11 is the level in the topmost left corner
            If there is a third number, that mean that that is teh cave that sprawns from that level
                for example: 311 is the cave that come from level 31
        """
        if self.current_level == 11:
            self.level = level11.level11(side)
        if self.current_level == 12:
            self.level = level12.level12(side)
        if self.current_level == 13:
            self.level = level13.level13(side)
        if self.current_level == 21:
            self.level = level21.level21(side)
        if self.current_level == 22:
            self.level = level22.level22(side)
        if self.current_level == 23:
            self.level = level23.level23(side)
        if self.current_level == 31:
            self.level = level31.level31(side)
        if self.current_level == 32:
            self.level = level32.level32(side)
        if self.current_level == 33:
            self.level = level33.level33(side)
        if self.current_level == 221:
            self.level = cave22.cave22(side)
        if self.current_level == 311:
            self.level = cave31.cave31(side)


        """This sets which side the player is entering on. THis helps the level render the player on the appropriate entrance to the screen"""
        if side == "T":
            self.layout = self.level.getLayoutTop()
        elif side == "B":
            self.layout = self.level.getLayoutBottom()
        elif side == "L":
            self.layout = self.level.getLayoutLeft()
        elif side == "R":
            self.layout = self.level.getLayoutRight()
        elif side == "C":
            self.layout = self.level.getLayoutCave()


        self.img_list = self.level.getSprites()

        """
        Create the groups for all the updateable sprites
        """
        self.block_group = pygame.sprite.RenderUpdates()
        self.passage_group = pygame.sprite.RenderUpdates()
        self.crossable_group = pygame.sprite.RenderUpdates()
        self.breakable_group = pygame.sprite.RenderUpdates()
        self.inventory_group = pygame.sprite.RenderUpdates()
        self.bomb_number = pygame.sprite.RenderUpdates()
        self.potion_number = pygame.sprite.RenderUpdates()
        self.heart1_group = pygame.sprite.RenderUpdates()
        self.heart2_group = pygame.sprite.RenderUpdates()
        self.heart3_group = pygame.sprite.RenderUpdates()
        self.troll_group = pygame.sprite.RenderUpdates()
        self.bat_group = pygame.sprite.RenderUpdates()
        self.shooter_group = pygame.sprite.RenderUpdates()
        self.projectile_group = pygame.sprite.RenderUpdates()
        self.potion_group = pygame.sprite.RenderUpdates()
        self.pickup_bomb_group = pygame.sprite.RenderUpdates()
        self.bomb_group = pygame.sprite.RenderUpdates()

        """Go through all the level array"""
        for y in range(len(self.layout)):
            for x in range(len(self.layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                """
                Read the level array to define what comes in which place of the Screen
                Create the sprites necessary to fill the parts we just read
                """

                """Basic grounds"""
                if self.layout[y][x]==self.level.GROUND:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                elif self.layout[y][x]==self.level.CAVEGROUND:
                    ground = singleSprite(centerPoint, self.img_list[self.level.CAVEGROUND])
                    self.crossable_group.add(ground)

                    """Basic Block groups"""
                elif self.layout[y][x]==self.level.GRASS:
                    grass = singleSprite(centerPoint, self.img_list[self.level.GRASS])
                    self.block_group.add(grass)
                elif self.layout[y][x]==self.level.WATER:
                    water = singleSprite(centerPoint, self.img_list[self.level.WATER])
                    self.block_group.add(water)
                elif self.layout[y][x]==self.level.TREE:
                    tree = singleSprite(centerPoint, self.img_list[self.level.TREE])
                    self.block_group.add(tree)
                elif self.layout[y][x]==self.level.WALL:
                    wall = singleSprite(centerPoint, self.img_list[self.level.WALL])
                    self.block_group.add(wall)

                    """Breakable Walls"""
                elif self.layout[y][x]==self.level.BREAKABLE_WALL:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL], (self.current_level * 10 + 1), "C", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BROKEN_WALL:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL], (self.current_level * 10 + 1), "C", True) #create breakable
                    self.breakable_group.add(breakable)

                    """Passages"""
                elif self.layout[y][x]==self.level.PASSAGE_T:
                    passage = Passage(centerPoint, self.img_list[self.level.PASSAGE_T], (self.current_level - 10), "T")#create passage to top
                    self.passage_group.add(passage)
                elif self.layout[y][x]==self.level.PASSAGE_B:
                    passage = Passage(centerPoint, self.img_list[self.level.PASSAGE_B], (self.current_level + 10), "B")#create passage to bottom
                    self.passage_group.add(passage)
                elif self.layout[y][x]==self.level.PASSAGE_L:
                    passage = Passage(centerPoint, self.img_list[self.level.PASSAGE_L], (self.current_level - 1), "L")#create passage to left
                    self.passage_group.add(passage)
                elif self.layout[y][x]==self.level.PASSAGE_R:
                    passage = Passage(centerPoint, self.img_list[self.level.PASSAGE_R], (self.current_level + 1), "R")#create passage to right
                    self.passage_group.add(passage)
                elif self.layout[y][x]==self.level.PASSAGE_C:
                    passage = Passage(centerPoint, self.img_list[self.level.PASSAGE_C], int(((self.current_level- 1)/10)), "C")#create passage to right
                    self.passage_group.add(passage)
                elif self.layout[y][x]==self.level.CAVEENTRANCE:
                    cave = Passage(centerPoint, self.img_list[self.level.CAVEENTRANCE], (self.current_level * 10 + 1), "C")#create passage to right
                    self.passage_group.add(cave)

                    """Enemies"""
                elif self.layout[y][x]==self.level.BAT_V:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    bat = Bat(centerPoint, self.img_list[self.level.BAT_V], (x, y), 1)#create bat
                    self.bat_group.add(bat)
                elif self.layout[y][x]==self.level.BAT_H:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    bat = Bat(centerPoint, self.img_list[self.level.BAT_H], (x, y), 2)#create bat
                    self.bat_group.add(bat)
                elif self.layout[y][x]==self.level.TROLL_V:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    troll = Troll(centerPoint, self.img_list[self.level.TROLL_V], (x, y), 1)#create troll
                    self.troll_group.add(troll)
                elif self.layout[y][x]==self.level.TROLL_H:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    troll = Troll(centerPoint, self.img_list[self.level.TROLL_H], (x, y), 2)#create troll
                    self.troll_group.add(troll)
                elif self.layout[y][x]==self.level.SHOOTER_V:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    shooter = Shooter(centerPoint, self.img_list[self.level.SHOOTER_V], (x, y), 1)#create shooter
                    self.shooter_group.add(shooter)
                elif self.layout[y][x]==self.level.SHOOTER_H:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    shooter = Shooter(centerPoint, self.img_list[self.level.SHOOTER_H], (x, y), 2)#create shooter
                    self.shooter_group.add(shooter)

                    """Player"""
                elif self.layout[y][x]==self.level.PLAYER_OW:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    if self.started:
                        self.player = Player(centerPoint, self.img_list[self.level.PLAYER_OW], (x,y), 4, self.player.bombs, self.player.potions, self.player.currentHealth)
                    else:
                        self.player = Player(centerPoint, self.img_list[self.level.PLAYER_OW], (x,y), 4)
                elif self.layout[y][x]==self.level.PLAYER_C:
                    ground = singleSprite(centerPoint, self.img_list[self.level.CAVEGROUND])
                    self.crossable_group.add(ground)
                    if self.started:
                        self.player = Player(centerPoint, self.img_list[self.level.PLAYER_C], (x,y), 4, self.player.bombs, self.player.potions, self.player.currentHealth)
                    else:
                        self.player = Player(centerPoint, self.img_list[self.level.PLAYER_C], (x,y), 4)

                    """Projectiles and Items"""
                elif self.layout[y][x]==self.level.PICKPOTION:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    potion = Potion(centerPoint, self.img_list[self.level.PICKPOTION])
                    self.potion_group.add(potion)
                elif self.layout[y][x]==self.level.PICKBOMB:
                    ground = singleSprite(centerPoint, self.img_list[self.level.CAVEGROUND])
                    self.crossable_group.add(ground)
                    bomb = Bomb(centerPoint, self.img_list[self.level.PICKBOMB])
                    self.pickup_bomb_group.add(bomb)

                    """Inventory"""
                elif self.layout[y][x]==self.level.BLANK:
                    blank = singleSprite(centerPoint, self.img_list[self.level.BLANK])
                    self.inventory_group.add(blank)
                elif self.layout[y][x]==self.level.BOMB:
                    blank = singleSprite(centerPoint, self.img_list[self.level.BOMB])
                    self.inventory_group.add(blank)
                elif self.layout[y][x]==self.level.BOMBNUM:
                    nums = Numbers(centerPoint, self.img_list[self.level.BOMBNUM], self.player.bombs)
                    self.bomb_number.add(nums)
                elif self.layout[y][x]==self.level.POTION:
                    potion = singleSprite(centerPoint, self.img_list[self.level.POTION])
                    self.inventory_group.add(potion)
                elif self.layout[y][x]==self.level.POTIONNUM:
                    nums = Numbers(centerPoint, self.img_list[self.level.POTIONNUM], self.player.potions)
                    self.potion_number.add(nums)
                elif self.layout[y][x]==self.level.HEART1:
                    heart = Heart(centerPoint, self.img_list[self.level.HEART1])
                    self.heart1_group.add(heart)
                elif self.layout[y][x]==self.level.HEART2:
                    heart = Heart(centerPoint, self.img_list[self.level.HEART2])
                    self.heart2_group.add(heart)
                elif self.layout[y][x]==self.level.HEART3:
                    heart = Heart(centerPoint, self.img_list[self.level.HEART3])
                    self.heart3_group.add(heart)

                """
                    Not sure how ot do projectiles (not even sure if they are needed here)

                elif self.layout[y][x]==self.level.JAVELIN:
                    javelin = #create javelin
                    self.projectile_group.add(javelin)
                elif self.layout[y][x]==self.level.BALL:
                    ball = #create ball
                    self.projectile_group.add(ball)
                elif self.layout[y][x]==self.level.ARROW:
                    arrow = #create arrow
                    self.projectile_group.add(arrow)

                    NOt sure how to do boss since he is more than one block big

                elif self.layout[y][x]==self.level.BOSS:
                    boss = #create boss
                    self.block_group.add(boss)
                    """

        self.player_group=pygame.sprite.RenderUpdates(self.player)


if __name__ == "__main__":
    MainWindow = MainQuest()
    MainWindow.MainLoop()

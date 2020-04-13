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
import basicSprite
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

BLOCK_SIZE = 68

class MainQuest:
    """
    The Main PyGame Class – This class handles the main
    initialization and creating of the Game.
    """

    def __init__(self, width=816,height=680):
        """
        Initialize PyGame
        """
        pygame.init()
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

            self.player_group.clear(self.screen,self.background)
            self.troll_group.clear(self.screen,self.background)
            self.bat_group.clear(self.screen,self.background)
            self.shooter_group.clear(self.screen,self.background)
            self.projectile_group.clear(self.screen, self.background)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #elif event.type == PLAYER_DEAD:
                    """
                    What happens when the player dies
                    """

                #elif event.type == WIN:
                    """
                    The player Won
                    Quit the Game
                    """
                    #print("You Won!")
                    #sys.exit()

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
                Update the player sprite
                """
                num = self.player.update(self.block_group, self.passage_group, self.breakable_group, self.troll_group, self.shooter_group, self.bat_group, self.projectile_group)
                if (len(self.troll_group.sprites()) > 0):
                    javelin = self.troll_group.update(self.block_group, self.player.coords, self.img_list[self.level.JAVELIN], self.breakable_group, self.passage_group)
                    if javelin != None:
                        self.projectile_group.add(javelin)
                if (len(self.bat_group.sprites()) > 0):
                    self.bat_group.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)
                if (len(self.shooter_group.sprites()) > 0):
                    ball = self.shooter_group.update(self.block_group, self.player.coords, self.img_list[self.level.BALL], self.breakable_group, self.passage_group)
                if (len(self.projectile_group.sprites()) > 0):
                    self.projectile_group.update(self.block_group, self.breakable_group, self.player_group, self.projectile_group)

                if num != None:
                    self.current_level = num[0]
                    """
                    Load all of our Sprites
                    """
                    self.LoadSprites(num[1])
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

                pygame.display.update(reclist)

                time.sleep (0.05)
                #This time can be changed depending on what we establish as the best time

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
        print(self.current_level)
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
        else:
            self.layout = self.level.getLayoutTop()

        self.img_list = self.level.getSprites()

        """
        Create the groups:
            - block backgrounds
            - crossable Backgrounds
            - passage Backgrounds
            - breakable Backgrounds
            - Enemies
            - projectiles
        """
        self.block_group = pygame.sprite.RenderUpdates()
        self.passage_group = pygame.sprite.RenderUpdates()
        self.crossable_group = pygame.sprite.RenderUpdates()
        self.breakable_group = pygame.sprite.RenderUpdates()

        self.troll_group = pygame.sprite.RenderUpdates()
        self.bat_group = pygame.sprite.RenderUpdates()
        self.shooter_group = pygame.sprite.RenderUpdates()
        self.projectile_group = pygame.sprite.RenderUpdates()

        for y in range(len(self.layout)):
            for x in range(len(self.layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                """
                Read the level array to define what comes in which place of the Screen
                Create the sprites necessary to fill the parts we just read
                """
                if self.layout[y][x]==self.level.GROUND:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                elif self.layout[y][x]==self.level.GRASS:
                    grass = singleSprite(centerPoint, self.img_list[self.level.GRASS])
                    self.crossable_group.add(grass)
                elif self.layout[y][x]==self.level.WATER:
                    water = singleSprite(centerPoint, self.img_list[self.level.WATER])
                    self.block_group.add(water)
                elif self.layout[y][x]==self.level.TREE:
                    tree = singleSprite(centerPoint, self.img_list[self.level.TREE])
                    self.block_group.add(tree)
                elif self.layout[y][x]==self.level.WALL:
                    wall = singleSprite(centerPoint, self.img_list[self.level.WALL])
                    self.block_group.add(wall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL], (self.current_level * 10 + 1), False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BROKEN_WALL:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL], (self.current_level * 10 + 1), True) #create breakable
                    self.breakable_group.add(breakable)
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
                elif self.layout[y][x]==self.level.PLAYER_OW:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    self.player = Player(centerPoint, self.img_list[self.level.PLAYER_OW], (x,y), 4)


                """
                    Not sure how ot do projectiles (not even sure if they are needed here)

                elif self.layout[y][x]==self.level.JAVELIN:
                    #javelin = #create javelin
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

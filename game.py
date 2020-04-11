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
from basicSprite import Sprite
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
        self.LoadSprites()
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
            self.monster_group.clear(self.screen,self.background)
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

                self.player.update(self.block_group, self.passage_group, self.breakable_group, self.monster_group, self.projectile_group)

                """Do the Drawing"""
                textpos = 0
                self.screen.blit(self.background, (0, 0))


                reclist = self.block_group.draw(self.screen)
                reclist += self.passage_group.draw(self.screen)
                reclist += self.crossable_group.draw(self.screen)
                reclist +=  self.breakable_group.draw(self.screen)
                reclist +=  self.monster_group.draw(self.screen)
                reclist +=  self.projectile_group.draw(self.screen)
                reclist +=  self.player_group.draw(self.screen)

                pygame.display.update(reclist)

                time.sleep (0.05)
                #This time can be changed depending on what we establish as the best time



    def LoadSprites(self):
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
            level = level11.level11()
        if self.current_level == 12:
            level = level12.level12()
        if self.current_level == 13:
            level = level13.level13()
        if self.current_level == 21:
            level = level21.level21()
        if self.current_level == 22:
            level = level22.level22()
        if self.current_level == 23:
            level = level23.level23()
        if self.current_level == 31:
            level = level31.level31()
        if self.current_level == 32:
            level = level32.level32()
        if self.current_level == 33:
            level = level33.level33()
        if self.current_level == 221:
            level = cave22.cave22()
        if self.current_level == 311:
            level = cave31.cave31()

        layout = level.getLayout()
        img_list = level.getSprites()

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

        self.monster_group = pygame.sprite.RenderUpdates()
        self.projectile_group = pygame.sprite.RenderUpdates()

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                """
                Read the level array to define what comes in which place of the Screen
                Create the sprites necessary to fill the parts we just read
                """
                if layout[y][x]==level.GROUND:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                elif layout[y][x]==level.GRASS:
                    grass = Sprite(centerPoint, img_list[level.GRASS])
                    self.crossable_group.add(grass)
                elif layout[y][x]==level.WATER:
                    water = Sprite(centerPoint, img_list[level.WATER])
                    self.block_group.add(water)
                elif layout[y][x]==level.TREE:
                    tree = Sprite(centerPoint, img_list[level.TREE])
                    self.block_group.add(tree)
                elif layout[y][x]==level.WALL:
                    wall = Sprite(centerPoint, img_list[level.WALL])
                    self.block_group.add(wall)
                elif layout[y][x]==level.BREAKABLE_WALL:
                    breakableWall = BreakableBackground(centerPoint, img_list[level.BREAKABLE_WALL], (self.current_level * 10 + 1), False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif layout[y][x]==level.BROKEN_WALL:
                    breakableWall = BreakableBackground(centerPoint, img_list[level.BREAKABLE_WALL], (self.current_level * 10 + 1), True) #create breakable
                    self.breakable_group.add(breakable)
                elif layout[y][x]==level.PASSAGE_T:
                    passage = Passage(centerPoint, img_list[level.PASSAGE_T], (self.current_level - 10))#create passage to top
                    self.passage_group.add(passage)
                elif layout[y][x]==level.PASSAGE_B:
                    passage = Passage(centerPoint, img_list[level.PASSAGE_B], (self.current_level + 10))#create passage to bottom
                    self.passage_group.add(passage)
                elif layout[y][x]==level.PASSAGE_L:
                    passage = Passage(centerPoint, img_list[level.PASSAGE_L], (self.current_level - 1))#create passage to left
                    self.passage_group.add(passage)
                elif layout[y][x]==level.PASSAGE_R:
                    passage = Passage(centerPoint, img_list[level.PASSAGE_R], (self.current_level + 1))#create passage to right
                    self.passage_group.add(passage)
                elif layout[y][x]==level.BAT_V:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    bat = Bat(centerPoint, img_list[level.BAT_V], (x, y), 1)#create bat
                    self.monster_group.add(bat)
                elif layout[y][x]==level.BAT_H:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    bat = Bat(centerPoint, img_list[level.BAT_H], (x, y), 2)#create bat
                    self.monster_group.add(bat)
                elif layout[y][x]==level.TROLL_V:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    troll = Troll(centerPoint, img_list[level.TROLL_V], (x, y), 1)#create troll
                    self.monster_group.add(troll)
                elif layout[y][x]==level.TROLL_H:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    troll = Troll(centerPoint, img_list[level.TROLL_H], (x, y), 2)#create troll
                    self.monster_group.add(troll)
                elif layout[y][x]==level.SHOOTER_V:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    shooter = Shooter(centerPoint, img_list[level.SHOOTER_V], (x, y), 1)#create shooter
                    self.monster_group.add(shooter)
                elif layout[y][x]==level.SHOOTER_H:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    shooter = Shooter(centerPoint, img_list[level.SHOOTER_H], (x, y), 2)#create shooter
                    self.monster_group.add(shooter)
                elif layout[y][x]==level.PLAYER:
                    ground = Sprite(centerPoint, img_list[level.GROUND])
                    self.crossable_group.add(ground)
                    self.player = Player(centerPoint, img_list[level.PLAYER], (x,y), 4)


                """
                    Not sure how ot do projectiles (not even sure if they are needed here)

                elif layout[y][x]==level.JAVELIN:
                    #javelin = #create javelin
                    self.projectile_group.add(javelin)
                elif layout[y][x]==level.BALL:
                    ball = #create ball
                    self.projectile_group.add(ball)
                elif layout[y][x]==level.ARROW:
                    arrow = #create arrow
                    self.projectile_group.add(arrow)

                    NOt sure how to do boss since he is more than one block big

                elif layout[y][x]==level.BOSS:
                    boss = #create boss
                    self.block_group.add(boss)
                    """

        self.player_group=pygame.sprite.RenderUpdates(self.player)


if __name__ == "__main__":
    MainWindow = MainQuest()
    MainWindow.MainLoop()

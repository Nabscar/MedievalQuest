import os, sys
sys.path.append('/home/nabih/Documents/SoftDes/MedievalQuest/levels')
sys.path.append('/home/nabih/Documents/SoftDes/MedievalQuest/Images')

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
from playerSprite import *
from monsters import *
from projectiles import *
import time

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

BLOCK_SIZE = 24

class MainQuest:
    """
    The Main PyGame Class – This class handles the main
    initialization and creating of the Game.
    """

    def __init__(self, width=960,height=680):
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
        elf.background = pygame.Surface(self.screen.get_size())
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == PLAYER_DEAD:
                    """
                    What happens when the player dies
                    """

                elif event.type == WIN:
                    """
                    The player Won
                    Quit the Game
                    """
                    print("You Won!")
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
                Update the player sprite
                """

                """
                Do the drawing of the moved sprites in the Screen
                The idea here would be that the player would always be in the center of the x axis
                Based on the players coordinates, the game would read the squares around the player and print those
                That way, the player can move back and forwards, and always have screen to play
                That is the reason nothing was permanently drawn on the Screen
                Every x time (which we would determine by playing but would probably be shorter than a second
                it is currently set to 0.05 seconds, but its an easy change)
                The whole screen would reprint, and depending on how the player moved, the screen would move
                Besides, the enemies coordinates would also need to change, not only in respect to the player
                but also in respect to the background
                """

                time.sleep (0.05)
                #This time can be changed depending on what we establish as the best time
        pass


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
        self.player_group = pygame.sprite.RenderUpdates()

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                """
                Read the level array to define what comes in which place of the Screen
                Create the sprites necessary to fill the parts we just read
                """
                if layout[y][x]==level.BLOCK:
                    block = BlockBackground(centerPoint, img_list[level.BLOCK])#create block
                    self.block_group.add(block)
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
                elif layout[y][x]==level.CROSSABLE:
                    crossable = Crossable(centerPoint, img_list[level.CROSSABLE])#create crossable
                    self.crossable_group.add(crossable)
                elif layout[y][x]==level.BREAKABLE:
                    breakable = Breakable(centerPoint, img_list[level.BREAKABLE], (self.current_level * 10 + 1), False) #create breakable
                    self.breakable_group.add(breakable)
                    """
                    Not sure hot ot do projectiles (not even sure if they are needed here)

                elif layout[y][x]==level.JAVELIN:
                    #javelin = #create javelin
                    self.projectile_group.add(javelin)
                elif layout[y][x]==level.BALL:
                    ball = #create ball
                    self.projectile_group.add(ball)
                elif layout[y][x]==level.ARROW:
                    arrow = #create arrow
                    self.projectile_group.add(arrow)
                    """
                elif layout[y][x]==level.TROLL:
                    troll = Troll(centerPoint, img_list[level.TROLL], (x, y), direction = random.randint(1,4))#create troll
                    self.monster_group.add(troll)
                elif layout[y][x]==level.SHOOTER:
                    shooter = Shooter(centerPoint, img_list[level.SHOOTER], (x, y), direction = random.randint(1,4))#create shooter
                    self.monster_group.add(shooter)
                elif layout[y][x]==level.BAT:
                    bat = Bat(centerPoint, img_list[level.BAT], (x, y), direction = random.randint(1,4))#create bat
                    self.monster_group.add(bat)
                    """
                    NOt sure how to do boss since he is more than one block big

                elif layout[y][x]==level.BOSS:
                    boss = #create boss
                    self.block_group.add(boss)
                    """
                elif layout[y][x]==level.PLAYER:
                    player = Player(centerPoint, ing_list[level.PLAYER])#create player
                    self.player_group.add(player)
                """
        pass

if __name__ == "__main__":
    MainWindow = MainQuest()
    MainWindow.MainLoop()

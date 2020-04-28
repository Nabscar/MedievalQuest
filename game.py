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
from bossMonster import Boss #, BossHelper

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

BLOCK_SIZE = 64
BOSS_BLOCK_SIZE = 192

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
        self.boss = None
        pygame.display.flip()
        """
        Main Loop of game
        """
        while 1:
            self.started = True

            self.player_group.clear(self.screen,self.background)
            self.block_group.clear(self.screen,self.background)
            self.passage_group.clear(self.screen,self.background)
            self.crossable_group.clear(self.screen,self.background)
            self.breakable_group.clear(self.screen,self.background)
            self.inventory_group.clear(self.screen,self.background)
            self.bomb_number.clear(self.screen,self.background)
            self.potion_number.clear(self.screen,self.background)
            self.heart1_group.clear(self.screen,self.background)
            self.heart2_group.clear(self.screen,self.background)
            self.heart3_group.clear(self.screen,self.background)
            self.troll_group.clear(self.screen,self.background)
            self.bat_group.clear(self.screen,self.background)
            self.shooter_group.clear(self.screen,self.background)
            self.projectile_group.clear(self.screen,self.background)
            self.potion_group.clear(self.screen,self.background)
            self.pickup_bomb_group.clear(self.screen,self.background)
            self.bomb_group.clear(self.screen,self.background)
            self.arrow_group.clear(self.screen,self.background)
            self.bowandquiver_group.clear(self.screen,self.background)
            self.boss_group.clear(self.screen,self.background)


            events = pygame.event.get()
            for event in events:

                if event.type == pygame.QUIT:
                    sys.exit()

                elif self.player.currentHealth == 0:
                    """
                    What happens when the player dies
                    """
                    print("GAME OVER")
                    sys.exit()

                elif self.boss != None and self.boss.health == 0:
                    """
                    The player Won
                    Quit the Game
                    """
                    print("You Have reached the Castle! You Won!")
                    for door in self.door_group:
                        door.image = door.images[1]

                    self.boss_group.remove(self.bosstho)
                    self.Draw()
                    pygame.time.wait(10000)
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
                self.Update()
                self.Draw()


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
        self.block_group = pygame.sprite.RenderUpdates()#uncrossable background blocks
        self.passage_group = pygame.sprite.RenderUpdates()#passages to other screens
        self.crossable_group = pygame.sprite.RenderUpdates()#crossable background blocks
        self.breakable_group = pygame.sprite.RenderUpdates()#breakable walls in teh backgrounds
        self.inventory_group = pygame.sprite.RenderUpdates()#most of the things in the inventory
        self.bomb_number = pygame.sprite.RenderUpdates()#number of bombs the player has
        self.potion_number = pygame.sprite.RenderUpdates()#number of potions the player has
        self.heart1_group = pygame.sprite.RenderUpdates()#heart 1 to show player hp
        self.heart2_group = pygame.sprite.RenderUpdates()#heart 2 to show player hp
        self.heart3_group = pygame.sprite.RenderUpdates()#heart 3 to show player hp
        self.troll_group = pygame.sprite.RenderUpdates()#trolls that attack player
        self.bat_group = pygame.sprite.RenderUpdates()#bats that attack player
        self.shooter_group = pygame.sprite.RenderUpdates()#shooters that attack player
        self.projectile_group = pygame.sprite.RenderUpdates()#projectiles shot by enemies
        self.potion_group = pygame.sprite.RenderUpdates()#potions player can pick up
        self.pickup_bomb_group = pygame.sprite.RenderUpdates()#bombs player can pick up
        self.bomb_group = pygame.sprite.RenderUpdates()#bombs player puts down
        self.arrow_group = pygame.sprite.RenderUpdates()#arrows player shoots
        self.bowandquiver_group = pygame.sprite.RenderUpdates()#bow and quiver player can pick up
        self.player_group = pygame.sprite.RenderUpdates()#player
        self.boss_group = pygame.sprite.RenderUpdates()#Boss
        self.door_group = pygame.sprite.RenderUpdates()


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
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_T:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_T], (self.current_level-10), "T", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_B:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_B], (self.current_level+10), "B", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_L:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_L], (self.current_level-1), "L", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_R:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_R], (self.current_level+1), "R", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_C:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_C], (self.current_level * 10 + 1), "C", False) #create breakable
                    self.breakable_group.add(breakableWall)
                elif self.layout[y][x]==self.level.BREAKABLE_WALL_F:
                    breakableWall = BreakableBackground(centerPoint, self.img_list[self.level.BREAKABLE_WALL_F], (13), "C", False) #create breakable
                    self.breakable_group.add(breakableWall)


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
                elif self.layout[y][x]==self.level.BOSS:
                    ground = singleSprite(centerPoint, self.img_list[self.level.GROUND])
                    self.crossable_group.add(ground)
                    boss = Boss(centerPoint, self.img_list[self.level.BOSS], (x, y), 0)
                    self.boss = boss
                    self.boss_group.add(boss)
                    self.boss_group.add(self.boss)

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

                    """Items"""
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
                elif self.layout[y][x]==self.level.BOWANDQUIVER:
                    ground = singleSprite(centerPoint, self.img_list[self.level.CAVEGROUND])
                    self.crossable_group.add(ground)
                    bowandquiver = Bomb(centerPoint, self.img_list[self.level.BOWANDQUIVER])
                    self.bowandquiver_group.add(bowandquiver)

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


                    """Castle"""
                elif self.layout[y][x]==self.level.LEFTTOWER:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTTOWER])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.CASTLEGRASS:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.CASTLEGRASS])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTFLAGPOLE:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTFLAGPOLE])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTFLAG:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTFLAG])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTFLAG:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTFLAG])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTFLAGPOLE:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTFLAGPOLE])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTTOWER:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTTOWER])
                    self.block_group.add(castlepart)

                elif self.layout[y][x]==self.level.LEFTWINDOWLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTWINDOWLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTWINDOWRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTWINDOWRIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTBANNERTOPLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERTOPLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTBANNERTOPRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERTOPRIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTTOPWINDOW:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTTOPWINDOW])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTTOPWINDOW:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTTOPWINDOW])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERTOPLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERTOPLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERTOPRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERTOPRIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTWINDOWLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTWINDOWLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTWINDOWRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTWINDOWRIGHT])
                    self.block_group.add(castlepart)

                elif self.layout[y][x]==self.level.LEFTWALL:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTWALL])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTFULLWINDOW:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTFULLWINDOW])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTBANNERMIDDLELEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERMIDDLELEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTBANNERMIDDLERIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERMIDDLERIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTWINDOWANDDOOR:
                    castlepart = multipleSprite(centerPoint, self.img_list[self.level.LEFTWINDOWANDDOOR])
                    self.door_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTWINDOWANDDOOR:
                    castlepart = multipleSprite(centerPoint, self.img_list[self.level.RIGHTWINDOWANDDOOR])
                    self.door_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERMIDDLELEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERMIDDLELEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERMIDDLERIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERMIDDLERIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTFULLWINDOW:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTFULLWINDOW])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTWALL:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTWALL])
                    self.block_group.add(castlepart)

                elif self.layout[y][x]==self.level.LEFTBANNERBOTTOMLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERBOTTOMLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTBANNERBOTTOMRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.LEFTBANNERBOTTOMRIGHT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.LEFTDOOR:
                    castlepart = multipleSprite(centerPoint, self.img_list[self.level.LEFTDOOR])
                    self.door_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTDOOR:
                    castlepart = multipleSprite(centerPoint, self.img_list[self.level.RIGHTDOOR])
                    self.door_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERBOTTOMLEFT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERBOTTOMLEFT])
                    self.block_group.add(castlepart)
                elif self.layout[y][x]==self.level.RIGHTBANNERBOTTOMRIGHT:
                    castlepart = singleSprite(centerPoint, self.img_list[self.level.RIGHTBANNERBOTTOMRIGHT])
                    self.block_group.add(castlepart)


        self.player_group.add(self.player)

    def Update(self):
        """Update the troll group, each update gives a flag that basically tells us wether we need to create a javelin or not"""
        for troll in self.troll_group:
            troll_flag = troll.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)
            if troll_flag != None:
                info = troll_flag[1]
                javelin = Javelin(info[0], self.img_list[self.level.JAVELIN], info[1])
                self.projectile_group.add(javelin)

        """Update the bat group, since bats are not ranged, then there are no necessary flags"""
        if (len(self.bat_group.sprites()) > 0):
            self.bat_group.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)

        """Update the shooter group, each update gives a flag that basically tells us wether we need to create a ball or not"""
        for shooter in self.shooter_group:
            shooter_flag = shooter.update(self.block_group, self.player.coords, self.breakable_group, self.passage_group)
            if shooter_flag != None:
                info = shooter_flag[1]
                ball = Ball(info[0], self.img_list[self.level.BALL], info[1])
                self.projectile_group.add(ball)

        """Update the projectile group, each update gives a flag that basically tells us wether we hit something"""
        for projectile in self.projectile_group:
            projectile_flag = projectile.update(self.block_group, self.breakable_group, self.player_group, self.projectile_group, self.troll_group, self.shooter_group, self.bat_group, self.boss_group)
            if projectile_flag != None:
                if projectile_flag[0] != "Enemy":
                    self.projectile_group.remove(projectile)

        """Update the boss"""
        if self.boss != None:
            self.boss.update(self.block_group, self.passage_group)

        """Player update that returns flags"""
        player_flag = self.player.update(self.block_group, self.door_group, self.passage_group, self.breakable_group, self.troll_group, self.shooter_group, self.bat_group, self.projectile_group, self.potion_group, self.pickup_bomb_group, self.bowandquiver_group, self.boss_group)

        """If player has put a bomb, then update it, it may create a flag"""
        if self.player.bomb != None:
            bomb_flag = self.player.bomb.update(self.breakable_group, self.troll_group, self.shooter_group, self.bat_group, self.boss_group)
        else:
            bomb_flag = None

        """If player has put a arrow, it may create a flag"""
        if self.player.arrow != None:
            arrow_flag = self.player.arrow.update(self.block_group, self.breakable_group, self.player_group, self.projectile_group, self.troll_group, self.shooter_group, self.bat_group, self.boss_group)
        else:
            arrow_flag = None

        """
        Update the inventory
        """
        self.bomb_number.update(self.player.bombs)
        self.potion_number.update(self.player.potions)
        self.heart1_group.update(self.player.currentHealth - 8)
        self.heart2_group.update(self.player.currentHealth - 4)
        self.heart3_group.update(self.player.currentHealth)

        """check bomb_flag"""
        if bomb_flag != None:
            if bomb_flag[0] == "Enemy":
                for i in range(0,7):
                    enemies = bomb_flag[1][i]
                    if len(enemies[0]) > 0:
                        for troll in enemies[0]:
                            self.troll_group.remove(troll)
                    if len(enemies[1]) > 0:
                        for shooter in enemies[1]:
                            self.shooter_group.remove(shooter)
                    if len(enemies[2]) > 0:
                        for bat in enemies[2]:
                            self.bat_group.remove(bat)
            if bomb_flag[0] == "Boss":
                self.boss.health -= 1

            self.player.bomb = None
            self.bomb_group.empty()

        """check arrow_flag"""
        if arrow_flag != None:
            if arrow_flag[0] == "Enemy":
                enemies = arrow_flag[1]
                if len(enemies[0]) > 0:
                    for troll in enemies[0]:
                        self.troll_group.remove(troll)
                if len(enemies[1]) > 0:
                    for shooter in enemies[1]:
                        self.shooter_group.remove(shooter)
                if len(enemies[2]) > 0:
                    for bat in enemies[2]:
                        self.bat_group.remove(bat)
            if arrow_flag[0] == "BossHit":
                self.boss.health -= 1

            elif arrow_flag[0] == "Projectile":
                projectiles = arrow_flag[1]
                if len(projectiles) > 0:
                    for projectile in projectiles:
                        self.projectile_group.remove(projectile)

            if arrow_flag[0] != "Player":
                self.player.arrow = None
                self.arrow_group.empty()

        """If the player has collided against something specific, we get a flag as player_flag, depending on the flag, do different things"""

        if player_flag == None:
            holder = 1
        elif player_flag[0] == "Potion":
            self.potion_group.remove(player_flag[1])
        elif player_flag[0] == "Bomb":
            self.pickup_bomb_group.remove(player_flag[1])
        elif player_flag[0] == "PlaceBomb":
            bomb = Bomb(self.player.rect.center, self.img_list[self.level.KINGBOMB])
            self.player.bomb = bomb
            self.bomb_group.add(bomb)
        elif player_flag[0] == "Arrow":
            arrow = Arrow(self.player.rect.center, self.img_list[self.level.KINGARROW], self.player.direction)
            self.player.arrow = arrow
            self.arrow_group.add(arrow)
        elif player_flag[0] == "Attacked":
            enemies = player_flag[1]
            if len(enemies[0]) > 0:
                for troll in enemies[0]:
                    self.troll_group.remove(troll)
            if len(enemies[1]) > 0:
                for shooter in enemies[1]:
                    self.shooter_group.remove(shooter)
            if len(enemies[2]) > 0:
                for bat in enemies[2]:
                    self.bat_group.remove(bat)
        elif player_flag[0] == "BossHit":
            if self.boss.attack == 1:
                self.boss.health -= 1
            else:
                self.player.currentHealth -= 1
        elif player_flag[0] == "Passage":
            self.current_level = player_flag[1]
            """
            Load all of our Sprites
            """
            self.LoadSprites(player_flag[2])
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

    def Draw(self):
        """Do the Drawing"""
        textpos = 0
        self.screen.blit(self.background, (0, 0))

        reclist = self.block_group.draw(self.screen)
        reclist += self.passage_group.draw(self.screen)
        reclist += self.crossable_group.draw(self.screen)
        reclist += self.breakable_group.draw(self.screen)
        reclist += self.troll_group.draw(self.screen)
        reclist += self.bat_group.draw(self.screen)
        reclist += self.shooter_group.draw(self.screen)
        reclist += self.projectile_group.draw(self.screen)
        reclist += self.player_group.draw(self.screen)
        reclist += self.inventory_group.draw(self.screen)
        reclist += self.bomb_number.draw(self.screen)
        reclist += self.potion_number.draw(self.screen)
        reclist += self.heart1_group.draw(self.screen)
        reclist += self.heart2_group.draw(self.screen)
        reclist += self.heart3_group.draw(self.screen)
        reclist += self.potion_group.draw(self.screen)
        reclist += self.pickup_bomb_group.draw(self.screen)
        reclist += self.bomb_group.draw(self.screen)
        reclist += self.arrow_group.draw(self.screen)
        reclist += self.bowandquiver_group.draw(self.screen)
        reclist += self.boss_group.draw(self.screen)
        reclist += self.door_group.draw(self.screen)


        pygame.display.update(reclist)

if __name__ == "__main__":
    MainWindow = MainQuest()
    MainWindow.MainLoop()

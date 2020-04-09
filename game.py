import os, sys
import pygame
import \levels\ *
import basicSprite
from pygame.locals import *
from helpers import *
from playerSprite import *
from enemies import *
from projectiles import *
import time

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

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
        pass

    def MainLoop(self):
        """
        Load all of our Sprites
        """
        self.LoadSprites(self.current_level)
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
                    if ((event.key == A_DOWN)
                    or (event.key == W_DOWN)
                    or (event.key == D_DOWN)
                    or (event.key == S_DOWN)
                    or (event.key == J_DOWN)
                    or (event.key == K_DOWN)
                    or (event.key == L_DOWN)
                    or (event.key == I_DOWN)):
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
        self.crossable_group = pygame.sprite.RenderUpdates()
        self.passage_group = pygame.sprite.RenderUpdates()
        self.breakable_group = pygame.sprite.RenderUpdates()
        self.enemy_group = pygame.sprite.RenderUpdates()
        self.projectile_group = pygame.sprite.RenderUpdates()
        self.character_group = pygame.sprite.RenderUpdates()

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """
                Get center points for all Sprites
                Read the level array to define what comes in which place of the Screen
                Create the sprites necessary to fill the parts we just read
                """
        """
        Create the player sprite group
        It will only be one sprite in the group
        But it is still created as a group to be more easily readable
        """
        self.character_group =  = pygame.sprite.RenderUpdates(self.player)

        pass

if __name__ == "__main__":
    MainWindow = MainQuest()
    MainWindow.MainLoop()

import os, sys
import pygame
import \levels\level11
import \levels\level12
import \levels\level13
import \levels\level21
import \levels\level22
import \levels\level23
import \levels\level31
import \levels\level32
import \levels\level33
import basicSprite
from pygame.locals import *
from helpers import *
from playerSprite import *
from enemies import *
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
        But since its a sliding platformer, that will not be necessary
        """

        pygame.display.flip()
        """
        Main Loop of game
        """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    """
                    What happens when the key is pressed
                    """
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.MoveKeyDown(event.key)
                elif event.type == KEYUP:
                    """
                    What happens when the key is let go
                    """
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.MoveKeyUp(event.key)
                elif event.type == POWER_UP_ONE_START:
                    """
                    What happens when the player gets a powerup
                    Which powerup does the player get?
                    """
                    self.player.power_up_one = True
                elif event.type == POWER_UP_ONE_END:
                    """
                    What happens when the loses powerup / powerup timer runs out
                    """
                    self.player.power_up_one = False
                    """
                    If the power-up has a timer, set it to 0
                    """
                    pygame.time.set_timer(POWER_UP_ONE_END, 0)
                elif event.type == POWER_UP_TWO_START:
                    """
                    What happens when the player gets a powerup
                    Which powerup does the player get?
                    """
                    self.player.power_up_two = True
                elif event.type == POWER_UP_TWO_END:
                    """
                    What happens when the loses powerup / powerup timer runs out
                    """
                    self.player.power_up_two = False
                    """
                    If the power-up has a timer, set it to 0
                    """
                    pygame.time.set_timer(POWER_UP_TWO_END, 0)
                elif event.type == PLAYER_DEAD:
                    """
                    The player died
                    Quit the Game
                    """
                    print("You Lost")
                    sys.exit()
                elif event.type == WIN:
                    """
                    The player Won
                    Quit the Game
                    """
                    print("You Won!")
                    sys.exit()

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
        """
        level1 = level001.level()
        layout = level1.getLayout()
        img_list = level1.getSprites()

        """
        Create the groups:
            - Powerups
            - enemies
            - Anything else needed
        """
        self.power_up_sprites = pygame.sprite.RenderUpdates()
        self.enemy_sprites = pygame.sprite.RenderUpdates()
        self.block_sprites = pygame.sprite.RenderUpdates()

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
        self.player_sprites =  = pygame.sprite.RenderUpdates(self.player)

        pass

if __name__ == "__main__":
    MainWindow = MainQuest()    
    MainWindow.MainLoop()

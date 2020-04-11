import levelBase
from helpers import load_image


class level13(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """
        GROUND = 0
        TREE = 1
        WALL = 2
        CAVE = 3
        BOSS = 4
        PLAYER = 5
        PASSAGE = 6
        CASTLE = 7
        pass

    def getLayout(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """

        pass

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        pass

import levelBase
from helpers import load_image


class cave31(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """
        WALL = 0
        BREAKABLE_WALL = 1
        BOMB = 2
        PLAYER = 3
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

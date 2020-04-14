import levelBase
from helpers import load_image


class level13(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self, side):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self, side)

        self.GROUND = 0
        self.TREE = 1
        self.WALL = 2
        self.CAVEENTRANCE = 3
        self.BOSS = 4
        self.PLAYER_OW = 5
        self.CASTLE = 6

    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],\
                [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],\
                [1, 0, 0, 0, 0, 0 ,0 ,0, 0, 0 ,0, 1],\
                [1, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [1, 3, 5, 0, 0, 0, 0, 0 ,0, 0, 0, 1],\
                [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground= load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        wall = load_image('BrickWall.png')
        cave = load_image('CaveEntrance.png')
        boss = self.bossImages()
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')

        return [ground, tree, wall, cave, boss, player, passage]

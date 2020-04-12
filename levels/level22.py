import levelBase
from helpers import load_image


class level22(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self)

        self.GROUND = 0
        self.TREE = 1
        self.WALL = 2
        self.BREAKABLE_WALL = 3
        self.PLAYER_OW = 4
        self.PASSAGE_T = 5

    def getLayout(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 2, 2, 2, 2, 5, 5, 1, 1, 1, 1, 1],\
                [2, 3, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0 ,0 ,0, 0, 0 ,0, 1],\
                [1, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0 ,1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 4, 0, 0, 1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0 ,0, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground= load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        wall = load_image('BrickWall.png')
        breakable_wall = [load_image('BreakableWall.png'), load_image('BrokenWall.png')]
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')

        return [ground, tree, wall, breakable_wall, player, passage]

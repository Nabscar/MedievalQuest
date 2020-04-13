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

        levelBase.Level.__init__(self)


        self.CAVEGROUND = 0
        self.CAVEWALL = 1
        self.CAVEWALLBREAKABLE = 2
        self.BOWANDQUIVER = 3
        self.PLAYER_C = 4
        self.PASSAGE_C = 5

    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 1, 0, 0, 0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 3 ,0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0 ,0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                [1, 1, 1, 1, 0, 4, 0, 0 ,1, 1, 1, 1],\
                [1, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 1]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground = load_image('CaveFloor.png')
        wall = load_image('CaveWall.png')
        BreakableWall = load_image('CaveWallBreakable.png')
        bowAndQuiver = load_image('Tree.png')
        player = self.kingCaveImages()
        passage = load_image('CaveFloor.png')

        return [ground, wall, BreakableWall, bowAndQuiver, player, passage]

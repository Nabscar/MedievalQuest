import levelBase
from helpers import load_image


class cave31(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self, side):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self, side)


        self.CAVEGROUND = 0
        self.CAVEWALL = 1
        self.CAVEWALLBREAKABLE = 2
        self.CAVEWALLBROKEN = 3
        self.PLAYER_C = 4
        self.PASSAGE_C = 5
        self.BOWANDQUIVER = 6
        self.BOMB = 7
        self.BOMBNUM = 8
        self.POTION = 9
        self.POTIONNUM= 10
        self.HEART1 = 11
        self.HEART2 = 12
        self.HEART3 = 13

    def getLayoutCaveTop(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1],\
                [1, 1, 0, 0, 0, 0 ,0 ,0, 0, 4, 1, 1],\
                [1, 1, 0, 0 ,0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 6, 0, 0, 0, 0, 0 ,0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def getLayoutCaveTop(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1],\
                [1, 1, 0, 0, 0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0 ,0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 6, 0, 0, 0, 0, 0 ,0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground = load_image('CaveFloor.png')
        wall = load_image('CaveWall.png')
        BreakableWall = load_image('CaveWallBreakable.png')
        BrokenWall = load_image('CaveWallBroken.png')
        bowAndQuiver = load_image('Tree.png')
        player = self.kingCaveImages()
        passage = load_image('CaveFloor.png')
        blank = load_image("Blank.png")
        bomb = load_image("Bomb.png")
        nums = self.numberImages()
        potion = load_image("Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]


        return [ground, wall, BreakableWall, bowAndQuiver, player, passage, blank, bomb, nums, potion, heart]

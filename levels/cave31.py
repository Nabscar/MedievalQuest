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
        self.WALL = 1
        self.BREAKABLE_WALL = 2
        self.PLAYER_C = 4
        self.PASSAGE_C = 5
        self.BOWANDQUIVER = 6
        self.BLANK = 7
        self.BOMB = 8
        self.BOMBNUM = 9
        self.POTION = 10
        self.POTIONNUM= 11
        self.HEART1 = 12
        self.HEART2 = 13
        self.HEART3 = 14
        self.KINGBOMB = 15
        self.KINGARROW = 16

    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0 ,0 ,0, 1, 1, 1, 1],\
                [1, 0, 6, 0 ,0, 0 ,0 ,0, 1, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 1 ,1, 1, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\
                [5, 0, 0, 0, 0, 0, 1, 1 ,1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [7, 8, 9, 7, 10, 11, 7, 7, 12, 13, 14, 7]]


    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground = load_image('CaveFloor.png')
        wall = load_image('CaveWall.png')
        BreakableWall = [load_image('CaveWallBreakable.png'), load_image('CaveWallBroken.png')]
        bowAndQuiver = load_image('Tree.png')
        player = self.kingCaveImages()
        passage = load_image('CaveEntrance.png')
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]
        kingbomb = load_image("CaveBomb.png")
        kingarrow = self.arrowImages()

        return [ground, wall, BreakableWall,blank,player, passage, bowAndQuiver, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb, kingarrow]

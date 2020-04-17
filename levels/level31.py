import levelBase
from helpers import load_image


class level31(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self, side):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self, side)

        self.GROUND = 0
        self.GRASS = 1
        self.WATER = 2
        self.TREE = 3
        self.WALL = 4
        self.BREAKABLE_WALL = 5
        self.SHOOTER_V = 6
        self.SHOOTER_H = 7
        self.PLAYER_OW = 8
        self.PASSAGE_T = 9
        self.CAVEENTRANCE = 10
        self.BALL = 11
        self.BLANK = 12
        self.BOMB = 13
        self.BOMBNUM = 14
        self.POTION = 15
        self.POTIONNUM= 16
        self.HEART1 = 17
        self.HEART2 = 18
        self.HEART3 = 19
        self.KINGBOMB = 20

    def getLayoutLeft(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 3, 3, 3, 3, 3, 3, 3, 9, 9, 9, 3],\
                [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3],\
                [2, 1, 1, 0, 0, 0 ,0 ,0, 0, 0 ,0, 3],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 5],\
                [3, 6, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 10, 0, 7, 0, 0, 0, 0 ,0, 0, 0, 3],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [12, 13, 14, 12, 15, 16, 12, 12, 17, 18, 19, 12]]

    def getLayoutBottom(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 3, 3, 3, 3, 3, 3, 3, 9, 9, 9, 3],\
                [2, 1, 1, 1, 0, 0, 0, 0, 0, 8, 0, 3],\
                [2, 1, 1, 0, 0, 0 ,0 ,0, 0, 0 ,0, 3],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],\
                [3, 6, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 10, 0, 7, 0, 0, 0, 0 ,0, 0, 0, 3],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [11, 12, 13, 11, 14, 15, 11, 11, 16, 17, 18, 11]]

    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 3, 3, 3, 3, 3, 3, 3, 9, 9, 9, 3],\
                [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3],\
                [2, 1, 1, 0, 0, 0 ,0 ,0, 0, 0 ,0, 3],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],\
                [3, 6, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 4],\
                [3, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 4],\
                [3, 10, 0, 7, 0, 0, 0, 0 ,0, 0, 0, 3],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [11, 12, 13, 11, 14, 15, 11, 11, 16, 17, 18, 11]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground = load_image('OW_Ground.png')
        grass = load_image('Grass.png')
        water = load_image('Water.png')
        tree = load_image('Tree.png')
        wall = load_image('BrickWall.png')
        breakableWall = [load_image('BreakableWall.png'), load_image('BrokenWall.png')]
        shooter = self.shooterImages()
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')
        cave  = load_image('CaveEntrance.png')
        ball = self.ballImages()
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]
        kingbomb = load_image("Bomb.png")

        return [ground, grass, water, tree, wall, breakableWall, shooter, shooter, player, passage, cave, ball, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb]

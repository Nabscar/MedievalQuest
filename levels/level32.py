import levelBase
from helpers import load_image


class level32(levelBase.Level):
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
        self.BREAKABLE_WALL_T = 5
        self.BAT_V = 6
        self.SHOOTER_H = 7
        self.TROLL_V = 8
        self.PLAYER_OW = 9
        self.PASSAGE_L = 10
        self.PASSAGE_R = 11
        self.BALL = 12
        self.JAVELIN = 13
        self.BLANK = 14
        self.BOMB = 15
        self.BOMBNUM = 16
        self.POTION = 17
        self.POTIONNUM= 18
        self.HEART1 = 19
        self.HEART2 = 20
        self.HEART3 = 21
        self.KINGBOMB = 22

    def getLayoutRight(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[3, 3, 3, 3, 4, 4, 5, 4, 4, 1, 1, 1],\
                [3, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2],\
                [3, 1, 1, 0, 0, 7 ,0 ,0, 0, 2 ,2, 2],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 3, 3, 3],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],\
                [10, 9, 0, 6, 0, 0, 0, 0, 0, 8, 0, 11],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 11],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [3, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1, 1],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [14, 15, 16, 14, 17, 18, 14, 14, 19, 20, 21, 14]]

    def getLayoutLeft(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[3, 3, 3, 3, 4, 4, 5, 4, 4, 1, 1, 1],\
                [3, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2],\
                [3, 1, 1, 0, 0, 7 ,0 ,0, 0, 2 ,2, 2],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 3, 3, 3],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],\
                [10, 0, 0, 6, 0, 0, 0, 0, 0, 0, 9, 11],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 11],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 1],\
                [3, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1, 1],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [14, 15, 16, 14, 17, 18, 14, 14, 19, 20, 21, 14]]

    def getLayoutBottom(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[3, 3, 3, 3, 4, 4, 5, 4, 4, 1, 1, 1],\
                [3, 1, 1, 1, 0, 0, 9, 0, 0, 2, 2, 2],\
                [3, 1, 1, 0, 0, 7 ,0 ,0, 0, 2 ,2, 2],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 3, 3, 3],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],\
                [10, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 11],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 11],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 1],\
                [3, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1, 1],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [14, 15, 16, 14, 17, 18, 14, 14, 19, 20, 21, 14]]

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
        bat = self.batImages()
        shooter = self.shooterImages()
        troll = self.trollImages()
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')
        ball = self.ballImages()
        javelin = self.javelinImages()
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]
        kingbomb = load_image("Bomb.png")

        return [ground, grass, water, tree, wall, breakableWall, bat, shooter, troll, player, passage, passage, ball, javelin, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb]

import levelBase
from helpers import load_image


class level12(levelBase.Level):
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
        self.GRASS = 2
        self.TROLL_V = 3
        self.PICKPOTION = 4
        self.PLAYER_OW = 5
        self.PASSAGE_L = 6
        self.PASSAGE_B = 7
        self.JAVELIN = 8
        self.BLANK = 9
        self.BOMB = 10
        self.BOMBNUM = 11
        self.POTION = 12
        self.POTIONNUM= 13
        self.HEART1 = 14
        self.HEART2 = 15
        self.HEART3 = 16
        self.KINGBOMB = 17
        self.KINGARROW = 18


    def getLayoutTop(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],\
                [1, 2, 2, 0, 0, 0 ,0 ,0, 0, 2 ,2, 1],\
                [1, 2, 0, 0 ,0, 0 ,0 ,0, 0, 4, 2, 1],\
                [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [6, 0, 0, 3, 0, 0, 0, 0, 3, 0, 2, 1],\
                [6, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 2, 1],\
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],\
                [1, 2, 2, 0, 0, 0, 5, 0, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 7, 7, 7, 1, 1, 1, 1],\
                [9, 10, 11, 9, 12, 13, 9, 9, 14, 15, 16, 9]]

    def getLayoutRight(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],\
                [1, 2, 2, 0, 0, 0 ,0 ,0, 0, 2 ,2, 1],\
                [1, 2, 0, 0 ,0, 0 ,0 ,0, 0, 4, 2, 1],\
                [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [6, 5, 0, 3, 0, 0, 0, 0, 3, 0, 2, 1],\
                [6, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 2, 1],\
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],\
                [1, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 7, 7, 7, 1, 1, 1, 1],\
                [9, 10, 11, 9, 12, 13, 9, 9, 14, 15, 16, 9]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """
        ground = load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        grass = load_image('Grass.png')
        troll = self.trollImages()
        potion = load_image('Potion_Health.png')
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')
        javelin = self.javelinImages()
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image('Heart_0.png'), load_image("Heart_1.png"), load_image("Heart_2.png"), load_image("Heart_3.png"), load_image("Heart_4.png")]
        kingbomb = load_image("Bomb.png")
        kingarrow = self.arrowImages()

        return [ground, tree, grass, troll, potion, player, passage, passage, javelin, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb, kingarrow]

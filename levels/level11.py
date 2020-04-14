import levelBase
from helpers import load_image


class level11(levelBase.Level):
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
        self.TROLL_V = 4
        self.BAT_V = 5
        self.PLAYER_OW = 6
        self.PASSAGE_B = 7
        self.PASSAGE_R = 8
        self.JAVELIN = 9
        self.BLANK = 10
        self.BOMB = 11
        self.BOMBNUM = 12
        self.POTION = 13
        self.POTIONNUM= 14
        self.HEART1 = 15
        self.HEART2 = 16
        self.HEART3 = 17

    def getLayoutLeft(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [1, 1, 1, 0, 0, 0 ,0 ,0, 0, 0 ,0, 3],\
                [3, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 8],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8],\
                [3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 8],\
                [3, 0, 5, 0, 0, 0, 0, 0, 0 ,0, 0, 3],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [3, 7, 7, 7, 3, 3, 3, 3, 3, 3, 3, 3],\
                [10, 11, 12, 10, 13, 14, 10, 10, 15, 16, 17, 10]]

    def getLayoutTop(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3],\
                [2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [1, 1, 1, 0, 0, 0 ,0 ,0, 0, 0 ,0, 3],\
                [3, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 8],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],\
                [3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 8],\
                [3, 0, 5, 0, 0, 0, 0, 0, 0 ,0, 0, 3],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [3, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],\
                [3, 7, 7, 7, 3, 3, 3, 3, 3, 3, 3, 3],\
                [10, 11, 12, 10, 13, 14, 10, 10, 15, 16, 17, 10]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """
        ground = load_image('OW_Ground.png')
        grass = load_image('Grass.png')
        water = load_image('Water.png')
        tree = load_image('Tree.png')
        troll = self.trollImages()
        bat = self.batImages()
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')
        javelin = self.javelinImages()
        blank = load_image("Blank.png")
        bomb = load_image("Bomb.png")
        nums = self.numberImages()
        potion = load_image("Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]

        return [ground, grass, water, tree, troll, bat, player, passage, passage, javelin, blank, bomb, nums, potion, nums, heart, heart, heart]

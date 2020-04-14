import levelBase
from helpers import load_image


class level21(levelBase.Level):
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
        self.TREE = 2
        self.TROLL_H = 3
        self.PICKPOTION = 4
        self.PLAYER_OW = 5
        self.PASSAGE_T = 6
        self.PASSAGE_B = 7
        self.JAVELIN  = 8
        self.BLANK = 9
        self.BOMB = 10
        self.BOMBNUM = 11
        self.POTION = 12
        self.POTIONNUM= 13
        self.HEART1 = 14
        self.HEART2 = 15
        self.HEART3 = 16

    def getLayoutBottom(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2],\
                [2, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0 ,0 ,0, 0, 0 ,0, 2],\
                [2, 0, 0, 0 ,0, 3 ,0 ,0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 2],\
                [2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2],\
                [2, 2, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 2],\
                [2, 2, 1, 1, 1, 1, 1, 1, 7, 7, 7, 2],\
                [9, 10, 11, 9, 12, 13, 9, 9, 14, 15, 16, 9]]

    def getLayoutTop(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0 ,0 ,0, 0, 0 ,0, 2],\
                [2, 0, 0, 0 ,0, 3 ,0 ,0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2],\
                [2, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 2],\
                [2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2],\
                [2, 2, 0, 0, 0, 0, 0, 0 ,0, 5, 0, 2],\
                [2, 2, 1, 1, 1, 1, 1, 1, 7, 7, 7, 2],\
                [9, 10, 11, 9, 12, 13, 9, 9, 14, 15, 16, 9]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """
        ground= load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        grass = load_image('Grass.png')
        troll = self.trollImages()
        player = self.kingOWImages()
        potion = load_image('Potion_Health.png')
        passage = load_image('OW_Ground.png')
        javelin = self.javelinImages()
        blank = load_image("Blank.png")
        bomb = load_image("Bomb.png")
        nums = self.numberImages()
        potion = load_image("Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]

        return [ground, grass, tree, troll, potion, player, passage, passage, javelin, blank, bomb, nums, potion, nums, heart, heart, heart]

import levelBase
from helpers import load_image


class level22(levelBase.Level):
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
        self.BREAKABLE_WALL = 3
        self.PLAYER_OW = 4
        self.PASSAGE_T = 5
        self.BLANK = 6
        self.BOMB = 7
        self.BOMBNUM = 8
        self.POTION = 9
        self.POTIONNUM= 10
        self.HEART1 = 11
        self.HEART2 = 12
        self.HEART3 = 13

    def getLayoutTop(self):
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
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [6, 7, 8, 6, 9, 10, 6, 6, 11, 12, 13, 6]]

    def getLayoutBottom(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[2, 2, 2, 2, 2, 5, 5, 1, 1, 1, 1, 1],\
                [2, 3, 2, 2, 2, 0, 4, 1, 1, 1, 1, 1],\
                [1, 0, 0, 0, 0, 0 ,0 ,0, 0, 0 ,0, 1],\
                [1, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0 ,1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],\
                [1, 1, 1, 0, 0, 0, 0, 0 ,0, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [6, 7, 8, 6, 9, 10, 6, 6, 11, 12, 13, 6]]

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
        blank = load_image("Blank.png")
        bomb = load_image("Bomb.png")
        nums = self.numberImages()
        potion = load_image("Potion_Health.png")
        heart = [load_image("Heart_Full.png"), load_image("Heart_Half.png"), load_image("Heart_Empty.png")]

        return [ground, tree, wall, breakable_wall, player, passage, blank, bomb, nums, potion, nums, heart, heart, heart]

import levelBase
from helpers import load_image


class level12(levelBase.Level):
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
        self.GRASS = 2
        self.TROLL_V = 3
        self.POTION = 4
        self.PLAYER_OW = 5
        self.PASSAGE_L = 6
        self.PASSAGE_B = 7


    def getLayout(self):
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
                [1, 1, 1, 1, 1, 7, 7, 7, 1, 1, 1, 1]]

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
        return [ground, tree, grass, troll, potion, player, passage, passage]

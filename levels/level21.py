import levelBase
from helpers import load_image


class level21(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self)

        self.GROUND = 0
        self.GRASS = 1
        self.TREE = 2
        self.TROLL_H = 3
        self.POTION = 4
        self.PLAYER_OW = 5
        self.PASSAGE_T = 6
        self.PASSAGE_B = 7

    def getLayout(self):
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
                [2, 2, 1, 1, 1, 1, 1, 1, 7, 7, 7, 2]]

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
        return [ground, grass, tree, troll, potion, player, passage, passage, javelin]

import levelBase
from helpers import load_image


class level32(levelBase.Level):
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
        self.WATER = 2
        self.TREE = 3
        self.WALL = 4
        self.BREAKABLE_WALL = 5
        self.BAT_V = 6
        self.SHOOTER_H = 7
        self.TROLL_V = 8
        self.PLAYER_OW = 9
        self.PASSAGE_L = 10
        self.PASSAGE_R = 11
        pass

    def getLayout(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[3, 3, 3, 3, 4, 4, 5, 4, 4, 1, 1, 1],\
                [3, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2],\
                [3, 1, 1, 0, 0, 7 ,0 ,0, 0, 2 ,2, 2],\
                [3, 1, 0, 0 ,0, 0 ,0 ,0, 0, 3, 3, 3],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],\
                [11, 9, 0, 6, 0, 0, 0, 0, 0, 8, 0, 11],\
                [4, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 11],\
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [3, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1, 1],\
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]

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

        return [ground, grass, water, tree, wall, breakableWall, bat, shooter, troll, player, passage, passage]

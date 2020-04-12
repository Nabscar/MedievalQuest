import levelBase
from helpers import load_image


class level31(levelBase.Level):
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
        self.SHOOTER_V = 6
        self.SHOOTER_H = 7
        self.PLAYER_OW = 8
        self.PASSAGE_T = 9
        self.CAVEENTRANCE = 10

    def getLayout(self):
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
        shooter = self.shooterImages()
        player = self.kingOWImages()
        passage = load_image('OW_Ground.png')
        cave  = load_image('CaveEntrance.png')

        return [ground, grass, water, tree, wall, breakableWall, shooter, shooter, player, passage, cave]

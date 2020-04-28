import levelBase
from helpers import load_image


class level13(levelBase.Level):
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
        self.CAVEENTRANCE = 3
        self.BOSS = 4
        self.PLAYER_OW = 5
        self.BLANK = 6
        self.BOMB = 7
        self.BOMBNUM = 8
        self.POTION = 9
        self.POTIONNUM= 10
        self.HEART1 = 11
        self.HEART2 = 12
        self.HEART3 = 13
        self.KINGBOMB = 14
        self.KINGARROW = 15

        self.LEFTTOWER = 16
        self.CASTLEGRASS = 17
        self.LEFTFLAGPOLE = 18
        self.LEFTFLAG = 19
        self.RIGHTFLAG = 20
        self.RIGHTFLAGPOLE = 21
        self.RIGHTTOWER = 22

        self.LEFTWINDOWLEFT = 23
        self.LEFTWINDOWRIGHT = 24
        self.LEFTBANNERTOPLEFT = 25
        self.LEFTBANNERTOPRIGHT = 26
        self.LEFTTOPWINDOW = 27
        self.RIGHTTOPWINDOW = 28
        self.RIGHTBANNERTOPLEFT = 29
        self.RIGHTBANNERTOPRIGHT = 30
        self.RIGHTWINDOWLEFT = 31
        self.RIGHTWINDOWRIGHT = 32

        self.LEFTWALL = 33
        self.LEFTFULLWINDOW = 34
        self.LEFTBANNERMIDDLELEFT = 35
        self.LEFTBANNERMIDDLERIGHT = 36
        self.LEFTWINDOWANDDOOR = 37
        self.RIGHTWINDOWANDDOOR = 38
        self.RIGHTBANNERMIDDLELEFT = 39
        self.RIGHTBANNERMIDDLERIGHT = 40
        self.RIGHTFULLWINDOW = 41
        self.RIGHTWALL = 42

        self.LEFTBANNERBOTTOMLEFT = 43
        self.LEFTBANNERBOTTOMRIGHT = 44
        self.LEFTDOOR = 45
        self.RIGHTDOOR = 46
        self.RIGHTBANNERBOTTOMLEFT = 47
        self.RIGHTBANNERBOTTOMRIGHT = 48


    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[16, 16, 17, 18, 19, 17, 17, 20, 21, 17, 22, 22],\
                [23, 24, 16, 25, 26, 27, 28, 29, 30, 22, 31, 32],\
                [33, 33, 34, 35, 36 ,37, 38, 39, 40, 41, 42, 42],\
                [33, 33, 33, 43, 44, 45, 46, 47, 48, 42, 42, 42],\
                [1, 0, 0, 0 ,0, 0 ,0 ,0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 1],\
                [1, 3, 5, 0, 0, 0, 0, 0 ,0, 0, 0, 1],\
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],\
                [6, 7, 8, 6, 9, 10, 6, 6, 11, 12, 13, 6]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground= load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        wall = load_image('BrickWall.png')
        cave = load_image('CaveEntrance.png')
        boss = self.bossImages()
        player = self.kingOWImages()
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image('Heart_0.png'), load_image("Heart_1.png"), load_image("Heart_2.png"), load_image("Heart_3.png"), load_image("Heart_4.png")]
        kingbomb = load_image("Bomb.png")
        kingarrow = self.arrowImages()

        castle = []

        castle = [load_image('Left_Tower.png'), load_image('Castle_Grass.png'), load_image('Left_Flag_Pole.png'), load_image('Left_Flag.png'), load_image('Right_Flag.png'), load_image('Right_Flag_Pole.png'), load_image('Right_Tower.png'),
                  load_image('Left_Window_Left.png'), load_image('Left_Window_Right.png'), load_image('Left_Top_Banner_Left.png'), load_image('Left_Top_Banner_Right.png'), load_image('Left_Top_Window.png'), load_image('Right_Top_Window.png'), load_image('Right_Top_Banner_Left.png'), load_image('Right_Top_Banner_Right.png'), load_image('Right_Window_Left.png'), load_image('Right_Window_Right.png'),
                  load_image('Left_Castle_Wall.png'), load_image('Left_Full_Window.png'), load_image('Left_Middle_Banner_Left.png'), load_image('Left_Middle_Banner_Right.png'), [load_image('Left_Window_and_Door_Closed.png'), load_image('Left_Window_and_Door_Open.png')], [load_image('Right_Window_and_Door_Closed.png'), load_image('Right_Window_and_Door_Open.png')], load_image('Right_Middle_Banner_Left.png'), load_image('Right_Middle_Banner_Right.png'), load_image('Right_Full_Window.png'), load_image('Right_Castle_Wall.png'),
                  load_image('Left_Bottom_Banner_Left.png'), load_image('Left_Bottom_Banner_Right.png'), [load_image('Left_Door_Closed.png'), load_image('Left_Door_Open.png')], [load_image('Right_Door_Closed.png'), load_image('Right_Door_Open.png')], load_image('Right_Bottom_Banner_Left.png'), load_image('Right_Bottom_Banner_Right.png')]

        lt = [ground, tree, wall, cave, boss, player, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb, kingarrow]
        lt += castle
        return lt

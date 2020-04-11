import levelBase
from helpers import load_image


class level22(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """
        self.GROUND = 0
        self.GRASS = 'x'
        self.WATER = 'x'
        self.TREE = 1
        self.WALL = 2
        self.BREAKABLE_WALL = 3
        self.BROKEN_WALL = 'x'
        self.PASSAGE_T = 5
        self.PASSAGE_B = 'x'
        self.PASSAGE_L = 'x'
        self.PASSAGE_R = 'x'
        self.BAT_V = 'x'
        self.BAT_H = 'x'
        self.TROLL_V = 'x'
        self.TROLL_H = 'x'
        self.SHOOTER_V = 'x'
        self.SHOOTER_H = 'x'
        self.BOSS = 'x'
        self.PLAYER = 4

    def getLayout(self):
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
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground= load_image('OW_Ground.png')
        tree = load_image('Tree.png')
        wall = load_image('BrickWall.png')
        breakable_wall1 = load_image('BreakableWall.png')
        breakable_wall2 = load_image('BrokenWall.png')
        breakable_wall = [breakable_wall1, breakable_wall2]

        basic_player_down = load_image('King_Side_Down.png')
        basic_player_left = load_image('King_Side_Left.png')
        basic_player_right = load_image('King_Side_Right.png')
        basic_player_up = load_image('King_Side_Up.png')

        """
        basic_player_attack_up = load_image('monster_scared_01.png')
        basic_player_attack_left = load_image('monster_scared_01.png')
        basic_player_attack_down = load_image('monster_scared_01.png')
        basic_player_attack_right = load_image('monster_scared_01.png')

        quiver_player_up = load_image('monster_scared_01.png')
        quiver_player_left = load_image('monster_scared_01.png')
        quiver_player_down = load_image('monster_scared_01.png')
        quiver_player_right = load_image('monster_scared_01.png')

        quiver_player_attack_up = load_image('monster_scared_01.png')
        quiver_player_attack_left = load_image('monster_scared_01.png')
        quiver_player_attack_down = load_image('monster_scared_01.png')
        quiver_player_attack_right = load_image('monster_scared_01.png')

        quiver_player_shoot_up = load_image('monster_scared_01.png')
        quiver_player_shoot_left = load_image('monster_scared_01.png')
        quiver_player_shoot_down = load_image('monster_scared_01.png')
        quiver_player_shoot_right = load_image('monster_scared_01.png')
        """
        player = [basic_player_down, basic_player_left, basic_player_right, basic_player_up]
        passage = load_image('OW_Ground.png')

        return [ground, tree, wall, breakable_wall1, basic_player_up, passage]

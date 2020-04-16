from helpers import load_image

class Level:
    """The Base Class for Levels"""
    def getLayout(self):
        """Get the Layout of the level"""
        """Returns a [][] list"""
        pass

    def getImages(self):
        """Get a list of all the images used by the level"""
        """Returns a list of all the images used. The indices
        in the layout refer to sprites in the list returned by
        this function"""
        pass

    def __init__ (self, side):
        """
        General initializer that start the constants
        """
        self.side = side

        self.GROUND = 'x'
        self.GRASS = 'x'
        self.WATER = 'x'
        self.TREE = 'x'
        self.WALL = 'x'
        self.BREAKABLE_WALL = 'x'
        self.BROKEN_WALL = 'x'
        self.PASSAGE_B = 'x'
        self.PASSAGE_T = 'x'
        self.PASSAGE_L = 'x'
        self.PASSAGE_R = 'x'
        self.CAVEENTRANCE = 'x'
        self.BAT_V = 'x'
        self.BAT_H = 'x'
        self.TROLL_V = 'x'
        self.TROLL_H = 'x'
        self.SHOOTER_V = 'x'
        self.SHOOTER_H = 'x'
        self.BOSS = 'x'
        self.PLAYER_OW = 'x'
        self.PLAYER_C = 'x'
        self.BOWANDQUIVER = 'x'
        self.CAVEGROUND = 'x'
        self.CAVEWALL = 'x'
        self.CAVEWALLBREAKABLE = 'x'
        self.STONE = 'x'
        self.PASSAGE_C = 'x'
        self.JAVELIN = 'x'
        self.BALL = 'x'
        self.BLANK = 'x'
        self.BOMB = 'x'
        self.BOMBNUM = 'x'
        self.POTION = 'x'
        self.POTIONNUM = 'x'
        self.HEART = 'x'
        self.PICKPOTION = 'x'
        self.PICKBOMB = 'x'

    def numberImages(self):
        """
        Returns a list of troll images
        """
        return [load_image('Number0.png'), load_image('Number1.png'), load_image('Number2.png'), load_image('Number3.png'), load_image('Number4.png'), load_image('Number5.png'), load_image('Number6.png'), load_image('Number7.png'), load_image('Number8.png'), load_image('Number9.png')]

    def trollImages(self):
        """
        Returns a list of troll images
        """
        return [load_image('Troll_Down.png'), load_image('Troll_Left1.png'), load_image('Troll_Left2.png'), load_image('Troll_Right1.png'), load_image('Troll_Right2.png'), load_image('Troll_Up.png')]

    def javelinImages(self):
        """
        Returns a list of javelin images
        """
        return[load_image('Javelin_Down.png'), load_image('Javelin_Left.png'), load_image('Javelin_Right.png'), load_image('Javelin_Up.png')]

    def shooterImages(self):
        """
        Returns a list of shooter images
        """
        return [load_image('Shooter_Down1.png'), load_image('Shooter_Down2.png'), load_image('Shooter_Left1.png'), load_image('Shooter_Left2.png'),
                load_image('Shooter_Right1.png'), load_image('Shooter_Right2.png'), load_image('Shooter_Up1.png'), load_image('Shooter_Up2.png')]

    def ballImages(self):
        """
        Returns a list of ball images
        """
        return load_image('Shooter_Projectile.png')

    def batImages(self):
        """
        Returns a list of bat images
        """
        return [load_image('Bat_Down1.png'), load_image('Bat_Down2.png'), load_image('Bat_Left1.png'), load_image('Bat_Left2.png'),
                load_image('Bat_Right1.png'), load_image('Bat_Right2.png'), load_image('Bat_Up1.png'), load_image('Bat_Up2.png')]


    def bossImages(self):
        """
        Returns a list of boss images
        """
        return load_image('OW_Ground.png')
        """
        return [[load_image('Boss_Lv0_Front.png'), load_image('Boss_Lv0_Neutral.png'), load_image('Boss_Lv0_Prep.png'), load_image('Boss_Lv0_Sides.png'), load_image('Boss_Lv0_Swing.png')],
                [load_image('Boss_Lv1_Front.png'), load_image('Boss_Lv1_Neutral.png'), load_image('Boss_Lv1_Prep.png'), load_image('Boss_Lv1_Sides.png'), load_image('Boss_Lv1_Swing.png')],
                [load_image('Boss_Lv2_Front.png'), load_image('Boss_Lv2_Neutral.png'), load_image('Boss_Lv2_Prep.png'), load_image('Boss_Lv2_Sides.png'), load_image('Boss_Lv2_Swing.png')],
                [load_image('Boss_Lv3_Front.png'), load_image('Boss_Lv3_Neutral.png'), load_image('Boss_Lv3_Prep.png'), load_image('Boss_Lv3_Sides.png'), load_image('Boss_Lv3_Swing.png')],
                [load_image('Boss_Lv4_Front.png'), load_image('Boss_Lv4_Neutral.png'), load_image('Boss_Lv4_Prep.png'), load_image('Boss_Lv4_Sides.png'), load_image('Boss_Lv4_Swing.png')],
                [load_image('Boss_Lv5_Front.png'), load_image('Boss_Lv5_Neutral.png'), load_image('Boss_Lv5_Prep.png'), load_image('Boss_Lv5_Sides.png'), load_image('Boss_Lv5_Swing.png')]]
        """

    def kingOWImages(self):
        """
        Returns a list of king images
        """
        basic_player_down = load_image('King_Side_Down.png')
        basic_player_left = load_image('King_Side_Left.png')
        basic_player_right = load_image('King_Side_Right.png')
        basic_player_up = load_image('King_Side_Up.png')


        basic_player_attack_down = load_image('King_Attack_Down_Sword.png')
        basic_player_attack_left = load_image('King_Attack_Left_Sword.png')
        basic_player_attack_right = load_image('King_Attack_Right_Sword.png')
        basic_player_attack_up = load_image('King_Attack_Up_Sword.png')

        """
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
        basic_player = [basic_player_down, basic_player_left, basic_player_right, basic_player_up, basic_player_attack_down, basic_player_attack_left,basic_player_attack_right, basic_player_attack_up]
        quiver_player = []
        player = basic_player + quiver_player
        return player

    def kingCaveImages(self):
        """
        Returns a list of king images
        """
        basic_player_down = load_image('Cave_King_Side_Down.png')
        basic_player_left = load_image('Cave_King_Side_Left.png')
        basic_player_right = load_image('Cave_King_Side_Right.png')
        basic_player_up = load_image('Cave_King_Side_Up.png')


        basic_player_attack_down = load_image('Cave_King_Attack_Down_Sword.png')
        basic_player_attack_left = load_image('Cave_King_Attack_Left_Sword.png')
        basic_player_attack_right = load_image('Cave_King_Attack_Right_Sword.png')
        basic_player_attack_up = load_image('Cave_King_Attack_Up_Sword.png')

        """
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
        basic_player = [basic_player_down, basic_player_left, basic_player_right, basic_player_up, basic_player_attack_down, basic_player_attack_left,basic_player_attack_right, basic_player_attack_up]
        quiver_player = []
        player = basic_player + quiver_player
        return player

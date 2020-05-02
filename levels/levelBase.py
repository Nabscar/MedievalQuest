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
        self.BLOCK_GROUND = 'x'
        self.GRASS = 'x'
        self.WATER = 'x'
        self.TREE = 'x'
        self.WALL = 'x'
        self.BREAKABLE_WALL_T = 'x'
        self.BREAKABLE_WALL_R = 'x'
        self.BREAKABLE_WALL_L = 'x'
        self.BREAKABLE_WALL_B = 'x'
        self.BREAKABLE_WALL_C = 'x'
        self.BREAKABLE_WALL_F = 'x'
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
        self.PICKBOMBC = 'x'
        self.PICKBOMBOW = 'x'

        self.LEFTTOWER = 'x'
        self.CASTLEGRASS = 'x'
        self.LEFTFLAGPOLE = 'x'
        self.LEFTFLAG = 'x'
        self.RIGHTFLAG = 'x'
        self.RIGHTFLAGPOLE = 'x'
        self.RIGHTTOWER = 'x'
        self.LEFTWINDOWLEFT = 'x'
        self.LEFTWINDOWRIGHT = 'x'
        self.LEFTBANNERTOPLEFT = 'x'
        self.LEFTBANNERTOPRIGHT = 'x'
        self.LEFTTOPWINDOW = 'x'
        self.RIGHTTOPWINDOW = 'x'
        self.RIGHTBANNERTOPLEFT = 'x'
        self.RIGHTBANNERTOPRIGHT = 'x'
        self.RIGHTWINDOWLEFT = 'x'
        self.RIGHTWINDOWRIGHT = 'x'
        self.LEFTWALL = 'x'
        self.LEFTFULLWINDOW = 'x'
        self.LEFTBANNERMIDDLELEFT = 'x'
        self.LEFTBANNERMIDDLERIGHT = 'x'
        self.LEFTWINDOWANDDOOR = 'x'
        self.RIGHTWINDOWANDDOOR = 'x'
        self.RIGHTBANNERMIDDLELEFT = 'x'
        self.RIGHTBANNERMIDDLERIGHT = 'x'
        self.RIGHTFULLWINDOW = 'x'
        self.RIGHTWALL = 'x'
        self.LEFTBANNERBOTTOMLEFT = 'x'
        self.LEFTBANNERBOTTOMRIGHT = 'x'
        self.LEFTDOOR = 'x'
        self.RIGHTDOOR = 'x'
        self.RIGHTBANNERBOTTOMLEFT = 'x'
        self.RIGHTBANNERBOTTOMRIGHT = 'x'

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
        return [load_image('Shooter_Projectile.png'), load_image('Shooter_Projectile.png'), load_image('Shooter_Projectile.png'), load_image('Shooter_Projectile.png')]

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
        return [[load_image('Boss_Lv0_Front.png', 192, 256), load_image('Boss_Lv0_Neutral.png', 192, 192), load_image('Boss_Lv0_Prep.png', 256, 192), load_image('Boss_Lv0_Sides.png', 320, 192), load_image('Boss_Lv0_Swing.png', 320, 256)],
                [load_image('Boss_Lv1_Front.png', 192, 256), load_image('Boss_Lv1_Neutral.png', 192, 192), load_image('Boss_Lv1_Prep.png', 256, 192), load_image('Boss_Lv1_Sides.png', 320, 192), load_image('Boss_Lv1_Swing.png', 320, 256)],
                [load_image('Boss_Lv2_Front.png', 192, 256), load_image('Boss_Lv2_Neutral.png', 192, 192), load_image('Boss_Lv2_Prep.png', 256, 192), load_image('Boss_Lv2_Sides.png', 320, 192), load_image('Boss_Lv2_Swing.png', 320, 256)],
                [load_image('Boss_Lv3_Front.png', 192, 256), load_image('Boss_Lv3_Neutral.png', 192, 192), load_image('Boss_Lv3_Prep.png', 256, 192), load_image('Boss_Lv3_Sides.png', 320, 192), load_image('Boss_Lv3_Swing.png', 320, 256)],
                [load_image('Boss_Lv4_Front.png', 192, 256), load_image('Boss_Lv4_Neutral.png', 192, 192), load_image('Boss_Lv4_Prep.png', 256, 192), load_image('Boss_Lv4_Sides.png', 320, 192), load_image('Boss_Lv4_Swing.png', 320, 256)],
                [load_image('Boss_Lv5_Front.png', 192, 256), load_image('Boss_Lv5_Neutral.png', 192, 192), load_image('Boss_Lv5_Prep.png', 256, 192), load_image('Boss_Lv5_Sides.png', 320, 192), load_image('Boss_Lv5_Swing.png', 320, 256)]]

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

        quiver_player_down = load_image('King_Side_Down_w_bow.png')
        quiver_player_left = load_image('King_Side_Left_w_bow.png')
        quiver_player_right = load_image('King_Side_Right_w_bow.png')
        quiver_player_up = load_image('King_Side_Up_w_bow.png')


        quiver_player_attack_down = load_image('King_Attack_Down_Sword_w_bow.png')
        quiver_player_attack_left = load_image('King_Attack_Left_Sword_w_bow.png')
        quiver_player_attack_right = load_image('King_Attack_Right_Sword_w_bow.png')
        quiver_player_attack_up = load_image('King_Attack_Up_Sword_w_bow.png')

        quiver_player_shoot_down = load_image('King_ArrowAttack_Down.png')
        quiver_player_shoot_left = load_image('King_ArrowAttack_Left.png')
        quiver_player_shoot_right = load_image('King_ArrowAttack_Right.png')
        quiver_player_shoot_up = load_image('King_ArrowAttack_Up.png')

        basic_player = [basic_player_down, basic_player_left, basic_player_right, basic_player_up, basic_player_attack_down, basic_player_attack_left,basic_player_attack_right, basic_player_attack_up]
        quiver_player = [quiver_player_down, quiver_player_left, quiver_player_right, quiver_player_up, quiver_player_attack_down, quiver_player_attack_left,quiver_player_attack_right, quiver_player_attack_up, quiver_player_shoot_down, quiver_player_shoot_left, quiver_player_shoot_right, quiver_player_shoot_up]
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

        quiver_player_down = load_image('Cave_King_Side_Down_w_bow.png')
        quiver_player_left = load_image('Cave_King_Side_Left_w_bow.png')
        quiver_player_right = load_image('Cave_King_Side_Right_w_bow.png')
        quiver_player_up = load_image('Cave_King_Side_Up_w_bow.png')


        quiver_player_attack_down = load_image('Cave_King_Attack_Down_Sword_w_bow.png')
        quiver_player_attack_left = load_image('Cave_King_Attack_Left_Sword_w_bow.png')
        quiver_player_attack_right = load_image('Cave_King_Attack_Right_Sword_w_bow.png')
        quiver_player_attack_up = load_image('Cave_King_Attack_Up_Sword_w_bow.png')

        quiver_player_shoot_down = load_image('Cave_King_ArrowAttack_Down.png')
        quiver_player_shoot_left = load_image('Cave_King_ArrowAttack_Left.png')
        quiver_player_shoot_right = load_image('Cave_King_ArrowAttack_Right.png')
        quiver_player_shoot_up = load_image('Cave_King_ArrowAttack_Up.png')

        basic_player = [basic_player_down, basic_player_left, basic_player_right, basic_player_up, basic_player_attack_down, basic_player_attack_left,basic_player_attack_right, basic_player_attack_up]
        quiver_player = [quiver_player_down, quiver_player_left, quiver_player_right, quiver_player_up, quiver_player_attack_down, quiver_player_attack_left,quiver_player_attack_right, quiver_player_attack_up, quiver_player_shoot_down, quiver_player_shoot_left, quiver_player_shoot_right, quiver_player_shoot_up]
        player = basic_player + quiver_player
        return player

    def arrowImages(self):
        """
        Returns a list of arrow images
        """
        return[load_image('Arrow_Down.png'), load_image('Arrow_Left.png'), load_image('Arrow_Right.png'), load_image('Arrow_Up.png')]

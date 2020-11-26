class Settings:
    # 储存游戏中的所有设置类

    def __init__(self):
        #  初始化游戏设置
        self.screen_width = 1000  # 游戏窗口的大小
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # 背景颜色设置

        # 飞船速度设置
        self.ship_speed = 1.5

        #  子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 100  # 限制子弹最大数目

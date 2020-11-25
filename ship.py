import pygame


class Ship:
    # 飞船类

    def __init__(self, ai_game):
        # 初始化飞船并初始化其位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(
            "/Users/shilin/Documents/VSCode/Python/alien_incasion/images/ship.png"
        )
        # 改变飞船大小
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # 放置飞船到窗口底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = ai_game.settings

        # 在飞船的x属性中储存小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # 根据移动标志调整飞船位置
        # 限制移动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # 更新self.x的值

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed  # 更新self.y的值

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 根据self.x的值更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

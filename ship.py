import pygame


class Ship:
    # 飞船类

    def __init__(self, ai_game):
        # 初始化飞船并初始化其位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("/Users/shilin/Documents/VSCode/Python/alien_incasion/images/ship.png")
        # 改变飞船大小
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # 放置飞船到窗口底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

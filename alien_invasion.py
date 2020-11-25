import sys
import pygame
from settings import Settings
from ship import Ship


class AlinenInvasion:
    # 管理游戏资源和行为的类
    def __init__(self):
        # 初始化游戏并创建游戏资源
        pygame.init()  # 初始化背景设置
        self.settings = Settings()  # 设置类
        # 设置窗口大小
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 初始化ship
        self.ship = Ship(self)

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # 绘制飞船

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlinenInvasion()
    ai.run_game()

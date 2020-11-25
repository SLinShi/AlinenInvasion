import sys
import pygame
from settings import Settings
from ship import Ship


class AlinenInvasion:
    # 管理游戏资源和行为的类
    def __init__(self):
        # 初始化游戏并创建游戏资源
        # 初始化背景设置
        pygame.init()

        # 初始化设置类
        self.settings = Settings()

        # 设置窗口大小
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # 全屏运行
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # 初始化ship
        self.ship = Ship(self)

    def run_game(self):
        # 开始游戏主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    # 监视键盘和鼠标事件
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # 响应按下
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船标志改变
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        # Q快捷键退出
        elif event.key == pygame.K_q:
            sys.exit()

    #  响应松开
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    # 更新屏幕
    def _update_screen(self):
        # 每次循环重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 绘制飞船

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlinenInvasion()
    ai.run_game()

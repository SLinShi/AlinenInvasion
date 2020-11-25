import sys
import pygame


class AlinenInvasion:
    # 管理游戏资源和行为的类
    def __init__(self):
        # 初始化游戏并创建游戏资源
        pygame.init()  # 初始化背景设置

        self.screen = pygame.display.set_mode((1200, 800))  # 创建一个显示窗口
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # 开始游戏主循环
        while Ture:
            
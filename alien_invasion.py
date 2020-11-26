import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # 初始化子弹编组
        self.bullets = pygame.sprite.Group()

        # 初始化外星人编组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()  # 创建外星人

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
        elif event.key == pygame.K_SPACE:
            # 空格开火
            if len(self.bullets) < self.settings.bullet_allowed:
                self._fire_bullet()

        # Q快捷键退出
        elif event.key == pygame.K_q:
            sys.exit()

    # 创建一颗子弹加入编组
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

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

    # 更新子弹位置并删除消失的子弹
    def _update_bullets(self):
        self.bullets.update()  # 每个子弹调用bullet中的update

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # 创建一个外星人并放置在当前行
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # 创建外星人群
    def _create_fleet(self):
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) -
                             ship_height)
        number_rows = available_space_y // (3 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    # 更新屏幕
    def _update_screen(self):
        # 每次循环重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 绘制飞船

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 调用编组的draw方法
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        # 开始游戏主循环
        while True:
            self._check_events()
            self.ship.update()
            # 更新子弹
            self._update_bullets()
            # 更新屏幕
            self._update_screen()


if __name__ == '__main__':
    ai = AlinenInvasion()
    ai.run_game()

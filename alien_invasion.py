import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf



def run_game():
    #初始化pygame、设置、和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Aline Invasion")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个存储子弹的编组
    bullets= Group()
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
          ship.update()
          print(len(bullets))
          gf.updata_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
          gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        #每次循环时都重绘屏幕
        gf.updata_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
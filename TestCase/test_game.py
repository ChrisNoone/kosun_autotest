# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class GameTest(BaseCase):
    @classmethod
    def setUpClass(cls):
        url = ConfigHelper().conf_read('fusion', 'home_url')
        cls.driver = BaseDriver('Chrome')
        cls.driver.maximize_window()
        cls.driver.navigate(url)
        time.sleep(3)
        cls.login_page = login_page.LoginPageElement(cls.driver)
        cls.login_page.login()
        cls.home_page = home_page.HomePageElement(cls.driver)
        cls.home_page.click_game()
        cls.game_page = game_page.GamePageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('游戏管理', '分类列表', '分类名称'),
                ('游戏管理', '游戏设置', '游戏名'),
                ('游戏管理', '注单管理', '订单编号'),
                ('游戏管理', '平台设置', '开关'),
                ('游戏管理', '转额记录', '转额金额'),
                ('返水管理', '规则组', '组名称'),
                ('返水管理', '返水规则', '快速设置'),
                ('返水管理', '返水优惠', '电子游艺'),
                ('返水管理', '历史返水', '返水金额'),
                ('工资管理', '代理工资设置', '代理级别'),
                ('工资管理', '工资管理', '期号')
                ]
        for d in data:
            self.game_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time
import unittest


class SportsTest(BaseCase):
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
        cls.home_page.click_sports()
        cls.sports_page = sports_page.SportsPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('体育设置', '皇冠公告', '日期'),
                ('体育设置', '球类管理', '英文名'),
                ('体育设置', '层级返水设置', '返水比例'),
                ('赛事管理', '联赛管理', '选择体育'),
                ('赛事管理', '比赛管理', '球队名'),
                ('赛事管理', '冠军管理', '联赛或盘口名'),
                ('注单管理', '全部注单', '比赛编号'),
                ('注单管理', '滚球未审核注单', '手动刷新'),
                ('注单管理', '异常注单', '比赛编号'),
                ('工资管理', '代理工资设置', '查看教程'),
                ('工资管理', '工资管理', '重置期数')
                ]
        for d in data:
            self.sports_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

    def func_search_sportsmatches(self, preset='preset', expect='expect'):
        menu = ('赛事管理', '联赛管理')
        data = [{'sport': '竞彩足球', 'status': '', 'league': ''}]
        self.logger.info(preset, expect)
        for d in data:
            self.sports_page.open_menu(*menu)
            self.sports_page.search_sportsmatches(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

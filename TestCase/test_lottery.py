# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class LotteryTest(BaseCase):
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
        cls.home_page.click_lottery()
        cls.lottery_page = lottery_page.LotteryPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('分销管理', '规则组', '规则名称'),
                ('分销管理', '黑名单', '用户名'),
                ('彩票管理', '注单管理', '会员账号'),
                ('彩票管理', '开奖结果', '彩种'),
                ('彩票管理', '投注分析', '彩种'),
                ('工资管理', '代理工资设置', '代理级别'),
                ('工资管理', '工资管理', '期号'),
                ('工资管理', '代理作弊名单', '用户层级'),
                ('彩票设置', '展示分类', '热门'),
                ('彩票设置', '彩种设置', '时时彩'),
                ('彩票设置', '限额设置', '六合彩'),
                ('彩票设置', '彩种列表', '分类'),
                ('彩票设置', '玩法列表', '彩种分类'),
                ('彩票设置', '分类设置', '最大返点'),
                ('返水管理', '规则组', '规则名称'),
                ('返水管理', '期数管理', '期数名称'),
                ('返水管理', '黑名单', '用户名')
                ]
        for d in data:
            self.lottery_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

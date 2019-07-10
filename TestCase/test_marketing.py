# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class MarketingTest(BaseCase):
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
        cls.home_page.click_marketing()
        cls.marketing_page = marketing_page.MarketingPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('优惠券配置', '优惠券列表', '优惠券名称'),
                ('活动设置', '优惠活动列表', '活动名称'),
                ('数据查询', '优惠券查询', '用户账号'),
                ('互动大厅', '成员列表', '禁言状态'),
                ('互动大厅', '红包统计', '红包留言'),
                ('互动大厅', '跟单统计', '分单时间'),
                ('互动大厅', '基础设置', '互动大厅总开关')
                ]
        for d in data:
            self.marketing_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

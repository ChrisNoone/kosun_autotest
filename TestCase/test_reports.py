# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class ReportsTest(BaseCase):
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
        cls.home_page.click_reports()
        cls.reports_page = reports_page.ReportsPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('报表管理', '综合报表', '总充值'),
                ('报表管理', '电子游艺总览', '平台名称'),
                ('报表管理', '体彩总览', '投注金额'),
                ('报表管理', '数字彩代理报表', '总充值'),
                ('报表管理', '出入汇总', '平台实际盈亏'),
                ('报表管理', '支付平台入款汇总', '支付平台'),
                ('报表管理', '渠道报表', '渠道名称'),
                ('报表管理', '会员报表', '真实姓名')
                ]
        for d in data:
            self.reports_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

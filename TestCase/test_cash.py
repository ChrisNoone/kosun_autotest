# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class CashTest(BaseCase):
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
        cls.home_page.click_cash()
        cls.cash_page = cash_page.CashPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('充值中心', '支付银行列表', '银行名称'),
                ('充值中心', '可用渠道列表', '序号'),
                ('充值中心', '代付配置', '商户号'),
                ('充值中心', '渠道商户设置', '商户号'),
                ('充值中心', '好友支付类型', '序号'),
                ('充值中心', '支付类型设置', '分组ID'),
                ('充值中心', '好友支付列表', '支付账号'),
                ('充值中心', '支付类型分组', '分组ID'),
                ('充值中心', '公司支付账号', '公司入款账号'),
                ('优惠管理', '注册优惠设定', '注册送彩金'),
                ('现金管理', '金流管理', '会员账号'),
                ('现金管理', '即时检查', '订单号'),
                ('现金管理', '线上出款', '会员层级'),
                ('现金管理', '公司入款', '上级用户'),
                ('现金管理', '线上入款', '层级'),
                ('现金管理', '人工出款', '会员'),
                ('现金管理', '人工入款', '订单编号')
                ]
        for d in data:
            self.cash_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

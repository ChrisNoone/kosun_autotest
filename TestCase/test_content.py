# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class ContentTest(BaseCase):
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
        cls.home_page.click_content()
        cls.content_page = content_page.ContentPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('广告管理', '广告位管理', '广告类型'),
                ('活动管理', '活动列表', '活动名称'),
                ('活动管理', '活动类型', '编辑时间'),
                ('资讯管理', '资讯列表', '资讯标题'),
                ('资讯管理', '文档管理', '标题'),
                ('帮助管理', '帮助列表', '标题'),
                ('前台设置', '配置管理', 'ID'),
                ('前台设置', '弹窗设置', '位置'),
                ('推送管理', '消息推送', '日期区间'),
                ('推送管理', '推送渠道', '渠道名称'),
                ('公告管理', '站内信', '用户名'),
                ('公告管理', '公告列表', '公告类型')
                ]
        for d in data:
            self.content_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

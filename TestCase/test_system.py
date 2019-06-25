# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class SystemTest(BaseCase):
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
        cls.home_page.click_system()
        cls.system_page = system_page.SystemPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jump_menus(self):
        data = [('系统设置', '网站设置', 'app_name'),
                ('系统设置', '菜单管理', '顶级菜单'),
                ('系统设置', '基础壳配置', '批量设定版本号'),
                ('系统设置', '基础壳多域名', '域名管理'),
                ('行为管理', '行为日志', '行为名称'),
                ('行为管理', '用户行为', '行为编号'),
                ('后台用户管理', '权限管理', '分组'),
                ('后台用户管理', '用户反馈', '反馈日期'),
                ('后台用户管理', '管理员信息', '昵称')
                ]
        for d in data:
            self.system_page.open_menu(*d)
            self.assertEqual(self.driver.exist_ele(d[2]), True, '%s查询结果为空' % str(d))

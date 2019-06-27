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

    def test_switch_siteconfig_tab(self):
        try:
            menu = ('系统设置', '网站设置')
            self.system_page.open_menu(*menu)
            data = [('注册配置', '推荐人ID'), ('pc', '首页:悬浮'), ('公共', '在线客服地址'), ('h5', '开屏图片'),
                    ('app', '开屏图片'), ('代理注册配置', '邮箱')]
            for d in data:
                self.system_page.switch_siteconfig_tab(d[0])
                self.assertEqual(self.driver.exist_ele(d[1]), True, '%s查询结果为空' % str(d))
        except Exception as e:
            self.logger.error(e)

    def test_search_menumanage(self):
        menu = ('系统设置', '菜单管理')
        data = [{'menuname': '体育管理', 'url': ''},
                {'menuname': '', 'url': 'Lottery'}]
        for d in data:
            self.system_page.open_menu(*menu)
            self.system_page.search_menumanage(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    def test_search_baseshell(self):
        menu = ('系统设置', '基础壳配置')
        data = [{'type': 'web页面', 'platform': '', 'uniquecode': '', 'name': '', 'version': ''},
                {'type': '', 'platform': '安卓', 'uniquecode': '', 'name': '', 'version': ''},
                {'type': '', 'platform': '', 'uniquecode': 'fusion.apk', 'name': '', 'version': ''},
                {'type': '', 'platform': '', 'uniquecode': '', 'name': 'fbgXXASDASDASDAS', 'version': ''},
                {'type': '', 'platform': '', 'uniquecode': '', 'name': '', 'version': '59'}]
        for d in data:
            self.system_page.open_menu(*menu)
            self.system_page.search_baseshell(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    def test_search_baseshelldomain(self):
        menu = ('系统设置', '基础壳多域名')
        data = [{'name': 'fusion.cpmobileapi.net'}]
        for d in data:
            self.system_page.open_menu(*menu)
            self.system_page.search_baseshelldomain(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    def test_search_actionlog(self):
        menu = ('行为管理', '行为日志')
        data = [{'ip': '47.254.201.214', 'user': '', 'actionname': '', 'actor': ''},
                {'ip': '', 'user': '', 'actionname': '', 'actor': 'qa'}]
        for d in data:
            self.system_page.open_menu(*menu)
            self.system_page.search_actionlog(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

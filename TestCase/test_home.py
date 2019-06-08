# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class HomeTest(BaseCase):
    @classmethod
    def setUpClass(cls):
        url = ConfigHelper().conf_read('fusion', 'home_url')
        cls.driver = BaseDriver('Chrome')
        cls.driver.maximize_window()
        cls.driver.navigate(url)
        time.sleep(3)
        cls.login_page = login_page.LoginPageElement(cls.driver)
        cls.login_page.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_system_a(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_system()
        url = self.home_page.get_url()
        self.assertIn('admin', url, '页面没有跳转')

    def test_user_a(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_user()
        url = self.home_page.get_url()
        self.assertIn('special', url, '页面没有跳转')

# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class LoginTest(BaseCase):
    @classmethod
    def setUpClass(cls):
        url = ConfigHelper().conf_read('fusion', 'home_url')
        cls.driver = BaseDriver('Chrome')
        cls.driver.maximize_window()
        cls.driver.navigate(url)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip('test')
    def test_login(self):
        self.login_page = login_page.LoginPageElement(self.driver)
        self.login_page.login()
        url = self.login_page.get_url()
        self.assertNotIn('login', url, '未登录成功，页面没有跳转')

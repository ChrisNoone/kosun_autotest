# coding: utf-8

from Common.base import *
from Common.box import *
from PageObject import *
import time


class UserTest(BaseCase):
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
        cls.home_page.click_user()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @unittest.skip('repeat with test_search_specialagent')
    def test_jump_specialagent(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_specialagent()
        self.assertEqual(self.driver.exist_ele('特殊代理用户'), True)

    def test_jump_channel(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_channel()
        self.assertEqual(self.driver.exist_ele('渠道类型'), True)

    def test_jump_user(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_user()
        self.assertEqual(self.driver.exist_ele('用户类别'), True)

    def test_jump_userlevel(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_userlevel()
        self.assertEqual(self.driver.exist_ele('层级名称'), True)

    def test_jump_loginlog(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_loginlog()
        self.assertEqual(self.driver.exist_ele('登录IP'), True)

    def test_jump_agentManegement(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_agentManegement()
        self.assertEqual(self.driver.exist_ele('代理状态'), True)

    def test_jump_agentcode(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_agentcode()
        self.assertEqual(self.driver.exist_ele('代理推广码'), True)

    def test_search_specialagent(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_specialagent()
        self.user_page.search_specialagent()
        self.assertEqual(self.driver.exist_ele('修改密码'), True)

    def test_search_agentcode(self):
        self.user_page = user_page.UserPageElement(self.driver)
        self.user_page.click_agentcode()
        # data1 = {'code': '501315', 'agent': ''}
        data2 = {'code': '', 'agent': 'demo02'}
        self.user_page.search_agentcode(**data2)
        self.assertEqual(self.driver.exist_ele('demo02'), True)

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

    def test_jump_system(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_system()
        self.assertEqual(self.driver.exist_ele('行为管理'), True)

    def test_jump_user(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_user()
        self.assertEqual(self.driver.exist_ele('会员管理'), True)

    def test_jump_reports(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_reports()
        self.assertEqual(self.driver.exist_ele('出入汇总'), True)

    def test_jump_sports(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_sports()
        self.assertEqual(self.driver.exist_ele('体育设置'), True)

    def test_jump_marketing(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_marketing()
        self.assertEqual(self.driver.exist_ele('互动大厅'), True)

    def test_jump_game(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_game()
        self.assertEqual(self.driver.exist_ele('游戏管理'), True)

    def test_jump_content(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_content()
        self.assertEqual(self.driver.exist_ele('广告管理'), True)

    def test_jump_lottery(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_lottery()
        self.assertEqual(self.driver.exist_ele('彩票管理'), True)

    def test_jump_cash(self):
        self.home_page = home_page.HomePageElement(self.driver)
        # 每次执行前先回到首页
        self.home_page.click_home()
        self.home_page.click_cash()
        self.assertEqual(self.driver.exist_ele('充值中心'), True)

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
        cls.user_page = user_page.UserPageElement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @unittest.skip('repeat with test_search_specialagent')
    def test_jump_specialagent(self):
        self.user_page.click_specialagent()
        self.assertEqual(self.driver.exist_ele('特殊代理用户'), True)

    def test_jump_channel(self):
        self.user_page.click_channel()
        self.assertEqual(self.driver.exist_ele('渠道类型'), True)

    def test_jump_user(self):
        self.user_page.click_user()
        self.assertEqual(self.driver.exist_ele('用户类别'), True)

    def test_jump_userlevel(self):
        self.user_page.click_userlevel()
        self.assertEqual(self.driver.exist_ele('层级名称'), True)

    def test_jump_loginlog(self):
        self.user_page.click_loginlog()
        self.assertEqual(self.driver.exist_ele('登录IP'), True)

    def test_jump_agentManegement(self):
        self.user_page.click_agentManegement()
        self.assertEqual(self.driver.exist_ele('代理状态'), True)

    def test_jump_agentcode(self):
        self.user_page.click_agentcode()
        self.assertEqual(self.driver.exist_ele('代理推广码'), True)

    def test_search_specialagent(self):
        self.user_page.click_specialagent()
        self.user_page.search_specialagent()
        self.assertEqual(self.driver.table_is_not_null(), True)

    def test_search_agentcode(self,):
        data = [{'code': '501315', 'agent': ''},
                {'code': '', 'agent': 'demo01'}]
        for d in data:
            self.user_page.click_agentcode()
            self.user_page.search_agentcode(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    # 数据驱动，构造testcase
    # @staticmethod
    # def creat_test(**kw):
    #     def func(self):
    #         self.test_search_agentcode(**kw)
    #     return func

    def test_search_agentManegement(self):
        data = [{'user': 'artee22', 'status': ''},
                {'user': '', 'status': '已拒绝'},
                {'user': '', 'status': '待审核'}]
        for d in data:
            self.user_page.click_agentManegement()
            self.user_page.search_agentManegement(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    def test_search_loginlog(self):
        data = [{'ip': '47.254.201.214', 'user': '', 'mode': ''},
                {'ip': '', 'user': 'artee23', 'mode': ''},
                {'ip': '47.254.201.214', 'user': 'demo', 'mode': '精确匹配'}]
        for d in data:
            self.user_page.click_loginlog()
            self.user_page.search_loginlog(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

    def test_search_userlevel(self):
        data = [{'levelname': '铂金会员'},
                {'levelname': 'test'}
                ]
        for d in data:
            self.user_page.click_userlevel()
            self.user_page.search_userlevel(**d)
            self.assertEqual(self.driver.table_is_not_null(), True, '%s查询结果为空' % d)

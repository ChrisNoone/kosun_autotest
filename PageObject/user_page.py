# coding: utf-8

from Common.base import *
from Common.box import *


class UserPageElement(BasePage):
    cd_user = YamlHelper.yaml_read('./Yaml/fusion.yaml')['User']
    sa = ConfigHelper().conf_read('fusion', 'apecialagent')

    def click_specialagent(self):
        self.driver.click(self.cd_user['specialagentA'])
        self.driver.forced_wait(1)

    def click_channel(self):
        self.driver.click(self.cd_user['channelA'])
        self.driver.forced_wait(1)

    def click_user(self):
        self.driver.click(self.cd_user['userA'])
        self.driver.forced_wait(1)

    def click_userlevel(self):
        self.driver.click(self.cd_user['userlevelA'])
        self.driver.forced_wait(1)

    def click_loginlog(self):
        self.driver.click(self.cd_user['loginlogA'])
        self.driver.forced_wait(1)

    def click_agentManegement(self):
        self.driver.click(self.cd_user['agentManegementA'])
        self.driver.forced_wait(1)

    def click_agentcode(self):
        self.driver.click(self.cd_user['agentcodeA'])
        self.driver.forced_wait(1)

    def search_specialagent(self):
        self.driver.type(self.cd_user['specialagentInp'], self.sa)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

    def search_agentcode(self, **kw):
        if kw['code'] is not None:
            self.driver.type(self.cd_user['agentcodeInp'], kw['code'])
        if kw['agent'] is not None:
            self.driver.type(self.cd_user['agentInp'], kw['agent'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

    def search_agentManegement(self, **kw):
        if kw['user']:
            self.driver.type(self.cd_user['userInp'], kw['user'])
        if kw['status']:
            self.driver.click(self.cd_user['agentstatusDiv'])
            self.driver.forced_wait(0.5)
            self.driver.logger.debug(self.driver.get_attribute(self.cd_user['statusLi'], 'role'))
            self.driver.click_by_text(self.cd_user['statusLi'], kw['status'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

    def search_loginlog(self, **kw):
        if kw['ip']:
            self.driver.type_search_input('IP', kw['ip'])
        if kw['user']:
            self.driver.type_search_input('用户名', kw['user'])
        if kw['mode']:
            self.driver.type_search_input('匹配模式', kw['mode'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

    def search_userlevel(self, **kw):
        if kw['levelname']:
            self.driver.type_search_input('层级名称', kw['levelname'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

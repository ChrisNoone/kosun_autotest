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
        self.driver.click(self.cd_user['specialagentA'])
        self.driver.type(self.cd_user['specialagentInp'], self.sa)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

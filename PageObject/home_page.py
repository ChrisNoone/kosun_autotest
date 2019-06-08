# coding: utf-8

from Common.base import *
from Common.box import *


class HomePageElement(BasePage):
    cd_home = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Home']

    def click_home(self):
        self.driver.click(self.cd_home['homeA'])
        self.driver.forced_wait(2)

    def click_system(self):
        self.driver.click(self.cd_home['systemA'])
        self.driver.forced_wait(2)

    def click_user(self):
        self.driver.click(self.cd_home['userA'])
        self.driver.forced_wait(2)

    # def get_url(self):
    #     self.driver.forced_wait(3)
    #     url = self.driver.get_url()
    #     return url

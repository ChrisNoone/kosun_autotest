# coding: utf-8

from Common.base import *
from Common.box import *


class HomePageElement(BasePage):
    cd_home = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Home']

    def click_home(self):
        self.driver.click(self.cd_home['homeA'])
        self.driver.forced_wait(2)

    def click_system(self):
        self.driver.click_by_text(self.cd_home['systemA'], "系统")
        self.driver.forced_wait(2)

    def click_user(self):
        self.driver.click(self.cd_home['userA'])
        self.driver.forced_wait(2)

    def click_reports(self):
        self.driver.click(self.cd_home['reportsA'])
        self.driver.forced_wait(2)

    def click_sports(self):
        self.driver.click(self.cd_home['sportsA'])
        self.driver.forced_wait(2)

    def click_marketing(self):
        self.driver.click(self.cd_home['marketingA'])
        self.driver.forced_wait(2)

    def click_game(self):
        self.driver.click(self.cd_home['gameA'])
        self.driver.forced_wait(2)

    def click_content(self):
        self.driver.click(self.cd_home['contentA'])
        self.driver.forced_wait(2)

    def click_lottery(self):
        self.driver.click(self.cd_home['lotteryA'])
        self.driver.forced_wait(2)

    def click_cash(self):
        self.driver.click(self.cd_home['cashA'])
        self.driver.forced_wait(2)

    # def get_url(self):
    #     self.driver.forced_wait(3)
    #     url = self.driver.get_url()
    #     return url

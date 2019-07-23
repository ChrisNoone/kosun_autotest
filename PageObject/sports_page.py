# coding: utf-8

from Common.base import *
from Common.box import *


class SportsPageElement(BasePage):
    cd_sports = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Sports']

    def open_menu(self, *args):
        group_div = 'x, //div[@class="menu"]//span[contains(text(), "%s")]' % args[0]
        memu_a = 'x, //a[contains(text(), "%s")]' % args[1]
        if self.driver.exist_ele(args[1]):
            self.driver.click(memu_a)
        else:
            self.driver.click(group_div)
            self.driver.forced_wait(0.5)
            self.driver.click(memu_a)
        self.driver.forced_wait(1)

    def search_sportsmatches(self, **kw):
        if kw['sport']:
            self.driver.type_search_input('选择体育', kw['sport'])
        if kw['status']:
            self.driver.type_search_input('状态', kw['status'])
        if kw['league']:
            self.driver.type_search_input('联赛', kw['league'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_sports['searchB'])
        self.driver.forced_wait(2)

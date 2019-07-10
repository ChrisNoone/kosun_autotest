# coding: utf-8

from Common.base import *
from Common.box import *


class ContentPageElement(BasePage):
    cd_content = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Content']

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
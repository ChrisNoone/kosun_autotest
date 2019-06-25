# coding: utf-8

from Common.base import *
from Common.box import *


class SystemPageElement(BasePage):
    cd_system = YamlHelper.yaml_read('./Yaml/fusion.yaml')['System']

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

    def switch_siteconfig_tab(self, tab_name):
        locator = 'x, //div[@class="ant-tabs-nav-wrap"]//*[contains(text(), "%s")]' % tab_name
        self.driver.click(locator)
        self.driver.forced_wait(1)

    def search_menumanage(self, **kw):
        if kw['menuname']:
            self.driver.type_search_input('菜单名称', kw['menuname'])
        if kw['url']:
            self.driver.type_search_input('URL', kw['url'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_system['searchB'])
        self.driver.forced_wait(2)

    def search_baseshell(self, **kw):
        if kw['type']:
            self.driver.type_search_input('app类型', kw['type'])
        if kw['platform']:
            self.driver.type_search_input('设备平台', kw['platform'])
        if kw['uniquecode']:
            self.driver.type_search_input('应用唯一标识', kw['uniquecode'])
        if kw['name']:
            self.driver.type_search_input('app名称', kw['name'])
        if kw['version']:
            self.driver.type_search_input('版本号', kw['version'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_system['searchB'])
        self.driver.forced_wait(2)

    def search_baseshelldomain(self, **kw):
        if kw['name']:
            self.driver.type_search_input('域名名称', kw['name'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_system['searchB'])
        self.driver.forced_wait(2)

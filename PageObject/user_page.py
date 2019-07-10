# coding: utf-8

from Common.base import *
from Common.box import *


class UserPageElement(BasePage):
    cd_user = YamlHelper.yaml_read('./Yaml/fusion.yaml')['User']
    sa = ConfigHelper().conf_read('fusion', 'apecialagent')

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

    def search_user(self, **kw):
        if kw['usertype']:
            self.driver.type_search_input('用户类别', kw['usertype'])
        if kw['bank']:
            self.driver.type_search_input('银行账号', kw['bank'])
        if kw['mail']:
            self.driver.type_search_input('邮箱', kw['mail'])
        if kw['number']:
            self.driver.type_search_input('手机号码', kw['number'])
        if kw['realname']:
            self.driver.type_search_input('真实姓名', kw['realname'])
        if kw['user']:
            self.driver.type_search_input('用户名', kw['user'])
        if kw['userlevel']:
            self.driver.type_search_input('用户层级', kw['userlevel'])
        if kw['mode']:
            self.driver.type_search_input('匹配模式', kw['mode'])
        if kw['resource']:
            self.driver.type_search_input('客户来源', kw['resource'])
        if kw['is_online']:
            self.driver.type_search_input('是否筛选在线用户', kw['is_online'])
        if kw['status']:
            self.driver.type_search_input('用户状态', kw['status'])
        if kw['channel']:
            self.driver.type_search_input('注册渠道', kw['channel'])
        if kw['qq']:
            self.driver.type_search_input('QQ', kw['qq'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

    def search_channel(self, **kw):
        if kw['channeltype']:
            self.driver.type_search_input('渠道类型', kw['channeltype'])
        if kw['channelname']:
            self.driver.type_search_input('渠道名称', kw['channelname'])
        if kw['agentcode']:
            self.driver.type_search_input('代理码', kw['agentcode'])
        self.driver.forced_wait(1)
        self.driver.click(self.cd_user['searchB'])
        self.driver.forced_wait(2)

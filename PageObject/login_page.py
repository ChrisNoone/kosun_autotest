# coding: utf-8

from Common.base import *
from Common.box import *


class LoginPageElement(BasePage):
    cd_login = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Login']

    def login(self):
        self.driver.type(self.cd_login['usernameInp'], 'qa')
        self.driver.type(self.cd_login['pwdInp'], '123456')
        # captcha = self.driver.get_attribute(self.cd_login['captchaImg'], 'src')
        # capt = Captcha()
        # text = capt.captcha(captcha)
        # self.driver.type(self.cd_login['captchaInp'], text)
        # 等待手动输入验证码
        self.driver.forced_wait(5)
        self.driver.click(self.cd_login['loginBut'])
        self.driver.forced_wait(5)

    # def get_url(self):
    #     self.driver.forced_wait(3)
    #     url = self.driver.get_url()
    #     return url

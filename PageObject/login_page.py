# coding: utf-8

from Common.base import *
from Common.box import *


class LoginPageElement(BasePage):
    cd_login = YamlHelper.yaml_read('./Yaml/fusion.yaml')['Login']

    def login(self):
        conf = ConfigHelper()
        username = conf.conf_read('fusion', 'username')
        pwd = conf.conf_read('fusion', 'password')
        self.driver.type(self.cd_login['usernameInp'], username)
        self.driver.type(self.cd_login['pwdInp'], pwd)
        # captcha = self.driver.get_attribute(self.cd_login['captchaImg'], 'src')
        # capt = Captcha()
        # text = capt.captcha(captcha)
        # self.driver.type(self.cd_login['captchaInp'], text)
        # 等待手动输入验证码
        self.driver.click(self.cd_login['captchaInp'])
        self.driver.forced_wait(2)
        self.driver.type(self.cd_login['captchaInp'], '1234')
        self.driver.click(self.cd_login['loginBut'])
        self.driver.explicitly_wait('x, //*[contains(text(), "现金系统")]', 20)

    # def get_url(self):
    #     self.driver.forced_wait(3)
    #     url = self.driver.get_url()
    #     return url

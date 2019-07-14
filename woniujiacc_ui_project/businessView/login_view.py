# coding=utf-8
from common.desired_cap import appium_desired
from common.common_fun import Common
import logging

class LoginView(Common):
    def __init__(self):
        self.driver = appium_desired()
        # 获取定位元素
        self.username_type = self.get_element_loc('LoginPage', 'userName')
        self.password_type = (self.get_element_loc('LoginPage', 'password'))
        self.loginBtn = (self.get_element_loc('LoginPage', 'login'))

    def login_action(self, username, password):
        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.send_keys(*self.username_type, text=username)
        logging.info('password is:%s' % password)
        self.send_keys(*self.password_type, text=password)
        logging.info('click loginBtn')
        self.click(*self.loginBtn)
        logging.info('login finished!')

if __name__ == '__main__':
    login = LoginView()
    login.login_action("15616699600", "zh123123")



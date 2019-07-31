# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from common.desired_cap import appium_desired
from common.common_fun import Common
import logging

class LoginView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.username_type = Common(driver).get_by_loc('LoginPage', 'userName')
        self.password_type = Common(driver).get_by_loc('LoginPage', 'password')
        self.loginBtn = Common(driver).get_by_loc('LoginPage', 'login')
        self.my_tab = Common(driver).get_by_loc('MinePage', 'my_tab')
        self.sys_setting = Common(driver).get_by_loc('MinePage', 'setting_text')
        self.logout_btn = Common(driver).get_by_loc('MinePage', 'logout_btn')
        self.logout_text = Common(driver).get_by_loc('MinePage', 'logout_text')

    # 执行登录操作
    def login_action(self, username, password):
        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        Common(self.driver).send_keys(self.username_type, text=username)
        logging.info('password is:%s' % password)
        Common(self.driver).send_keys(self.password_type, text=password)
        logging.info('click loginBtn')
        Common(self.driver).click(self.loginBtn)
        Common(self.driver).getScreenShot('login')
        logging.info('login finished!')

    # 执行退出登录操作
    def logout_action(self):
        logging.info("----------logout action---------")
        Common(self.driver).click(self.my_tab)
        Common(self.driver).click(self.sys_setting)
        Common(self.driver).click(self.logout_btn)
        Common(self.driver).click(self.logout_text)

    # 检查登录状态
    def check_login_status(self):
        try:
            Common(self.driver).find_element_by_uiautomator(self.my_tab)
        except NoSuchElementException:
            logging.info("login failure!")
            # Common(self.driver).getScreenShot('login')
            return False
        else:
            logging.info("login success!")
            self.logout_action()
            return True

if __name__ == '__main__':
    driver = appium_desired()
    login = LoginView(driver)
    # test_login.login_action("15616699600", "zh123123")



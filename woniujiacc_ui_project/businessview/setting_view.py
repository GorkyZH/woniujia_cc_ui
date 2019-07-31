# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging

"""封装系统设置页操作基类"""
class SettingView(Common):
    def __init__(self, driver):
        # 定位元素
        self.driver = driver
        self.title_loc = Common(driver).get_by_loc('MinePage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('MinePage', 'back_btn')
        self.phrase_setting_loc = Common(driver).get_by_loc('MinePage', 'phrase_setting_text')
        self.update_pwd_loc = Common(driver).get_by_loc('MinePage', 'update_pwd_text')
        self.logout_btn_loc = Common(driver).get_by_loc('MinePage', 'logout_btn')
        self.logout_text_loc = Common(driver).get_by_loc('MinePage', 'logout_text')

        # 操作元素
        self.get_title = self.getText(self.title_loc)
        self.get_phrase_setting_text = self.getText(self.phrase_setting_loc)
        self.get_update_pwd_text = self.getText(self.update_pwd_loc)

    # 点击常用语设置
    def goto_phrase_setting(self):
        logging.info("============跳转到常用语设置页==============")
        self.click(self.phrase_setting_loc)

    # 点击修改密码
    def goto_update_pwd(self):
        logging.info("============跳转到修改密码页==============")
        self.click(self.update_pwd_loc)

if __name__ == '__main__':
    driver = appium_desired()
    setting = SettingView(driver)
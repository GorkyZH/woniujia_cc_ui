# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired

"""封装微信商机页基础类"""
class ExtensionView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.title_loc = Common(driver).get_by_loc('ExtensionPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('ExtensionPage', 'back_btn')

        self.get_title = Common(driver).getText(self.title_loc)

if __name__ == '__main__':
    driver = appium_desired()
    extension = ExtensionView(driver)
# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time

"""封装消息页基础类"""
class MessageView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.message_tab_loc = Common(driver).get_by_loc('HomePage', 'message_tab')
        self.click(self.message_tab_loc)
        time.sleep(5)

        self.title_loc = Common(driver).get_by_loc('MessagePage', 'title')
        self.get_title = Common(driver).getText(self.title_loc)

if __name__ == '__main__':
    driver = appium_desired()
    message = MessageView(driver)
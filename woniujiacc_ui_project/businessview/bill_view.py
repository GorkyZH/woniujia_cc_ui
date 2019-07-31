# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired

"""封装海报页基础类"""
class BillView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.title_loc = Common(driver).get_by_loc('BillPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('BillPage', 'back_btn')

        self.get_title = Common(driver).getText(self.title_loc)

if __name__ == '__main__':
    driver = appium_desired()
    bill = BillView(driver)
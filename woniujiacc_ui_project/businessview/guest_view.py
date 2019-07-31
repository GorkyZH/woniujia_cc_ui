# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time

"""封装客户页基础类"""
class GuestView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.guest_tab_loc = Common(driver).get_by_loc('HomePage', 'guest_tab')
        self.click(self.guest_tab_loc)
        time.sleep(5)

        self.title_loc = Common(driver).get_by_loc('GuestPage', 'title')
        self.robguest_btn_loc = Common(driver).get_by_loc('GuestPage', 'robguest_btn')
        self.newguest_btn_loc = Common(driver).get_by_loc('GuestPage', 'newguest_btn')
        self.search_text_loc = Common(driver).get_by_loc('GuestPage', 'search_text')
        self.level_text_loc = Common(driver).get_by_loc('GuestPage', 'level_text')
        self.state_text_loc = Common(driver).get_by_loc('GuestPage', 'state_text')
        self.mark_text_loc = Common(driver).get_by_loc('GuestPage', 'mark_text')

        self.get_title = Common(driver).getText(self.title_loc)
        self.get_level_text = Common(driver).getText(self.level_text_loc)
        self.get_state_text = Common(driver).getText(self.state_text_loc)
        self.get_mark_text = Common(driver).getText(self.mark_text_loc)

    # 操作点击抢客按钮
    def goto_robguest(self):
        logging.info("============跳转到抢客页==============")
        self.click(self.robguest_btn_loc)

    # 操作点击新增图标
    def goto_newguest(self):
        logging.info("============跳转到新增客户页==============")
        self.click(self.newguest_btn_loc)

    # 操作点击搜索框
    def goto_searchguest(self):
        logging.info("============跳转到搜索客户页==============")
        self.click(self.search_text_loc)

if __name__ == '__main__':
    driver = appium_desired()
    guest = GuestView(driver)
# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired

"""封装驻守楼盘页基础类"""
class OwnbuildingView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.title_loc = Common(driver).get_by_loc('BuildPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('BuildPage', 'back_btn')
        self.describe_build_loc = Common(driver).get_by_loc('MinePage', 'describe_total_text')
        self.build_lv_loc = Common(driver).get_by_loc('MinePage', 'build_listview')
        self.build_item_loc = Common(driver).get_by_loc('MinePage', 'build_item')

        self.get_title = Common(driver).getText(self.title_loc)
        self.get_describe_build_text = Common(driver).getText(self.describe_build_loc)

    # 判断所有item是否在listview中
    def is_item_in_listview(self, list_data):
        items_text = Common(self.driver).get_items_text(self.build_item_loc)
        if items_text == list_data:
            return True

if __name__ == '__main__':
    driver = appium_desired()
    build = OwnbuildingView(driver)
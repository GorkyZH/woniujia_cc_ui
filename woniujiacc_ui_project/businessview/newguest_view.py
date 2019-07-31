# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time

class NewguestView(Common):
    def __init__(self, driver):
        self.driver = driver

        # 定位元素
        self.title_loc = Common(driver).get_by_loc('GuestPage', 'new_guest_title')
        self.back_btn_loc = Common(driver).get_by_loc('GuestPage', 'back__btn')
        self.guest_name_text_loc = Common(driver).get_by_loc('GuestPage', 'guest_name_text')
        self.guest_name_edt_loc = Common(driver).get_by_loc('GuestPage', 'guest_name_edt')
        self.guest_sex_text_loc = Common(driver).get_by_loc('GuestPage', 'guest_sex_text')
        self.guest_sex_man_loc = Common(driver).get_by_loc('GuestPage', 'guest_sex_man')
        self.guest_sex_woman_loc = Common(driver).get_by_loc('GuestPage', 'guest_sex_woman')
        self.guest_phone_text_loc = Common(driver).get_by_loc('GuestPage', 'guest_phone_text')
        self.guest_phone_edt_loc = Common(driver).get_by_loc('GuestPage', 'guest_phone_edt')
        self.other_phone_text_loc = Common(driver).get_by_loc('GuestPage', 'other_phone_text')
        self.other_phone_edt_loc = Common(driver).get_by_loc('GuestPage', 'other_phone_edt')
        self.guest_level_text_loc = Common(driver).get_by_loc('GuestPage', 'guest_level_text')
        self.level_A_loc = Common(driver).get_by_loc('GuestPage', 'level_A')
        self.level_B_loc = Common(driver).get_by_loc('GuestPage', 'level_B')
        self.level_C_loc = Common(driver).get_by_loc('GuestPage', 'level_C')
        self.level_D_loc = Common(driver).get_by_loc('GuestPage', 'level_D')
        self.require_type_text_loc = Common(driver).get_by_loc('GuestPage', 'require_type_text')
        self.focus_area_text_loc = Common(driver).get_by_loc('GuestPage', 'focus_area_text')
        self.focus_building_text_loc = Common(driver).get_by_loc('GuestPage', 'focus_building_text')
        self.follow_plan_text_loc = Common(driver).get_by_loc('GuestPage', 'follow_plan_text')
        self.follow_plan_time_loc = Common(driver).get_by_loc('GuestPage', 'follow_plan_time')
        self.remark_text_loc = Common(driver).get_by_loc('GuestPage', 'remark_text')
        self.remark_edt_loc = Common(driver).get_by_loc('GuestPage', 'remark_edt')
        self.save_btn_loc = Common(driver).get_by_loc('GuestPage', 'save_btn')

        # 元素操作
        self.get_title = Common(driver).getText(self.get_title)
        self.get_guest_name_text = Common(driver).getText(self.guest_name_text_loc)
        self.get_guest_sex_text = Common(driver).getText(self.guest_sex_text_loc)
        self.get_guest_phone_text = Common(driver).getText(self.guest_phone_text_loc)
        self.get_other_phone_text = Common(driver).getText(self.other_phone_edt_loc)
        self.get_guest_level_text = Common(driver).getText(self.guest_level_text_loc)
        self.get_require_type_text = Common(driver).getText(self.require_type_text_loc)
        self.get_focus_area_text = Common(driver).getText(self.focus_area_text_loc)
        self.get_focus_building_text = Common(driver).getText(self.focus_building_text_loc)
        self.get_follow_plan_text = Common(driver).getText(self.follow_plan_text_loc)
        self.get_remark_text = Common(driver).getText(self.remark_text_loc)

    # 输入客户信息，执行新增操作
    def input_data(self, *value):
        self.send_keys(self.guest_name_text_loc, *value)
        self.send_keys(self.guest_phone_text_loc, *value)


if __name__ == '__main__':
    driver = appium_desired()
    newguest = NewguestView(driver)
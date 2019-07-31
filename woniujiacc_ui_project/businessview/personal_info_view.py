# coding=utf-8

from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time

"""封装个人信息页操作基类"""
class PersonalInfoView(Common):
    def __init__(self, driver):
        self.driver = driver
        mine_tab_loc = Common(driver).get_by_loc('HomePage', 'mine_tab')
        self.click(mine_tab_loc)
        time.sleep(5)
        edit_info_loc = Common(driver).get_by_loc('MinePage', 'edit_info')
        self.click(edit_info_loc)
        time.sleep(5)

        # 元素定位
        # 个人信息页元素
        self.title_loc = Common(driver).get_by_loc('MinePage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('MinePage', 'back_btn')
        self.my_photo_loc = Common(driver).get_by_loc('MinePage', 'my_photo_text')
        self.my_photo_value_loc = Common(driver).get_by_loc('MinePage', 'my_photo_value')
        self.my_name_text_loc = Common(driver).get_by_loc('MinePage', 'my_name_text')
        self.my_name_value_loc = Common(driver).get_by_loc('MinePage', 'my_name_value')
        self.my_age_text_loc = Common(driver).get_by_loc('MinePage', 'my_age_text')
        self.my_age_value_loc = Common(driver).get_by_loc('MinePage', 'my_age_value')
        self.experience_text_loc = Common(driver).get_by_loc('MinePage', 'experience_text')
        self.experience_value_loc = Common(driver).get_by_loc('MinePage', 'experience_value')
        self.familiar_area_text_loc = Common(driver).get_by_loc('MinePage', 'familiar_area_text')
        self.familiar_area_value_loc = Common(driver).get_by_loc('MinePage', 'familiar_area_value')
        self.my_profile_text_loc = Common(driver).get_by_loc('MinePage', 'my_profile_text')
        self.my_profile_value_loc = Common(driver).get_by_loc('MinePage', 'my_profile_value')
        self.wechat_text_loc = Common(driver).get_by_loc('MinePage', 'wechat_text')
        self.wechat_value_loc = Common(driver).get_by_loc('MinePage', 'wechat_value')

        # 操作元素
        self.get_title = Common(driver).getText(self.title_loc)
        self.get_my_photo_text = Common(driver).getText(self.my_photo_loc)
        self.get_my_name_text = Common(driver).getText(self.my_name_text_loc)
        self.get_my_name_value = Common(driver).getText(self.my_name_text_loc)
        self.get_my_age_text = Common(driver).getText(self.my_age_text_loc)
        self.get_my_age_value = Common(driver).getText(self.my_age_text_loc)
        self.get_experience_text = Common(driver).getText(self.experience_text_loc)
        # self.get_experience_value
        self.get_familiar_area_text = Common(driver).getText(self.familiar_area_text_loc)
        self.get_my_profile_text = Common(driver).getText(self.my_profile_text_loc)
        self.get_wechat_text = Common(driver).getText(self.wechat_text_loc)

    # 定位我的头像页元素
    def myphoto_loc(self):
        # title_loc = Common(driver).get_by_loc('MinePage', 'update_photo_title')
        more_loc = Common(self.driver).get_by_loc('MinePage', 'update_photo_right')
        self.click(more_loc)
        time.sleep(3)
        gallery_loc = Common(self.driver).get_by_loc('MinePage', 'update_photo_gallery')
        self.click(gallery_loc)
        time.sleep(3)
        picture_loc = Common(self.driver).get_by_loc('MinePage', 'picture')
        self.click(picture_loc)
        selected_pic_loc = Common(self.driver).get_by_loc('MinePage', 'selected_pic')
        self.click_index(selected_pic_loc, 1)
        time.sleep(3)
        finish_loc = Common(self.driver).get_by_loc('MinePage', 'finish_loc')
        self.click(finish_loc)
        time.sleep(3)


    # 跳转到我的头像页操作
    def goto_update_photo(self):
        self.click(self.my_photo_value_loc)
        time.sleep(3)
        self.myphoto_loc()

    # 跳转到我的姓名页操作
    def goto_update_name(self, new_name):
        self.click(self.my_name_text_loc)
        # 我的姓名和年龄页元素
        update_edt_loc = Common(self.driver).get_by_loc('MinePage', 'update_edt')
        save_btn = Common(self.driver).get_by_loc('MinePage', 'right_btn')
        # update_remark_loc = Common(driver).get_by_loc('MinePage', 'update_remark')
        self.clear(update_edt_loc)
        self.send_keys(update_edt_loc, new_name)
        self.click(save_btn)

    # 跳转到我的年龄页操作
    def goto_update_age(self, new_age):
        self.click(self.my_age_text_loc)
        # 我的姓名和年龄页元素
        update_edt_loc = Common(self.driver).get_by_loc('MinePage', 'update_edt')
        save_btn = Common(self.driver).get_by_loc('MinePage', 'right_btn')
        # update_remark_loc = Common(driver).get_by_loc('MinePage', 'update_remark')
        self.clear(update_edt_loc)
        self.send_keys(update_edt_loc, new_age)
        self.click(save_btn)

    # 跳转到个人简介页操作
    def goto_my_profile(self, text):
        self.click(self.my_profile_text_loc)
        # 个人简介页元素
        my_profile_edt_loc = Common(self.driver).get_by_loc('MinePage', 'my_profile')
        save_btn = Common(self.driver).get_by_loc('MinePage', 'right_btn')
        self.clear(my_profile_edt_loc)
        self.send_keys(my_profile_edt_loc, text)
        self.click(save_btn)


if __name__ == '__main__':
    driver = appium_desired()
    personal = PersonalInfoView(driver)
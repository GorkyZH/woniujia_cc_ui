# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time
from common.run_method import RunMethod
from common.operation_json import OperationJson
import os

base_dir = os.path.dirname(os.path.dirname(__file__))

"""封装我的页基础类"""
class MineView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.mine_tab_loc = Common(driver).get_by_loc('HomePage', 'mine_tab')
        self.click(self.mine_tab_loc)
        time.sleep(5)

        # 获取定位
        self.user_name_loc = Common(driver).get_by_loc('MinePage', 'user_name')
        self.service_time_num_loc = Common(driver).get_by_loc('MinePage', 'service_time_num')
        self.service_people_num_loc = Common(driver).get_by_loc('MinePage', 'service_people_num')
        self.service_score_num_loc = Common(driver).get_by_loc('MinePage', 'service_score_num')

        self.service_time_text_loc = Common(driver).get_by_loc('MinePage', 'service_time_text')
        self.service_people_text_loc = Common(driver).get_by_loc('MinePage', 'service_people_text')
        self.service_score_text_loc = Common(driver).get_by_loc('MinePage', 'service_score_text')

        self.edit_info_loc = Common(driver).get_by_loc('MinePage', 'edit_info')
        self.share_card_loc = Common(driver).get_by_loc('MinePage', 'share_card')
        self.plan_text_loc = Common(driver).get_by_loc('MinePage', 'plan_text')
        self.callout_text_loc = Common(driver).get_by_loc('MinePage', 'callout_text')
        self.ownbuild_text_loc = Common(driver).get_by_loc('MinePage', 'build_text')
        self.ownbuild_value_loc = Common(driver).get_by_loc('MinePage', 'build_value')
        self.setting_text_loc = Common(driver).get_by_loc('MinePage', 'setting_text')


        # 元素操作
        self.get_user_name = Common(driver).getText(self.user_name_loc)
        self.get_service_time_num = Common(driver).getText(self.service_time_num_loc)
        self.get_service_people_num = Common(driver).getText(self.service_people_num_loc)
        self.get_service_score_num = Common(driver).getText(self.service_score_num_loc)

        self.get_service_time_text = Common(driver).getText(self.service_time_text_loc)
        self.get_service_people_text = Common(driver).getText(self.service_people_text_loc)
        self.get_service_score_text = Common(driver).getText(self.service_score_text_loc)

        self.get_edit_info_text = Common(driver).getText(self.edit_info_loc)
        self.get_share_card_text = Common(driver).getText(self.share_card_loc)
        self.get_plan_text = Common(driver).getText(self.plan_text_loc)
        self.get_callout_text = Common(driver).getText(self.callout_text_loc)
        self.get_ownbuild_text = Common(driver).getText(self.ownbuild_text_loc)
        self.get_ownbuild_value = Common(driver).getText(self.ownbuild_value_loc)
        self.get_setting_text = Common(driver).getText(self.setting_text_loc)

    # 获取个人信息
    def get_info(self):
        url = Common(self.driver).get_yaml_data('UrlData','personal_info_url')
        run = RunMethod()
        operName, experience, custCount, operScore = run.get_userinfo(url)
        return operName, experience, custCount, operScore

    # 点击编辑个人信息操作
    def goto_edit_info(self):
        logging.info("============跳转到编辑个人信息页==============")
        self.click(self.edit_info_loc)

    # 点击分享我的名片
    def click_share_card(self):
        logging.info("==============点击分享我的名片==================")
        self.click(self.share_card_loc)
        select_wechat_loc = Common(self.driver).get_by_loc('MinePage', 'select_wechat_text')
        select_bill_loc = Common(self.driver).get_by_loc('MinePage', 'select_bill_text')
        select_link_loc = Common(self.driver).get_by_loc('MinePage', 'select_link_text')
        select_copy_link_loc = Common(self.driver).get_by_loc('MinePage', 'select_copy_link_text')
        select_wechat_text = self.getText(select_wechat_loc)
        select_bill_text = self.getText(select_bill_loc)
        select_link_text = self.getText(select_link_loc)
        select_copy_link_text = self.getText(select_copy_link_loc)
        return select_wechat_text, select_bill_text, select_link_text, select_copy_link_text

    # 点击取消分享
    def click_cancel_share(self):
        logging.info("==============点击取消关闭分享弹窗==================")
        self.click(self.share_card_loc)
        cancel_text_loc = Common(self.driver).get_by_loc('MinePage', 'cancel_text')
        self.click(cancel_text_loc)

    # 点击跟进计划操作
    def goto_follow_plan(self):
        logging.info("============跳转到跟进计划页==============")
        self.click(self.plan_text_loc)

    # 点击营销外呼操作
    def goto_callout_task(self):
        logging.info("============跳转到营销外呼页==============")
        self.click(self.callout_text_loc)

    # 点击驻守楼盘操作
    def goto_own_build(self):
        logging.info("============跳转到驻守楼盘页==============")
        self.click(self.ownbuild_text_loc)

    # 点击系统设置操作
    def goto_setting(self):
        logging.info("============跳转到系统设置页==============")
        self.click(self.setting_text_loc)

if __name__ == '__main__':
    driver = appium_desired()
    mine = MineView(driver)
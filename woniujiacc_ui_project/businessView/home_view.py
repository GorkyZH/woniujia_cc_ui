# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging

#封装首页元素操作类
class HomeView(Common):
    def __init__(self):
        self.driver = appium_desired()
        # 定位元素
        self.home_tab = self.get_element_loc('HomePage', 'home_tab')
        self.home_title = self.get_element_loc('HomePage', 'home_title')
        self.follow_num = self.get_element_loc('HomePage', 'follow_num')
        self.follow_text = self.get_element_loc('HomePage', 'follow_text')
        self.reported_num = self.get_element_loc('HomePage', 'reported_num')
        self.reported_text = self.get_element_loc('HomePage', 'reported_text')
        self.vistited_num = self.get_element_loc('HomePage', 'vistited_num')
        self.visited_text = self.get_element_loc('HomePage', 'visited_text')
        self.concluded_num = self.get_element_loc('HomePage', 'concluded_num')
        self.concluded_text = self.get_element_loc('HomePage', 'concluded_text')
        self.build_text = self.get_element_loc('HomePage', 'build_text')
        self.build_click = self.get_element_loc('HomePage', 'build_click')
        self.information_text = self.get_element_loc('HomePage', 'information_text')
        self.information_click = self.get_element_loc('HomePage', 'information_click')
        self.bill_text = self.get_element_loc('HomePage', 'bill_text')
        self.bill_click = self.get_element_loc('HomePage', 'bill_click')
        self.extension_text = self.get_element_loc('HomePage', 'extension_text')
        self.extension_click = self.get_element_loc('HomePage', 'extension_click')
        self.plan_text = self.get_element_loc('HomePage', 'plan_text')
        self.plan_click = self.get_element_loc('HomePage', 'plan_click')
        self.callout_text = self.get_element_loc('HomePage', 'callout_text')
        self.callout_click = self.get_element_loc('HomePage', 'callout_click')
        self.customer_num = self.get_element_loc('HomePage', 'customer_num')
        self.customer_name = self.get_element_loc('HomePage', 'customer_name')
        self.customer_phone = self.get_element_loc('HomePage', 'customer_phone')
        self.customer_time = self.get_element_loc('HomePage', 'customer_time')
        self.rob_btn = self.get_element_loc('HomePage', 'rob_btn')

    def home_action(self):
        logging.info("============home_action==============")
        # 获取首页标题
        title = self.getText(*self.home_title)
        follow_text = self.getText(*self.follow_text)
        reported_text = self.getText(*self.reported_text)
        visited_text = self.getText(*self.visited_text)
        concluded_text = self.getText(*self.concluded_text)
        build_text = self.getText(*self.build_text)
        information_text = self.getText(*self.information_text)
        bill_text = self.getText(*self.bill_text)
        extension_text = self.getText(*self.extension_text)
        plan_text = self.getText(*self.plan_text)
        callout_text = self.getText(*self.callout_text)

    def go_to_build(self):
        logging.info("============跳转到楼盘列表页==============")
        self.click(*self.build_click)

    def go_to_information(self):
        logging.info("============跳转到资讯列表页==============")
        self.click(*self.information_click)

    def go_to_bill(self):
        logging.info("============跳转到海报页==============")
        self.click(*self.bill_click)

    def go_to_extension(self):
        logging.info("============跳转到商机页==============")
        self.click(*self.extension_click)









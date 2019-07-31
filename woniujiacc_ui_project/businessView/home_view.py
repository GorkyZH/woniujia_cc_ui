# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging
from businessview.login_view import LoginView

#封装首页元素操作类
class HomeView(Common):
    def __init__(self, driver):
        self.driver = driver
        # 定位元素
        self.home_title = Common(driver).get_by_loc('HomePage', 'home_title')
        self.follow_num = Common(driver).get_by_loc('HomePage', 'follow_num')
        self.follow_text = Common(driver).get_by_loc('HomePage', 'follow_text')
        self.reported_num = Common(driver).get_by_loc('HomePage', 'reported_num')
        self.reported_text = Common(driver).get_by_loc('HomePage', 'reported_text')
        self.visited_num = Common(driver).get_by_loc('HomePage', 'visited_num')
        self.visited_text = Common(driver).get_by_loc('HomePage', 'visited_text')
        self.concluded_num = Common(driver).get_by_loc('HomePage', 'concluded_num')
        self.concluded_text = Common(driver).get_by_loc('HomePage', 'concluded_text')
        self.build_text = Common(driver).get_by_loc('HomePage', 'build_text')
        self.build_click = Common(driver).get_by_loc('HomePage', 'build_click')
        self.information_text = Common(driver).get_by_loc('HomePage', 'information_text')
        self.information_click = Common(driver).get_by_loc('HomePage', 'information_click')
        self.bill_text = Common(driver).get_by_loc('HomePage', 'bill_text')
        self.bill_click = Common(driver).get_by_loc('HomePage', 'bill_click')
        self.extension_text = Common(driver).get_by_loc('HomePage', 'extension_text')
        self.extension_click = Common(driver).get_by_loc('HomePage', 'extension_click')
        self.plan_text = Common(driver).get_by_loc('HomePage', 'plan_text')
        self.plan_click = Common(driver).get_by_loc('HomePage', 'plan_click')
        self.callout_text = Common(driver).get_by_loc('HomePage', 'callout_text')
        self.callout_click = Common(driver).get_by_loc('HomePage', 'callout_click')
        self.customer_num = Common(driver).get_by_loc('HomePage', 'customer_num')
        self.customer_name = Common(driver).get_by_loc('HomePage', 'customer_name')
        self.customer_phone = Common(driver).get_by_loc('HomePage', 'customer_phone')
        self.customer_time = Common(driver).get_by_loc('HomePage', 'customer_time')
        self.rob_btn = Common(driver).get_by_loc('HomePage', 'rob_btn')
        self.guest_tab_click = Common(driver).get_by_loc('HomePage', 'guest_tab')
        self.guest_tab_text = Common(driver).get_by_loc('HomePage', 'guest_tab_text')
        self.message_tab_click = Common(driver).get_by_loc('HomePage', 'message_tab')
        self.message_tab_text = Common(driver).get_by_loc('HomePage', 'message_tab_text')
        self.mine_tab_click = Common(driver).get_by_loc('HomePage', 'mine_tab')
        self.mine_tab_text = Common(driver).get_by_loc('HomePage', 'mine_tab_text')

        # 获取首页文本内容
        self.get_title = Common(self.driver).getText(self.home_title)
        self.get_guest_tab_text = Common(driver).getText(self.guest_tab_text)
        self.get_message_tab_text = Common(driver).getText(self.message_tab_text)
        self.get_mine_tab_text = Common(driver).getText(self.mine_tab_text)
        self.get_follow_text = Common(self.driver).getText(self.follow_text)
        self.get_reported_text = Common(self.driver).getText(self.reported_text)
        self.get_visited_text = Common(self.driver).getText(self.visited_text)
        self.get_concluded_text = Common(self.driver).getText(self.concluded_text)
        self.get_build_text = Common(self.driver).getText(self.build_text)
        self.get_information_text = Common(self.driver).getText(self.information_text)
        self.get_bill_text = Common(self.driver).getText(self.bill_text)
        self.get_extension_text = Common(self.driver).getText(self.extension_text)
        self.get_plan_text = Common(self.driver).getText(self.plan_text)
        self.get_callout_text = Common(self.driver).getText(self.callout_text)

    # 登录
    def login(self):
        login = LoginView(self.driver)
        login.login_action("15616699600", "zh123123")

    # 首页基本操作
    # def home_action(self):
    #     logging.info("============home_action==============")
        # if login.check_login_status() == True:
        #     login.login_action("15616699600", "zh123123")
        # else:

    # 点击楼盘操作
    def goto_build(self):
        logging.info("============跳转到楼盘列表页==============")
        self.click(self.build_click)

    # 点击资讯操作
    def goto_information(self):
        logging.info("============跳转到资讯列表页==============")
        self.click(self.information_click)

    # 点击海报操作
    def goto_bill(self):
        logging.info("============跳转到海报页==============")
        self.click(self.bill_click)

    # 点击商机操作
    def goto_extension(self):
        logging.info("============跳转到商机页==============")
        self.click(self.extension_click)

    # 点击跟进计划操作
    def goto_follow_plan(self):
        logging.info("============跳转到跟进计划页==============")
        self.click(self.plan_click)

    # 点击外呼任务操作
    def goto_callout_task(self):
        logging.info("============跳转到外呼任务页==============")
        self.click(self.callout_click)

    # 点击客户tab操作
    def goto_guest(self):
        logging.info("============跳转到客户页==============")
        self.click(self.guest_tab_click)

    # 点击消息tab操作
    def goto_message(self):
        logging.info("============跳转到消息页==============")
        self.click(self.message_tab_click)

    # 点击我的tab操作
    def goto_mine(self):
        logging.info("============跳转到我的页==============")
        self.click(self.mine_tab_click)

    # 点击客户池中的抢客按钮
    def goto_robguest(self):
        logging.info("============跳转到抢客页==============")
        self.click(self.rob_btn)

if __name__ == '__main__':
    driver = appium_desired()
    home = HomeView(driver)








# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import time
from common.run_method import RunMethod

"""封装跟进计划页基础类"""
class PlanView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.click(Common(driver).get_by_loc('HomePage', 'plan_click'))
        time.sleep(3)

        # 定位元素
        self.title_loc = Common(driver).get_by_loc('PlanPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('PlanPage', 'back_btn')
        self.today_tab_loc = Common(driver).get_by_loc('PlanPage', 'tab1_title')
        self.tomorrow_tab_loc = Common(driver).get_by_loc('PlanPage', 'tab2_title')
        self.timeout_tab_loc = Common(driver).get_by_loc('PlanPage', 'tab3_title')
        self.empty_text_loc = Common(driver).get_by_loc('PlanPage', 'empty_text')
        self.item_phone_loc = Common(driver).get_by_loc('PlanPage', 'item_phone_text')
        self.item_follow_time_loc = Common(driver).get_by_loc('PlanPage', 'follow_time')

        # 操作元素
        self.get_title = Common(driver).getText(self.title_loc)
        self.get_today_tab = Common(driver).getText(self.today_tab_loc)
        self.get_tomorrow_tab = Common(driver).getText(self.tomorrow_tab_loc)
        self.get_timeout_tab = Common(driver).getText(self.timeout_tab_loc)
        # self.get_empty_text = Common(driver).getText(self.timeout_tab_loc)

    # 获取接口返回的数据 list
    def get_response_list(self, url, json_key):
        run = RunMethod()
        return run.get_response_value(url, json_key, "clientNumber")

    # 查看今日、明日、已超时tab页
    def check_tab_data(self, data):
        if len(data) == 0:
            return Common(self.driver).is_element_exist(self.empty_text_loc, 0)
        elif len(data) == 1:
            # return self.is_items_in_table(data, "only", tab)
            return self.is_items_in_table(self.get_items_text(self.item_phone_loc, "only"), data)
        else:
            # return self.is_items_in_table(data, "more", tab)
            return self.is_items_in_table(self.get_items_text(self.item_phone_loc, "more"), data)

    # 如果有跟进记录，判断list中的数据是否与数据库中查询出来的记录相同
    # def is_items_in_table(self, data, count, tab):
    #     # 获取item的跟进时间
    #     follow_time_list = Common(self.driver).get_item_follow_time(self.item_follow_time_loc, count, tab)
    #     follow_time_data = []
    #     for i in range(len(data)):
    #         # follow_time_data.append(Common(self.driver).datetime_toString(data[i]['next_follow_time']))
    #         follow_time = data[i]['next_follow_time']
    #         str_follow_time = follow_time.strftime("%Y-%m-%d %H:%M:%S")
    #         follow_time_data.append(str_follow_time)
    #     for item_data in follow_time_list:
    #         if item_data in follow_time_data:
    #             return True
    #         else:
    #             return False

    def get_list_item_name(self):
        items_phone = self.get_items_text(self.item_phone_loc, "more")
        return items_phone

    # 如果有跟进记录，判断list中的数据是否与接口返回的数据相同
    def is_items_in_table(self, list_data, response_data):
        for item_data in list_data:
            if item_data in response_data:
                return True
            else:
                return False


    # 点击切换tab页
    def click_tab(self, type_tab):
        if type_tab == 'today':
            self.click(self.today_tab_loc)
        elif type_tab == 'tomorrow':
            self.click(self.tomorrow_tab_loc)
        elif type_tab == 'timeout':
            self.click(self.timeout_tab_loc)


if __name__ == '__main__':
    driver = appium_desired()
    plan = PlanView(driver)
# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired

class CalloutView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.title_loc = Common(driver).get_by_loc('CalloutPage', 'title')
        self.back_button = Common(driver).get_by_loc('CalloutPage', 'back_btn')
        self.going_tab_loc = Common(driver).get_by_loc('CalloutPage', 'going_tab')
        self.done_tab_loc = Common(driver).get_by_loc('CalloutPage', 'done_tab')
        self.empty_text_loc = Common(driver).get_by_loc('CalloutPage', 'empty_text')
        self.item_text_loc = Common(driver).get_by_loc('CalloutPage', 'item_text')

        self.get_title = Common(driver).click(self.title_loc)
        # self.get_ing_tab = Common(driver).getText(self.ing_tab_loc)
        # self.get_finish_tab = Common(driver).getText(self.finish_tab_loc)

    # 查看进行中、已完成tab页
    def check_tab_data(self, data, tab=None):
        if len(data) == 0:
            return Common(self.driver).is_element_exist(self.empty_text_loc, 0)
        elif len(data) == 1:
            return self.is_items_in_table(data, "only", tab)
        else:
            return self.is_items_in_table(data, "more", tab)

    # 如果有外呼任务，判断list中的数据是否与数据库中查询出来的记录相同
    def is_items_in_table(self, data, count, tab):
        # 获取item的外呼任务名称
        task_name_list = Common(self.driver).get_items_text(self.item_follow_time_loc, count)
        task_name__data = []
        for i in range(len(data)):
            task_name__data.append(data[i]['mission_name'])
        for item_data in task_name_list:
            if item_data in task_name__data:
                return True
            else:
                return False

    # 点击切换tab页
    def click_tab(self, type_tab):
        if type_tab == 'ing':
            self.click(self.going_tab_loc)
        elif type_tab == 'done':
            self.click(self.done_tab_loc)

if __name__ == '__main__':
    driver = appium_desired()
    callout = CalloutView(driver)

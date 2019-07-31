# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import time
from common.run_method import RunMethod

"""封装资讯页基础类"""
class InformationView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.click(Common(driver).get_by_loc('HomePage', 'information_click'))
        time.sleep(3)

        # 定位元素
        self.title_loc = Common(driver).get_by_loc('InforPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('InforPage', 'back_btn')
        self.search_btn_loc = Common(driver).get_by_loc('InforPage', 'search_btn')
        self.info_home_tab_loc = Common(driver).get_by_loc('InforPage', 'info_home_tab')
        self.build_buy_tab_loc = Common(driver).get_by_loc('InforPage', 'build_buy_tab')
        self.local_news_tab_loc = Common(driver).get_by_loc('InforPage', 'local_news_tab')
        self.country_info_tab_loc= Common(driver).get_by_loc('InforPage', 'country_info_tab')
        self.item_title_loc = Common(driver).get_by_loc('InforPage', 'item_title')

        # 操作元素
        self.get_title = Common(driver).getText(self.title_loc)
        # self.get_info_home_tab = Common(driver).getText(self.info_home_tab_loc)
        # self.get_build_buy_tab = Common(driver).getText(self.build_buy_tab_loc)
        # self.get_local_news_tab = Common(driver).getText(self.local_news_tab_loc)
        # self.get_country_info_tab = Common(driver).getText(self.country_info_tab_loc)

    # 获取资讯列表返回的接口数据
    def get_response_list(self, url, json_key):
        run = RunMethod()
        response_list = run.get_response_value(url, json_key, "list", "title")
        return response_list

    # 获取资讯列表中的所有item值
    def get_list_item_name(self, url, json_key):
        count = len(self.get_response_list(url, json_key))
        if count > 1:
            items_name = self.get_items_text(self.item_title_loc, "more")
        elif count == 1:
            items_name = self.get_items_text(self.item_title_loc, "only")
        return items_name

    # 判断一个数组中的item值是否存在于另一个数组中
    def is_items_in_table(self, list_data, response_data):
        for item_data in list_data:
            if item_data in response_data:
                return True
            else:
                return False

    # 点击切换tab页
    def click_tab(self, type_tab):
        if type_tab == 'home':
            self.click(self.info_home_tab_loc)
        elif type_tab == 'build':
            self.click(self.build_buy_tab_loc)
        elif type_tab == 'local':
            self.click(self.local_news_tab_loc)
        elif type_tab == 'country':
            self.click(self.country_info_tab_loc)

if __name__ == '__main__':
    driver = appium_desired()
    information = InformationView(driver)
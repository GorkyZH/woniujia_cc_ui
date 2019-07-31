# coding=utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import time
from common.run_method import RunMethod

"""封装楼盘页基础类"""
class BuildView(Common):
    def __init__(self, driver):
        self.driver = driver
        self.click(Common(driver).get_by_loc('HomePage', 'build_click'))
        time.sleep(3)
        self.title_loc = Common(driver).get_by_loc('BuildPage', 'title')
        self.back_btn_loc = Common(driver).get_by_loc('BuildPage', 'back_btn')
        self.search_btn_loc = Common(driver).get_by_loc('BuildPage', 'search_btn')
        self.item_name_loc = Common(driver).get_by_loc('BuildPage', 'item_build_name')
        self.item_image_loc = Common(driver).get_by_loc('BuildPage', 'item_build_image')

        self.get_title = Common(driver).getText(self.title_loc)

    def get_response_list(self, url, json_key):
        run = RunMethod()
        return run.get_response_value(url, json_key, "list", "boroughName")

    # 获取楼盘列表的item楼盘名称
    def get_list_item_name(self):
        items_name = self.get_items_text(self.item_name_loc, "more")
        return items_name

    # 楼盘搜索
    def search_build(self, keyword):
        self.click(self.search_btn_loc)
        search_input_loc = Common(self.driver).get_by_loc('BuildPage', 'search_edt')
        self.send_keys(search_input_loc, keyword)
        time.sleep(3)
        res_empty = self.is_element_exist(Common(self.driver).get_by_loc('BuildPage', 'result_empty'), 0)
        res_data = self.is_element_exist(Common(self.driver).get_by_loc('BuildPage', 'result_name'), 1)
        # 如果搜索结果为空，返回缺省提示信息
        if res_empty is True:
            return self.getText(Common(self.driver).get_by_loc('BuildPage', 'result_empty'))
        # 如果搜索结果不为空，返回list中的楼盘名称
        elif res_data is True:
            return self.get_items_text(Common(self.driver).get_by_loc('BuildPage', 'result_name'), "more")

    # 判断list中的楼盘名称是否存在于接口返回的数据中
    def is_items_in_table(self, list_data, response_data):
        for item_data in list_data:
            if item_data in response_data:
                return True
            else:
                return False

    # 操作点击listview中的item跳转至楼盘详情页
    def go_to_build_detail(self):
        self.click_index(self.item_image_loc, 0)
        time.sleep(5)

if __name__ == '__main__':
    driver = appium_desired()
    build = BuildView(driver)
    build.get_list_item_name()


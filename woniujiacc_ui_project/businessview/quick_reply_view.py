# coding=utf-8
from common.common_fun import Common
import time
from common.run_method import RunMethod
import random

"""封装常用语页基础类"""
class QuickReplyView(Common):
    def __init__(self, driver):
        self.driver = driver
        # 进入常用语设置页
        self.click(Common(driver).get_by_loc('HomePage', 'mine_tab'))
        time.sleep(3)
        self.click(Common(driver).get_by_loc('MinePage', 'setting_text'))
        time.sleep(3)
        self.click(Common(driver).get_by_loc('MinePage', 'phrase_setting_text'))
        time.sleep(3)

        # 定位元素
        self.back_btn_loc = Common(driver).get_by_loc('MinePage', 'back_btn')
        self.title_loc = Common(driver).get_by_loc('MinePage', 'title')
        self.right_btn_loc = Common(driver).get_by_loc('MinePage', 'right_btn')
        self.phrase_item_loc = Common(driver).get_by_loc('MinePage', 'phrase_item_txt')
        self.new_phrase_btn_loc = Common(driver).get_by_loc('MinePage', 'new_phrase_btn')

        # 操作元素
        self.get_title = Common(driver).getText(self.title_loc)

    # 获取接口返回的常用语
    def get_response_list(self, url, json_key):
        run = RunMethod()
        response_list = run.get_response_value(url, json_key, "data", "replyContent")
        return response_list

    # 获取常用语列表中的所有item值
    def get_list_item_name(self, url, json_key):
        count = len(self.get_response_list(url, json_key))
        if count > 1:
            items_name = self.get_items_text(self.phrase_item_loc, "more")
        elif count == 1:
            items_name = self.get_items_text(self.phrase_item_loc, "only")
        return items_name

    # 判断一个数组中的item值是否存在于另一个数组中
    def is_items_in_table(self, list_data, response_data):
        for item_data in list_data:
            if item_data in response_data:
                return True
            else:
                return False

    # 点击新增常用语，新增一条常用语保存
    def save_one_phrase(self, url, json_key):
        Common(self.driver).click(self.new_phrase_btn_loc)
        phrase_input_loc = Common(self.driver).get_by_loc('MinePage', 'new_phrase_edt')
        input_text = Common(self.driver).get_yaml_data('TextData', 'new_pharse_data')['input_text']
        Common(self.driver).send_keys(phrase_input_loc, input_text + str(random.randint(1, 100)))
        Common(self.driver).click(self.right_btn_loc)
        if input_text in self.get_list_item_name(url, json_key):
            return True
        else:
            return False

    # 输入空常用语，点击保存
    def input_null_save(self):
        Common(self.driver).click(self.new_phrase_btn_loc)
        phrase_input_loc = Common(self.driver).get_by_loc('MinePage', 'new_phrase_edt')
        Common(self.driver).click(self.right_btn_loc)




# coding = utf-8
from common.common_fun import Common
from common.desired_cap import appium_desired
import logging, time


class SearchguestView(Common):
    def __init__(self, driver):
        self.driver = driver

        # 元素定位
        self.search_edt_loc = Common(driver).get_by_loc('GuestPage', 'search_edt')  # 定位搜索输入框
        self.search_cancel_loc = Common(driver).get_by_loc('GuestPage', 'search_cancel')  # 定位取消按钮
        self.search_clear_loc = Common(driver).get_by_loc('GuestPage', 'search_clear')   # 定位清除图标

        # 操作元素
        self.get_search_cancel = Common(driver).getText(self.search_cancel_loc)  # 获取取消文本内容

    # 输入搜索内容，进行搜索操作
    def input_search_keyword(self, keyword):
        logging.info("=============输入关键词搜索=============")
        self.send_keys(self.search_edt_loc, keyword)
        self.enableAppiumUnicodeIME()
        time.sleep(3)
        self.driver.keyevent(66)
        time.sleep(3)
        self.click(self.search_clear_loc)
        time.sleep(3)
        result_text_loc = Common(self.driver).get_by_loc('GuestPage', 'result_text')  # 定位最近文本
        get_result_text = Common(self.driver).getText(result_text_loc)
        return get_result_text


if __name__ == '__main__':
    driver = appium_desired()
    search_guest = SearchguestView(driver)
# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
import logging, os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from common.operation_json import OperationJson
base_dir = os.path.dirname(os.path.dirname(__file__))

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    # def find_element(self, *loc):
    #     element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*loc))
    #     return element

    # 判断元素是否存在
    def is_element_exist(self, loc, type):
        try:
            if type == 0:
                self.find_element_by_uiautomator(loc)
            if type == 1:
                self.find_elements_by_uiautomator(loc)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # 封装一个send_Keys
    # def send_keys(self, *loc, text):
    #     self.find_element(*loc).send_keys(text)

    # 封装一个click
    # def click(self, *loc):
    #     self.find_element(*loc).click()

    # # 封装toast
    # def toast_element(self, message):
    #     toast_element = WebDriverWait(self.driver, 5).until(lambda x:x.find_element_by_xpath(message))
    #     return toast_element.text

    # 封装文本
    # def getText(self, *loc):
    #     return self.find_element(*loc).text

    # def find_element(self, *loc):
        # logging.info("------------------check element--------------------")
        # try:
        #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(*loc))
        #     return self.driver.find_element(*loc)
        # except NoSuchElementException:
        #     logging.info(loc, "is not found!")
        #     print("%s 页面中未能找到 %s 元素" % (self, loc))
        # self.driver.find_element_by_android_uiautomato("text("+"\"+*loc+"\"+")")
        # return self.driver.find_element(*loc)

    def find_element_by_uiautomator(self, by_loc):
        logging.info("------------------check element--------------------")
        return self.driver.find_element_by_android_uiautomator(by_loc)
        # try:
        #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.driver.find_element_by_android_uiautomator(by_loc)))
        #     return self.driver.find_element_by_android_uiautomator(by_loc)
        # except NoSuchElementException:
        #     logging.info(by_loc, "is not found!")
        #     print("%s 页面中未能找到 %s 元素" %(self, by_loc))

    def getText(self, loc):
        return self.find_element_by_uiautomator(loc).text

    def click(self, loc):
        self.find_element_by_uiautomator(loc).click()

    def click_index(self, loc, index):
        self.find_elements_by_uiautomator(loc)[index].click()

    def clear(self, loc):
        self.find_element_by_uiautomator(loc).clear()

    def send_keys(self, loc, text):
        self.clear(loc)
        self.find_element_by_uiautomator(loc).send_keys(text)
        # if type == 'text':
        #     loc_text = 'new UiSelector().text("'+loc+'")'
        #     return self.driver.find_element_by_android_uiautomator(loc_text)
        # elif type == 'id':
        #     loc_id = 'new UiSelector().resourceId("+'+loc+'")'
        #     return self.driver.find_element_by_android_uiautomator(loc_id)
        # elif type == 'className':
        #     loc_class = 'new UiSelector().className("'+loc+'")'
        #     return self.driver.find_element_by_android_uiautomator(loc_class)
        # elif type == 'description':
        #     loc_description = 'new UiSelector().description("'+loc+'")'
        #     return self.driver.find_element_by_android_uiautomator(loc_description)
        # else:
        #     raise Exception("type is illegal, type: " + type)
        # elif type == 'id_text':
        #     loc_id_text = 'resourceId("'++'").text("小说")'

    def find_elements_by_uiautomator(self, loc):
        logging.info("------------------check element--------------------")
        return self.driver.find_elements_by_android_uiautomator(loc)
        # try:
        #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(by_loc))
        #
        # except NoSuchElementException:
        #     logging.info(by_loc, "is not found!")
        #     print("%s 页面中未能找到 %s 元素" %(self, by_loc))

    # 获取listview中的所有item文本内容
    def get_items_text(self, item_loc, count):
        items_text = []
        if count == "only":
            element = self.find_element_by_uiautomator(item_loc)
            item_text = element.text
            items_text.append(item_text)
        elif count == "more":
            elements = self.find_elements_by_uiautomator(item_loc)
            for element in elements:
                item_text = element.text
                items_text.append(item_text)
        return items_text

    # 获取header
    def get_header(self, type=None):
        if type == 'login':
            header = OperationJson(base_dir + "/config/request.json").get_data("header")
        else:
            header = OperationJson(base_dir + "/config/request.json").get_data("token_header")
        return header

    # 截取跟进计划中item的跟进时间数组
    def get_item_follow_time(self, item_loc, count, tab):
        items_time = []
        if count == "only":
            element = self.find_element_by_uiautomator(item_loc)
            item_text = element.text
            if tab == "tomorrow":
                items_time.append(item_text[5: -3])
            else:
                items_time.append(item_text[3: -3])
        elif count == "more":
            elements = self.find_elements_by_uiautomator(item_loc)
            for element in elements:
                item_text = element.text
                if tab == "tomorrow":
                    items_time.append(item_text[5: -3])
                else:
                    items_time.append(item_text[3 : -3])
        return items_time

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 切换appium输入法为当前输入法
    def enableAppiumUnicodeIME(self):
        command = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
        os.system(command)

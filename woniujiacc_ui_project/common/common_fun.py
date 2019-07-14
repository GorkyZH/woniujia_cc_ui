from baseView.baseView import BaseView
from common.desired_cap import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time, os
import csv
import yaml

class Common(BaseView):
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

    def swipe_left(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    # 获取当前时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 截取图片
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module, time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    # 读取csv文件
    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 读取yaml文件
    def parse_yaml(self, package):
        # 获取当前脚本路径
        base_dir = os.path.dirname(os.path.dirname(__file__))
        # 获取yaml文件当前所在目录
        # yaml_dir = os.path.join(base_dir, "page", "page_element")
        yaml_dir = os.path.join(base_dir, package)
        pageElements = {}
        print("yaml_dir:", yaml_dir)
        # 遍历读取yaml文件
        for fpath, dirname, fnames in os.walk(yaml_dir):
            print("fpath:", fpath)
            print("dirname:", dirname)
            print("fnames:", fnames)
            for name in fnames:
                # yaml文件绝对路径
                yaml_file_path = os.path.join(fpath, name)
                print(yaml_file_path)

                # 排除一些非.yaml的文件
                if ".yaml" in str(yaml_file_path):
                    with open(yaml_file_path, 'r', encoding='utf-8') as f:
                         page = yaml.load(f)
                         print(page)
                         pageElements.update(page)
        return pageElements

    # 获取yaml文件中的数据
    def get_yaml_data(self, model, case):
        yaml_data = self.parse_yaml('data')
        return yaml_data[model]['data'][case]

    # 获取页面元素定位
    def get_element_loc(self, page, key):
        yaml_data = self.parse_yaml('page')
        second_value = yaml_data[page]['locators'][key]['loc']
        type = yaml_data[page]['locators'][key]['type']
        if type == 'id':
            first_value = By.ID
        elif type == 'name':
            first_value = By.NAME
        elif type == 'xpath':
            first_value = By.XPATH
        elif type == 'css_selector':
            first_value = By.CSS_SELECTOR
        else:
            raise Exception("type is illegal, type: " + type)
            # print((By.ID, i['loc']))
            # loc = (By.ID, i['loc'])[index]
            #print("loc:", i['loc'])
        return first_value, second_value

if __name__ == '__main__':
    # list = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list):
    #     print(index, item)
    driver = appium_desired()
    common = Common(driver)
    a = common.get_yaml_data('LoginData', 'operid_pwd_null')
    print("第一条数据：", a['message'])
    # print(a['LoginPage']['locators'][0]['name'])
    # for i in a['LoginPage']['locators']:
    #     # print(a['LoginPage']['locators'][i]['name'])
    #     # print(i)
    #     print(i['name'])
    #     print(i['loc'])
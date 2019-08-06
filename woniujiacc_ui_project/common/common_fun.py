# coding=utf-8
from baseview.baseView import BaseView
from common.desired_cap import appium_desired
import logging
from selenium.webdriver.common.by import By
import time, os, datetime
import csv
import yaml
from selenium.webdriver.support.ui import WebDriverWait
base_dir = os.path.dirname(os.path.dirname(__file__))

class Common(BaseView):

    # 判断是否存在toast消息提示
    def is_toast_exist(self, model, toast_message):
        try:
            message = '//*[@text=\'{}\']'.format(toast_message)
            WebDriverWait(self.driver, 10, 0.1).until(lambda x: x.find_element_by_xpath(message))
            # self.getScreenShot(model)
            logging.info("toast_message equal!")
            return True
        except:
            logging.info("toast_message not exist!")
            # self.getScreenShot(model)
            return False

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

    # 截取图片并保存到响应模块目录下
    def getScreenShot(self, module):
        time = self.getTime()
        file_dir = base_dir + "/screenshots/" + module
        if os.path.exists(file_dir):
            image_file = file_dir+'/%s.png' % time
        else:
            os.makedirs(file_dir)
            image_file = file_dir + '/%s.png' % time
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
        # print("yaml_dir:", yaml_dir)
        # 遍历读取yaml文件
        for fpath, dirname, fnames in os.walk(yaml_dir):
            # print("fpath:", fpath)
            # print("dirname:", dirname)
            # print("fnames:", fnames)
            for name in fnames:
                # yaml文件绝对路径
                yaml_file_path = os.path.join(fpath, name)
                # print(yaml_file_path)
                # 排除一些非.yaml的文件
                if ".yaml" in str(yaml_file_path):
                    with open(yaml_file_path, 'r', encoding='utf-8') as f:
                         page = yaml.load(f)
                         # print(page)
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
        # third_value = yaml_data[page]['locators'][key]['text']
        type = yaml_data[page]['locators'][key]['type']
        if type == 'id':
            first_value = By.ID
        elif type == 'name':
            first_value = By.NAME
        elif type == 'xpath':
            first_value = By.XPATH
        elif type == 'css_selector':
            first_value = By.CSS_SELECTOR
        elif type == 'classname':
            first_value = By.CLASS_NAME
        else:
            raise Exception("type is illegal, type: " + type)
            # print((By.ID, i['loc']))
            # loc = (By.ID, i['loc'])[index]
            #print("loc:", i['loc'])
        return first_value, second_value

    """ 获取页面元素定位最新方法"""
    def get_by_loc(self, page, key):
        yaml_data = self.parse_yaml('page')
        loc = yaml_data[page]['locators'][key]['loc']
        # third_value = yaml_data[page]['locators'][key]['text']
        type = yaml_data[page]['locators'][key]['type']
        if type == 'text':
            by_loc = 'new UiSelector().text("'+loc+'")'
        elif type == 'id':
            by_loc = 'new UiSelector().resourceId("'+loc+'")'
        elif type == 'className':
            by_loc = 'new UiSelector().className("'+loc+'")'
        elif type == 'description':
            by_loc = 'new UiSelector().description("'+loc+'")'
        elif type == 'brother_text':
            by_loc = 'className("android.widget.TextView").fromParent(text("'+loc+'"))'
        elif type == 'brother_image':
            by_loc = 'className("android.widget.ImageView").fromParent(text("'+loc+'"))'
        else:
            raise Exception("type is illegal, type: " +type)
        return by_loc

    # 1.把datetime转成字符串
    def datetime_toString(dt):
        strftime = dt.strftime("%Y-%m-%d %H:%M:%S")
        return strftime
        print("1.把datetime转成字符串: ", dt.strftime("%Y-%m-%d %H:%M:%S"))

    # 2.把字符串转成datetime
    def string_toDatetime(st):
        return datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
        print("2.把字符串转成datetime: ", datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S"))

    """ 获取当前时间 """
    def get_datetime_now(self):
        #return datetime.datetime.now()
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_date_now(self):
        return datetime.date.now().strf

    """ 获取年、月、日 """
    def get_y_m_d(self, type):
        if type == 'day':
            return datetime.datetime.now().day   # 获取当前时间中的'天'
        elif type == 'month':
            return datetime.datetime.now().month  # 获取当前时间中的'月'
        elif type == 'year':
            return datetime.datetime.now().year  # 获取当前时间中的'年'

    """ 获取明日0点24点时间段"""
    def get_during_time(self):
        year = str(self.get_y_m_d('year'))
        month = str(self.get_y_m_d('month'))
        day = self.get_y_m_d('day')
        t_day = str(day+1)
        start_time = "00:00:00"
        end_time = "23:59:59"

        if len(month) == 1:
            today_end_time = year + "-0" + month + "-" + str(day) + " " + end_time
            tomorrow_start_time = year + "-0" + month + "-" + t_day + " " + start_time
            tomorrow_end_time = year + "-0" + month + "-" + t_day + " " + end_time
        elif len(month) == 2:
            today_end_time = year + "-" + month + "-" + str(day) + " " + end_time
            tomorrow_start_time = year + "-" + month + "-" + t_day + " " + start_time
            tomorrow_end_time = year + "-" + month + "-" + t_day + " " + end_time
        return tomorrow_start_time, tomorrow_end_time, today_end_time


    def get_day_of_day(UTC=False, days=0, hours=0, miutes=0, seconds=0):
        '''''
        if days>=0,date is larger than today
        if days<0,date is less than today
        date format = "YYYY-MM-DD"
        '''
        now = time.time()
        timeNew = now + days * 24 * 60 * 60 + hours * 60 * 60 + miutes * 60 + seconds
        if UTC:
            timeNew = timeNew + time.timezone
        t = time.localtime(timeNew)
        return time.strftime('%Y-%m-%d %H:%M:%S', t)


if __name__ == '__main__':
    driver = appium_desired()
    common = Common(driver)
    # now_time = common.get_datetime_now()
    print("当前年：", common.get_y_m_d('year'))
    print("当前月：", common.get_y_m_d('month'))
    print("当前日：", common.get_y_m_d('day'))

    print("明日开始时间：", common.get_during_time()[0])
    print("明日结束时间：", common.get_during_time()[1])
    print("今日结束时间：", common.get_during_time()[2])

    # print("天：", common.get_string(common.get_datetime_now()))
    #print("时间差：", common.get_day_of_day(False,3))

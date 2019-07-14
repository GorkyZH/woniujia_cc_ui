from selenium.webdriver.support.ui import WebDriverWait

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    # def find_element(self, *loc):
    #     element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*loc))
    #     return element

    # 判断元素是否存在
    def is_exist(self, *loc):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(*loc))
            return True
        except:
            return False

    # 封装一个send_Keys
    def send_keys(self, *loc, text):
        self.driver.find_element(*loc).send_keys(text)

    # 封装一个click
    def click(self, *loc):
        self.find_element(*loc).click()

    # 封装文本
    def getText(self, *loc):
        return self.find_element(*loc).text

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

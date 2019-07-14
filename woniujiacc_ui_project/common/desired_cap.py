# coding=utf-8

from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    # desired_caps['udid'] = data['udid']

    # 获取根目录
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # 获取app的文件路径
    app_dir = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_dir
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    # desired_caps['automationName'] = data['automationName']

    logging.info("start app......")
    driver = webdriver.Remote(str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver

if __name__ == '__main__':
    appium_desired()
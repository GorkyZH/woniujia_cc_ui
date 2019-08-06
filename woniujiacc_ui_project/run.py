#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from BSTestRunner import BSTestRunner
import unittest
import time
import logging
import os
import importlib, sys
# path = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_ui/appium_git/woniujiacc_ui_project"
# sys.path.append(path)
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')
base_dir = os.path.dirname(os.path.dirname(__file__))


# def new_report(report_dir):
#     lists = os.listdir(report_dir)
#     print(lists)
#     lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
#     print("The latest report is:" + lists[-1])
#
#     file_new = os.path.join(report_dir, lists[-1])
#     print(file_new)
#     return file_new

# 指定测试用例和测试报告的路径
# test_dir = '../test_case/test_login'
test_dir = base_dir + '/test_case'
report_dir =  base_dir + '/reports'
# test_dir = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_ui/appium_git/woniujiacc_ui_project/test_case/"
# report_dir = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_ui/appium_git/woniujiacc_ui_project/reports"

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='login_case.py')

# 定义报告的文件格式
now = time.strftime("%Y%m%d%H%M%S")
report_name = report_dir + '/' + now + 'test_report.html'

# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="蜗牛家ccApp UI自动化测试", description="蜗牛家ccApp UI自动化测试报告")
    logging.info("start run testcase...")
    runner.run(discover)

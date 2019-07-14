# coding=utf-8
from businessView.login_view import LoginView
from common.myunit import StartEnd
from common.common_fun import Common
import unittest
import logging

class LoginCase(StartEnd):
    # 获取登录测试文件存储地址
    #login_file = '../../data/login_data.yaml'

    def test_01_allnull(self):
        logging.info("-----用例1：用户名或密码为空------")
        login = LoginView()
        data = login.get_yaml_data('LoginData', 'operid_pwd_null')
        login.login_action(data['oper_id'], data['pwd'])

    def test_02_pwd_null(self):
        logging.info("-----用例2：密码为空------")
        login = LoginView()
        data = login.get_yaml_data('LoginData', 'pwd_null')
        login.login_action(data['oper_id'], data['pwd'])


    def test_03_operid_null(self):
        logging.info("-----用例3：账号为空------")
        login = LoginView()
        data = login.get_yaml_data('LoginData', 'operid_null')
        login.login_action(data['oper_id'], data['pwd'])

    def test_04_pwd_error(self):
        logging.info("-----用例4：密码错误------")
        login = LoginView()
        data = login.get_yaml_data('LoginData', 'pwd_error')
        login.login_action(data['oper_id'], data['pwd'])

    def test_05_success(self):
        logging.info("-----用例4：登录成功------")
        login = LoginView()
        data = login.get_yaml_data('LoginData', 'success')
        login.login_action(data['oper_id'], data['pwd'])


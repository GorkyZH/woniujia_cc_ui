# coding=utf-8
from common.myunit import StartEnd
from businessview.login_view import LoginView

import unittest
import logging

class LoginCase(StartEnd):
    """登录测试用例"""

    # @unittest.skip("test_login_001_allnull")
    def test_login_001_allnull(self):
        logging.info("-----用例1：用户名或密码为空------")
        login = LoginView(self.driver)
        data = login.get_yaml_data('LoginData', 'operid_pwd_null')
        login.check_login_status()
        login.login_action(data['oper_id'], data['oper_pwd'])
        self.assertTrue(login.is_toast_exist('login', data['message']))

    # @unittest.skip("test_login_002_pwd_null")
    def test_login_002_pwd_null(self):
        logging.info("-----用例2：密码为空------")
        login = LoginView(self.driver)
        data = login.get_yaml_data('LoginData', 'pwd_null')
        login.check_login_status()
        login.login_action(data['oper_id'], data['oper_pwd'])
        self.assertTrue(login.is_toast_exist('login', data['message']))

    # @unittest.skip("test_login_003_operid_null")
    def test_login_003_operid_null(self):
        logging.info("-----用例3：账号为空------")
        login = LoginView(self.driver)
        data = login.get_yaml_data('LoginData', 'operid_null')
        login.check_login_status()
        login.login_action(data['oper_id'], data['oper_pwd'])
        self.assertTrue(login.is_toast_exist('login', data['message']))

    # @unittest.skip("test_login_004_pwd_error")
    def test_login_004_pwd_error(self):
        logging.info("-----用例4：密码错误------")
        login = LoginView(self.driver)
        data = login.get_yaml_data('LoginData', 'pwd_error')
        login.check_login_status()
        login.login_action(data['oper_id'], data['oper_pwd'])
        self.assertTrue(login.is_toast_exist('login', data['message']))

    # @unittest.skip("test_login_005_success")
    def test_login_005_success(self):
        """用例5：输入正确"""
        logging.info("-----用例5：登录成功------")
        login = LoginView(self.driver)
        data = login.get_yaml_data('LoginData', 'success')
        login.check_login_status()
        login.login_action(data['oper_id'], data['oper_pwd'])
        self.assertFalse(login.is_toast_exist('login', data['message']), msg="登录成功")

if __name__ == '__main__':
    unittest.main()

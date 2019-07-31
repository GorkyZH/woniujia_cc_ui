# coding=utf-8
from common.myunit import StartEnd
from businessview.plan_view import PlanView
from common.mysql_conn import connection, get_userid
import unittest

class PlanCase(StartEnd):
    """跟进计划用例集合"""

    @unittest.skip('test_plan_001_correct_text')
    def test_plan_001_correct_text(self):
        """用例1：检测页面的标题是否正确"""
        plan = PlanView(self.driver)
        self.assertEqual(plan.get_title, plan.get_yaml_data('TextData', 'plan_data')['title'])
        plan.getScreenShot("plan")
        # self.assertEqual(plan.get_today_tab, plan.get_yaml_data('TextData', 'plan_data')['today'])
        # self.assertEqual(plan.get_tomorrow_tab, plan.get_yaml_data('TextData', 'plan_data')['tomorrow'])
        # self.assertEqual(plan.get_timeout_tab, plan.get_yaml_data('TextData', 'plan_data')['timeout'])

    # @unittest.skip('test_plan_002_today_data')
    def test_plan_002_today_data(self):
        """用例2： 检查今日tab页，判断若无记录显示缺省信息；若有记录，数据准确"""
        plan = PlanView(self.driver)
        plan.click_tab("today")
        url = plan.get_yaml_data('UrlData', 'follow_plan_url')
        json_key = "today_plan_list"
        data = plan.get_response_list(url, json_key)
        self.assertTrue(plan.check_tab_data(data))
        plan.getScreenShot("plan")

    # @unittest.skip('test_plan_003_tomorrow_data')
    def test_plan_003_tomorrow_data(self):
        """用例3：检查明日tab页，判断若无记录显示缺省信息；若有记录，数据准确"""
        plan = PlanView(self.driver)
        plan.click_tab("tomorrow")
        url = plan.get_yaml_data('UrlData', 'follow_plan_url')
        json_key = "tomorrow_plan_list"
        data = plan.get_response_list(url, json_key)
        self.assertTrue(plan.check_tab_data(data))
        plan.getScreenShot("plan")

    # @unittest.skip('test_plan_004_timeout_data')
    def test_plan_004_timeout_data(self):
        """用例4：检查已超时tab页,判断若无记录显示缺省信息；若有记录，数据准确"""
        plan = PlanView(self.driver)
        plan.click_tab("timeout")
        url = plan.get_yaml_data('UrlData', 'follow_plan_url')
        json_key = "timeout_plan_list"
        data = plan.get_response_list(url, json_key)
        self.assertTrue(plan.check_tab_data(data))
        plan.getScreenShot("plan")

if __name__ == '__main__':
    unittest.main()
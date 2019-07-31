# coding=utf-8
from common.myunit import StartEnd
from businessview.callout_view import CalloutView
import unittest
from common.mysql_conn import get_userid, connection

class CalloutCase(StartEnd):
    """外呼任务页面用例集合"""

    def test_callout_001_correct_text(self):
        """用例1：检测营销外呼页面标题是否正确"""
        callout = CalloutView(self.driver)
        self.assertEqual(callout.get_title, callout.get_yaml_data('TextData', 'callout_data')['title'])
        # self.assertEqual(callout.get_ing_tab, callout.get_yaml_data('TextData', 'callout_data')['going'])
        # self.assertEqual(callout.get_finish_tab, callout.get_yaml_data('TextData', 'callout_data')['done'])

    # @unittest.skip('test_plan_002_today_data')
    def test_callout_002_ing_data(self):
        """用例2： 检查进行中tab页，判断若无记录显示缺省信息；若有记录，数据准确"""
        callout = CalloutView(self.driver)
        callout.click_tab("done")
        oper_id = get_userid(self.driver)
        mission_member_data = connection("effect", callout.get_yaml_data('SqlData', 'callout_data')['mission_member_sql'] % oper_id)
        mission_id = mission_member_data[0]['mission_id']
        mission_data = connection("effect20190628", callout.get_yaml_data('SqlData', 'callout_data')['mission_sql'] % (mission_id, '1'))
        self.assertTrue(callout.check_tab_data(mission_data))

    # @unittest.skip('test_plan_003_tomorrow_data')
    def test_plan_003_tomorrow_data(self):
        """用例3：检查已完成tab页，判断若无记录显示缺省信息；若有记录，数据准确"""
        callout = CalloutView(self.driver)
        callout.click_tab("ing")
        oper_id = get_userid(self.driver)
        mission_member_data = connection("effect", callout.get_yaml_data('SqlData', 'callout_data')[
            'mission_member_sql'] % oper_id)
        # mission_id = mission_member_data[0]['mission_id']
        data = []
        for i in len(mission_member_data):
            mission_id = mission_member_data[i]['mission_id']
            mission_data = connection("effect20190628",
                                  callout.get_yaml_data('SqlData', 'callout_data')['mission_sql'] % (mission_id, '2'))
            data.append(mission_data)
        self.assertTrue(callout.check_tab_data(data))

if __name__ == '__main__':
    unittest.main()

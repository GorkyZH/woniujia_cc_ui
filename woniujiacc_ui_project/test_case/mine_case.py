# coding=utf-8
from common.myunit import StartEnd
from businessview.mine_view import MineView
from businessview.plan_view import PlanView
from businessview.callout_view import CalloutView
from businessview.ownbuilding_view import OwnbuildingView
from businessview.setting_view import SettingView
from businessview.personal_info_view import PersonalInfoView
from common.mysql_conn import connection
import unittest

class MineCase(StartEnd):
    """我的页面测试用例"""
    @unittest.skip("test_mine_001_correct_text")
    def test_mine_001_correct_text(self):
        """用例1：校验我的页面文本内容是否正确"""
        mine = MineView(self.driver)
        self.assertEqual(mine.get_service_time_text, mine.get_yaml_data('TextData', 'mine_data')['service_time_text'])
        self.assertEqual(mine.get_service_people_text, mine.get_yaml_data('TextData', 'mine_data')['service_people_text'])
        self.assertEqual(mine.get_service_score_text, mine.get_yaml_data('TextData', 'mine_data')['service_score_text'])
        self.assertEqual(mine.get_edit_info_text, mine.get_yaml_data('TextData', 'mine_data')['edit_info_text'])
        self.assertEqual(mine.get_share_card_text, mine.get_yaml_data('TextData', 'mine_data')['share_card_text'])
        self.assertEqual(mine.get_plan_text, mine.get_yaml_data('TextData', 'mine_data')['plan_text'])
        self.assertEqual(mine.get_callout_text, mine.get_yaml_data('TextData', 'mine_data')['callout_text'])
        self.assertEqual(mine.get_ownbuild_text, mine.get_yaml_data('TextData', 'mine_data')['build_text'])
        mine.getScreenShot("mine")

    # @unittest.skip("test_mine_002_correct_data")
    def test_mine_002_correct_data(self):
        """用例2：校验我的页面置业咨询师的个人数据是否正确"""
        mine = MineView(self.driver)
        # data = connection("effect20190628", "select * from sys_operator where oper_id='15616699600'")
        operName, experience, custCount, operScore = mine.get_info()
        self.assertEqual(mine.get_user_name, operName)
        self.assertEqual(mine.get_service_time_num, experience)
        self.assertEqual(mine.get_service_people_num, custCount)
        self.assertEqual(mine.get_service_score_num, operScore)
        mine.getScreenShot("mine")
        # user_id = data[0]['id']
        # build_data = connection("effect20190628", "select * from league_consultant_borough where user_id='%s'" % user_id)
        # self.assertEqual(mine.get_ownbuild_value, len(build_data))

    @unittest.skip("test_mine_003_goto_personalinfo")
    def test_mine_003_goto_personalinfo(self):
        """用例3：检验是否可成功跳转到个人信息页"""
        mine = MineView(self.driver)
        mine.goto_edit_info()
        personal = PersonalInfoView(self.driver)
        self.assertEqual(personal.get_title, personal.get_yaml_data('TextData', 'personal_info_data')['title'])

    @unittest.skip("test_mine_004_clickk_sharecard")
    def test_mine_004_clickk_sharecard(self):
        """用例4：检查点击分享我的名片是否弹出分享选择框"""
        mine = MineView(self.driver)
        select_wechat_text, select_bill_text, select_link_text, select_copy_link_text = mine.click_share_card()
        self.assertEqual(select_wechat_text, mine.get_yaml_data('TextData', 'share_card_pop_data')['select_wechat_text'])
        self.assertEqual(select_bill_text, mine.get_yaml_data('TextData', 'share_card_pop_data')['select_bill_text'])
        self.assertEqual(select_link_text, mine.get_yaml_data('TextData', 'share_card_pop_data')['select_link_text'])
        self.assertEqual(select_copy_link_text, mine.get_yaml_data('TextData', 'share_card_pop_data')['select_copy_link_text'])

    @unittest.skip("test_mine_005_goto_plan")
    def test_mine_005_goto_plan(self):
        """用例5：检验是否可成功跳转到跟进计划页"""
        mine = MineView(self.driver)
        mine.goto_follow_plan()
        plan = PlanView(self.driver)
        self.assertEqual(plan.get_title, plan.get_yaml_data('TextData', 'plan_data')['title'])

    @unittest.skip("test_mine_006_goto_callout")
    def test_mine_006_goto_callout(self):
        """用例6：检验是否可成功跳转到营销外呼页"""
        mine = MineView(self.driver)
        mine.goto_callout_task()
        callout = CalloutView(self.driver)
        self.assertEqual(callout.get_title, callout.get_yaml_data('TextData', 'callout_data')['title'])

    @unittest.skip("test_mine_007_goto_ownbuild")
    def test_mine_007_goto_ownbuild(self):
        """用例7：检验是否可成功跳转到驻守楼盘页"""
        mine = MineView(self.driver)
        mine.goto_own_build()
        ownbuild = OwnbuildingView(self.driver)
        self.assertEqual(ownbuild.get_title, ownbuild.get_yaml_data('TextData', 'ownbuild_data')['title'])
        # data = connection("effect20190628", "select * from sys_operator where oper_id='15616699600'")
        # user_id = data[0]['id']
        # build_data = connection("effect20190628", "select * from league_consultant_borough where user_id='%s'" % user_id)
        # self.assertEqual(ownbuild.get_describe_build_text, "当前驻守了"+str(len(build_data))+"个楼盘")
        # list_text = []
        # for i in range(len(build_data)):
        #     text = build_data[i]['borough_name']
        #     list_text.append(text)
        # self.assertTrue(ownbuild.is_item_in_listview(list_text))

    @unittest.skip("test_mine_008_goto_setting")
    def test_mine_008_goto_setting(self):
        """用例8：检验是否可成功跳转到系统设置页"""
        mine = MineView(self.driver)
        mine.goto_setting()
        setting = SettingView(self.driver)
        self.assertEqual(setting.get_title, setting.get_yaml_data('TextData', 'setting_data')['title'])

if __name__ == '__main__':
    unittest.main()
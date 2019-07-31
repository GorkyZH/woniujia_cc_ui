# coding=utf-8

from common.myunit import StartEnd
from businessview.home_view import HomeView
import unittest
from businessview.build_view import BuildView
from businessview.information_view import InformationView
from businessview.bill_view import BillView
from businessview.extension_view import ExtensionView
from businessview.guest_view import GuestView
from businessview.message_view import MessageView
from businessview.mine_view import MineView
from businessview.robguest_view import RobguestView
from businessview.plan_view import PlanView
from businessview.callout_view import CalloutView

class HomeCase(StartEnd):

    """用例1：校验首页的文本内容是否正确"""
    # @unittest.skip("test_home_001_correct_text")
    def test_home_001_correct_text(self):
        home = HomeView(self.driver)
        # home.login()
        self.assertEqual(home.get_title, home.get_yaml_data('HomeData', 'home_title')['text'])
        self.assertEqual(home.get_title, home.get_yaml_data('HomeData', 'home_title')['text'])
        self.assertEqual(home.get_follow_text, home.get_yaml_data('HomeData', 'follow_text')['text'])
        self.assertEqual(home.get_reported_text, home.get_yaml_data('HomeData', 'reported_text')['text'])
        self.assertEqual(home.get_visited_text, home.get_yaml_data('HomeData', 'visited_text')['text'])
        self.assertEqual(home.get_concluded_text, home.get_yaml_data('HomeData', 'concluded_text')['text'])
        self.assertEqual(home.get_build_text, home.get_yaml_data('HomeData', 'build_text')['text'])
        self.assertEqual(home.get_information_text, home.get_yaml_data('HomeData', 'information_text')['text'])
        self.assertEqual(home.get_bill_text, home.get_yaml_data('HomeData', 'bill_text')['text'])
        self.assertEqual(home.get_extension_text, home.get_yaml_data('HomeData', 'extension_text')['text'])
        self.assertEqual(home.get_plan_text, home.get_yaml_data('HomeData', 'plan_text')['text'])
        self.assertEqual(home.get_callout_text, home.get_yaml_data('HomeData', 'callout_text')['text'])

    """用例2：检验是否可成功跳转到楼盘列表页"""
    # @unittest.skip("test_home_002_goto_build")
    def test_home_002_goto_build(self):
        home = HomeView(self.driver)
        # home.login()
        home.goto_build()
        build = BuildView(self.driver)
        self.assertEqual(build.get_title, build.get_yaml_data('TextData', 'build_data')['title'])

    """用例3：检验是否可成功跳转到资讯列表页"""
    # @unittest.skip("test_home_003_goto_information")
    def test_home_003_goto_information(self):
        home = HomeView(self.driver)
        home.goto_information()
        information = InformationView(self.driver)
        self.assertEqual(information.get_title, information.get_yaml_data('TextData', 'information_data')['title'])

    """用例4：检验是否可成功跳转到海报页"""
    # @unittest.skip("test_home_004_goto_bill")
    def test_home_004_goto_bill(self):
        home = HomeView(self.driver)
        home.goto_bill()
        bill = BillView(self.driver)
        self.assertEqual(bill.get_title, bill.get_yaml_data('TextData', 'bill_data')['title'])

    """用例5：检验是否可成功跳转到微信商机页"""
    # @unittest.skip("test_home_005_go_to_extension")
    def test_home_005_goto_extension(self):
        home = HomeView(self.driver)
        home.goto_extension()
        extension = ExtensionView(self.driver)
        self.assertEqual(extension.get_title, extension.get_yaml_data('TextData', 'extension_data')['title'])

    """用例6：检验点击客户tab是否可成功跳转到我的客户页"""
    # @unittest.skip("test_home_006_go_to_guest")
    def test_home_006_goto_guest(self):
        home = HomeView(self.driver)
        home.goto_guest()
        guest = GuestView(self.driver)
        self.assertEqual(guest.get_title, guest.get_yaml_data('TextData', 'guest_data')['title'])

    """用例7：检验点击消息tab是否可成功跳转到消息页"""
    # @unittest.skip("test_home_007_go_to_message")
    def test_home_007_go_to_message(self):
        home = HomeView(self.driver)
        home.goto_message()
        message = MessageView(self.driver)
        self.assertEqual(message.get_title, message.get_yaml_data('TextData', 'message_data')['title'])

    """用例8：检验点击我的tab是否可成功跳转到我的页"""
    # @unittest.skip("test_home_008_go_to_mine")
    def test_home_008_goto_mine(self):
        home = HomeView(self.driver)
        home.goto_mine()
        mine = MineView(self.driver)
        self.assertEqual(mine.get_edit_info_text, mine.get_yaml_data('TextData', 'mine_data')['edit_info_text'])

    """用例9：检验点击客户池的抢客按钮是否可成功跳转到抢客页"""
    # @unittest.skip("test_home_009_go_to_robguest")
    def test_home_009_goto_robguest(self):
        home = HomeView(self.driver)
        home.goto_robguest()
        robguest = RobguestView(self.driver)
        self.assertIn(robguest.get_yaml_data('TextData', 'robguest_data')['title'], robguest.get_title)

    """用例10：检验点击跟进计划是否可成功跳转到跟进计划页"""
    @unittest.skip("test_home_010_go_to_plan")
    def test_home_010_goto_plan(self):
        home = HomeView(self.driver)
        home.goto_follow_plan()
        plan = PlanView(self.driver)
        self.assertEqual(plan.get_title, plan.get_yaml_data('TextData', 'plan_data')['title'])

    """用例11：检验点击外呼任务是否可成功跳转到营销外呼页"""
    @unittest.skip("test_home_011_go_to_callout")
    def test_home_011_goto_callout_task(self):
        home = HomeView(self.driver)
        home.goto_callout_task()
        callout = CalloutView(self.driver)
        self.assertEqual(callout.get_title, callout.get_yaml_data('TextData', 'callout_data')['title'])

if __name__ == '__main__':
    unittest.main()
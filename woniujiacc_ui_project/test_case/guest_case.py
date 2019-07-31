# coding=utf-8
from common.myunit import StartEnd
from businessview.guest_view import GuestView
from businessview.robguest_view import RobguestView
from businessview.newguest_view import NewguestView
from businessview.search_guest__view import SearchguestView

import logging, time
import unittest

class GuestCase(StartEnd):

    """用例1：检验页面文本内容是否正确"""
    @unittest.skip("test_guest_001_correct_text")
    def test_guest_001_correct_text(self):
        guest = GuestView(self.driver)
        self.assertEqual(guest.get_title, guest.get_yaml_data('TextData', 'guest_data')['title'])
        self.assertEqual(guest.get_level_text, guest.get_yaml_data('TextData', 'guest_data')['level_text'])
        self.assertEqual(guest.get_state_text, guest.get_yaml_data('TextData', 'guest_data')['state_text'])
        self.assertEqual(guest.get_mark_text, guest.get_yaml_data('TextData', 'guest_data')['mark_text'])

    """用例2：检验点击抢客按钮是否成功跳转至抢客页面"""
    @unittest.skip("test_guest_002_goto_robguest")
    def test_guest_002_goto_robguest(self):
        guest = GuestView(self.driver)
        guest.goto_robguest()
        robguest = RobguestView(self.driver)
        self.assertIn(robguest.get_yaml_data('TextData', 'robguest_data')['title'], robguest.get_title)

    """用例3：检验点击新增图标是否成功跳转至新增客户页面"""
    @unittest.skip("test_guest_003_goto_newguest")
    def test_guest_003_goto_newguest(self):
        guest = GuestView(self.driver)
        guest.goto_newguest()
        newguest = NewguestView(self.driver)
        self.assertEqual(newguest.get_title, newguest.get_yaml_data('TextData', 'newguest_data')['title'])

    """用例4：检验点击客户搜索输入框是否成功跳转到搜索客户页面"""
    @unittest.skip("test_guest_004_goto_searchguest")
    def test_guest_004_goto_searchguest(self):
        guest = GuestView(self.driver)
        guest.goto_searchguest()
        search_guest = SearchguestView(self.driver)
        self.assertEqual(search_guest.get_search_cancel, search_guest.get_yaml_data('TextData', 'search_guest_data')['cancel_text'])

    """用例5：检验客户搜索页输入关键词搜索后再清除是否显示最近搜索关键词"""
    @unittest.skip("test_guest_005_search_keyword")
    def test_guest_005_search_keyword(self):
        guest = GuestView(self.driver)
        guest.goto_searchguest()
        time.sleep(3)
        search_guest = SearchguestView(self.driver)
        result_text = search_guest.input_search_keyword("蜗牛家")
        self.assertEqual(result_text, search_guest.get_yaml_data('TextData', 'search_guest_data')['result_text'])

if __name__ == '__main__':
    unittest.main()







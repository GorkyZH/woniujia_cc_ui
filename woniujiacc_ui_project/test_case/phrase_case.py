# coding=utf-8
from common.myunit import StartEnd
from businessview.quick_reply_view import QuickReplyView
from common.mysql_conn import connection, get_userid
import unittest

class PhraseCase(StartEnd):
    """常用语设置用例集合"""

    # @unittest.skip('test_phrase_001_correct_text')
    def test_phrase_001_correct_text(self):
        """用例1：获取常用语列表，检验列表数据与接口返回的数据是否相等"""
        phrase = QuickReplyView(self.driver)
        url = phrase.get_yaml_data('UrlData', 'quick_reply_url')
        json_key = "quick_reply_list"
        response_list = phrase.get_response_list(url, json_key)
        phrase_list = phrase.get_list_item_name(url, json_key)
        self.assertTrue(phrase.is_items_in_table(phrase_list, response_list))
        phrase.getScreenShot("phrase")

    # @unittest.skip('test_phrase_002_save_null')
    def test_phrase_002_save_null(self):
        """用例2：新增一条为空的常用语，提示常用语不能为空"""
        phrase = QuickReplyView(self.driver)
        phrase.input_null_save()
        self.assertTrue(phrase.is_toast_exist('phrase', phrase.get_yaml_data('TextData', 'new_pharse_data')['message']))

    # @unittest.skip('test_phrase_003_new_phrase')
    def test_phrase_003_new_phrase(self):
        """用例3：新增一条常用语，保存成功"""
        phrase = QuickReplyView(self.driver)
        url = phrase.get_yaml_data('UrlData', 'quick_reply_url')
        json_key = "quick_reply_list"
        self.assertTrue(phrase.save_one_phrase(url, json_key))
        phrase.getScreenShot("phrase")
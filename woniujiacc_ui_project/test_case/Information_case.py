# coding=utf-8

from common.myunit import StartEnd
from businessview.information_view import InformationView
import unittest

"""资讯页面用例集合"""
class InformationCase(StartEnd):

    def test_information_001_correct_text(self):
        """用例1：检验页面文本内容是否正确"""
        information = InformationView(self.driver)
        self.assertEqual(information.get_title, information.get_yaml_data('TextData', 'information_data')['title'])

    def test_information_002_info_home(self):
        """用例2：查看资讯首页列表数据与接口返回的数据是否相同"""
        information = InformationView(self.driver)
        url = information.get_yaml_data('UrlData', 'article_list_url')
        json_key = "article_list"
        response = information.get_response_list(url, json_key)
        # information.click_tab("country")
        item_list = information.get_list_item_name(url, json_key)
        self.assertTrue(information.is_items_in_table(item_list, response))

    def test_information_003_info_home(self):
        """用例3：查看楼评导购列表的数据与接口返回的数据是否相同"""
        information = InformationView(self.driver)
        url = information.get_yaml_data('UrlData', 'article_list_url')
        json_key = "article_build_tab"
        response = information.get_response_list(url, json_key)
        information.click_tab("build")
        item_list = information.get_list_item_name(url, json_key)
        self.assertTrue(information.is_items_in_table(item_list, response))

    def test_information_004_info_home(self):
        """用例4：查看本地要闻列表的数据与接口返回的数据是否相同"""
        information = InformationView(self.driver)
        url = information.get_yaml_data('UrlData', 'article_list_url')
        json_key = "article_local_tab"
        response = information.get_response_list(url, json_key)
        information.click_tab("local")
        item_list = information.get_list_item_name(url, json_key)
        self.assertTrue(information.is_items_in_table(item_list, response))

    def test_information_005_info_country(self):
        """用例5：查看全国资讯列表的数据与接口返回的数据是否相同"""
        information = InformationView(self.driver)
        url = information.get_yaml_data('UrlData', 'article_list_url')
        json_key = "article_country_tab"
        response = information.get_response_list(url, json_key)
        information.click_tab("country")
        item_list = information.get_list_item_name(url, json_key)
        self.assertTrue(information.is_items_in_table(item_list, response))

if __name__ == '__main__':
    unittest.main()
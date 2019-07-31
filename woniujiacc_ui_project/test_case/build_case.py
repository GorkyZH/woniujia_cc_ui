# coding=utf-8
from businessview.build_view import BuildView
from common.myunit import StartEnd
from common.mysql_conn import connection
from common.run_method import RunMethod
from common.operation_json import OperationJson
import unittest

class BuildCase(StartEnd):
    """楼盘页测试用例集合"""

    # @unittest.skip('test_build_001_correct_data')
    def test_build_001_correct_data(self):
        """用例1：获取楼盘列表中的item数据是否正确"""
        build = BuildView(self.driver)
        get_list_data = build.get_list_item_name()
        # data = connection("testwoniujia", "select * from ymm_borough where city_id='62' AND is_checked = '1'")
        url = build.get_yaml_data('UrlData', 'build_list_url')
        json_key = "boroughtList"
        build_name_data = build.get_response_list(url, json_key)
        self.assertTrue(build.is_items_in_table(get_list_data, build_name_data))
        build.getScreenShot("build")

    @unittest.skip('test_build_002_search_empty')
    def test_build_002_search_empty(self):
        """用例2：搜索楼盘结果为空"""
        build = BuildView(self.driver)
        result = build.search_build(build.get_yaml_data('TextData', 'build_data')['keyword_empty'])
        self.assertEqual(result, build.get_yaml_data('TextData', 'build_data')['empty_tip'])
        build.getScreenShot("build")

    @unittest.skip('test_build_003_search_exist')
    def test_build_003_search_exist(self):
        """用例3：存在包含该关键字的楼盘"""
        build = BuildView(self.driver)
        result = build.search_build(build.get_yaml_data('TextData', 'build_data')['keyword_exist'])
        # keyword = "%" +build.get_yaml_data('TextData', 'build_data')['keyword_exist'] + "%"
        # data = connection("testwoniujia", "select * from ymm_borough where city_id='62' AND is_checked = '1' AND borough_name like '%s'" % keyword)
        url = build.get_yaml_data('UrlData', 'build_search_url')
        json_key = "searchBoroughList_kewords_in"
        build_name_data = build.get_response_list(url, json_key)  # 接口返回的所有楼盘数组
        self.assertTrue(build.is_items_in_table(result, build_name_data))
        build.getScreenShot("build")

    @unittest.skip('test_build_004_goto_detail')
    def test_build_004_goto_detail(self):
        """用例4：检查点击item是否跳转到对应楼盘详情页"""
        build = BuildView(self.driver)
        build.go_to_build_detail()
        self.assertTrue(build.is_element_exist(build.get_by_loc('BuildPage', 'build_detail_share_btn'), 0))
        build.getScreenShot("build")

if __name__ == '__main__':
    unittest.main()
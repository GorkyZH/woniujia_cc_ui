from common.desired_cap import appium_desired
from businessview.personal_info_view import PersonalInfoView
from common.myunit import StartEnd
import unittest
import time

class PersonalCase(StartEnd):
    """个人信息页测试用例"""

    @unittest.skip('test_personal_001_correct_text')
    def test_personal_001_correct_text(self):
        """用例1：校验个人信息页文本内容是否正确"""
        personal = PersonalInfoView(self.driver)
        self.assertEqual(personal.get_title, personal.get_yaml_data('personal_info_data', 'title'))
        self.assertEqual(personal.get_my_photo_text, personal.get_yaml_data('personal_info_data', 'my_photo_text'))
        self.assertEqual(personal.get_my_name_text, personal.get_yaml_data('personal_info_data', 'my_name_text'))
        self.assertEqual(personal.get_my_age_text, personal.get_yaml_data('personal_info_data', 'my_age_text'))
        self.assertEqual(personal.get_experience_text, personal.get_yaml_data('personal_info_data', 'experience_text'))
        self.assertEqual(personal.get_familiar_area_text, personal.get_yaml_data('personal_info_data', 'familiar_area_text'))
        self.assertEqual(personal.get_my_profile_text, personal.get_yaml_data('personal_info_data', 'personal_profile_text'))
        self.assertEqual(personal.get_wechat_text, personal.get_yaml_data('personal_info_data', 'wechat_code_text'))

    # def test_personal_002_correct_text(self):
    #     """用例2：校验个人信息页数据是否正确"""
    #     personal = PersonalInfoView(self.driver)
    #     # self.assertEqual(personal.get)

    #@unittest.skip('test_personal_002_upload_photo')
    def test_personal_002_upload_photo(self):
        """用例2：测试上传头像是否成功"""
        personal = PersonalInfoView(self.driver)
        personal.goto_update_photo()
        self.assertTrue(personal.is_toast_exist('personal', "图片上传成功！"))

if __name__ == '__main__':
    unittest.main()
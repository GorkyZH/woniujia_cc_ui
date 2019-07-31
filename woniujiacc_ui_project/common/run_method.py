#coding:utf-8
import requests
import json
from common.operation_json import OperationJson

"""
post、get基类的封装
"""

class RunMethod:
    def __init__(self):
        self.operator = OperationJson("/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_ui/appium_git/woniujiacc_ui_project/config/request.json")

    def post_main(self,url,data,header=None):
        result = None
        if header != None:

            result = requests.post(url=url,data=data,headers=header)
        else:
            result = requests.post(url=url, data=data)
        print(result.status_code)
        return result.json()

    def get_main(self,url,data=None,header=None):
        result = None
        if header != None:
            result = requests.get(url=url,data=data,headers=header)
        else:
            result = requests.get(url=url, data=data)
        return result.json()

    def run_main(self, method, url, data=None):
        result = None
        if method == 'post':
            if url == "http://182.61.33.241:8089/app/api/public/1.0/open/login":
                result = self.post_main(url,data,self.get_header())
            else:
                result = self.post_main(url,data,self.get_token_header())
        else:
            result = self.get_main(url,data,self.get_token_header())
        # 返回数据格式调整
        # return json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return json.dumps(result, ensure_ascii=False)
        #return result

    def get_token_header(self):
        header = {
            "Authorization": "Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJvcGVySWQiOiIxNTYxNjY5OTYwMCIsInVzZXJJZCI6IjFGNDcwMjM4REFFRDQyNkNBQUFCQjJFMjFDREIxMTkzIiwicGxhdGZvcm0iOjEsImNhY2hlSWQiOjEwLCJsb2dpbnRpbWUiOjE1NjQwNDI1OTkwMzYsImV4cCI6MzEyODY4OTk5OCwibmJmIjoxNTY0MDQyNTk5fQ.fm6eqdHZwRZapd5SOEl7rcg7kA1FCp06wnnWdpLcZdI",
            "Content-Type": "application/json"
        }
        return header

    def get_header(self):
        header = {
            "Content-Type": "application/json"
        }
        return header

    # 遍历获取返回结果data的list,取出关键字段放在数组中
    def get_response_value(self, url, json_key, list_key, response_key):
        method = "post"
        data = self.operator.get_data(json_key)
        response = self.run_main(method, url, data)
        response_dict = json.loads(response)
        if list_key == "data":
            response_list = response_dict['data']
        elif list_key == "list":
            response_list = response_dict['data']['list']
        count = len(response_list)
        # count = response_dict['data']['count']
        list = []
        if count == 0:
            list = response_list
        elif count > 0 and count/15 <= 1:
            for response_index in range(count):
                response_name = response_list[response_index][response_key]
                list.append(response_name)
        elif (count/15) > 1 and (count % 15) == 0:
            for i in range(1, int(count/15)):
                self.get_list(i, list, method, url, json_key, response_key)
        elif (count/15) > 1 and (count % 15) > 0:
            for i in range(1, int(count/15)+1):
                self.get_list(i, list, method, url, json_key, response_key)
        print("list:", list)
        return list

    # 获取接口返回的数组
    def get_list(self, i, list, method, url, json_key, list_key, response_key):
        data = self.operator.get_data_for_newjson(json_key, '"' + str(i) + '"')
        new_response = self.run_main(method, url, data)
        new_response_dict = json.loads(new_response)
        if list_key == "data":
            new_response_list = new_response_dict['data']
        elif list_key == "list":
            new_response_list = new_response_dict['data']['list']
        for response_index in range(len(new_response_list)):
            response_name = new_response_list[response_index][response_key]
            list.append(response_name)

    # 获取置业咨询师信息
    def get_userinfo(self, url):
        data = self.operator.get_data('personalinfo_data')
        response = self.run_main("get", url, data)
        response_dict = json.loads(response)
        operName = response_dict['data']['operName']
        experience = response_dict['data']['exp']
        custCount = response_dict['data']['custCount']
        operScore = response_dict['data']['operScore']
        return operName, experience, custCount, operScore


if __name__ == '__main__':
    run = RunMethod()

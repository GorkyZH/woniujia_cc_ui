# coding=utf-8
import pymysql.cursors
import os, yaml
from common.common_fun import Common
from common.desired_cap import appium_desired

base_dir = os.path.dirname(os.path.dirname(__file__))

"""封装数据库连接"""
def connection(db, sql):
    desired_yaml = os.path.join(base_dir, 'config', 'db_caps.yaml')
    with open(desired_yaml, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    conn = pymysql.connect(
        host = data['host_server'],
        port = 3306,
        user = data['db_user'],
        passwd = data['db_pwd'],
        db = db,
        charset ='utf8'
        )
    # 获取一个光标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    rows = cursor.execute(sql)
    print("rows:", rows)
    # print(cursor.fetchone())
    # print(cursor.fetchmany(2))
    cursor.close()
    conn.close()
    return cursor.fetchall()

# 获取置业咨询师id
def get_userid(driver):
    # sql_data = os.path.join(base_dir, 'data', 'sql_data.yaml')
    # with open(sql_data, 'r', encoding='utf-8') as file:
    #     data = yaml.load(file)
    sql = Common(driver).get_yaml_data('SqlData', 'sys_operator_data')['id_sql']
    data = connection("effect20190628",  sql)
    return data[0]['id']



if __name__ == '__main__':
    # data = connection("effect20190628", "select * from sys_operator where oper_id='15616699600'")
    # data = connection("testwoniujia", "select * from ymm_borough where city_id='62' AND is_checked = '1'")
    # for i in range(len(data)):
    #     print("值：", data[i]['borough_name'])
    print("userid:", get_userid())

    # build_data = connection("select * from league_consultant_borough where user_id='%s'" % data[0]['id'])
    # print("查询结果", len(build_data))

# 封装数据库
# class MysqlConn(object):
#     def __init__(self):
#         base_dir = os.path.dirname(os.path.dirname(__file__))
#         desired_yaml = os.path.join(base_dir, 'config', 'db_caps.yaml')
#         with open(desired_yaml, 'r', encoding='utf-8') as file:
#             data = yaml.load(file)
#         self.host = data['host_server']
#         self.port = 3306
#         self.user = data['db_user']
#         self.passwd = data['db_pwd']
#         self.db = data['db_base']
#         self.charset ='utf8'
#         self.conn = None
#         self.cur = None
#
#     # 连接数据库
#     def mysql_conn(self):
#         try:
#             self.conn = pymysql.connect(host = self.host,
#                                    port=3306,
#                                    user = self.user,
#                                    passwd = self.passwd,
#                                    db = self.db,
#                                    charset = self.charset,
#                                    cursorclass = pymysql.cursors.DictCursor)
#             print("检查数据库连接状态", self.conn.server_status)
#         except:
#             return False
#         self.cur = self.conn.cursor()
#         return True


        # 定义要执行的sql语句
        # sql = "SELECT * FROM 'sys_operator' WHERE 'oper_id'='15616699600'"
        # response = cursor.execute(sql)



# if __name__ == '__main__':
#     mysql = MysqlConn()
#     mysql.mysql_conn()
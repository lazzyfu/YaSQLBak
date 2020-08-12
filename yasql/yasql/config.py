# -*- coding:utf-8 -*-
# edit by fuzongfei

# 配置MySQL数据库，库必须先创建，且库的字符集必须为:utf8
# 存储django程序运行的系统库表等数据
# 权限：grant all on *.* to 'xxx'@'xxxhost' with grant options
DB = {
    'database': 'yasql',
    'user': 'yasql_rw',
    'host': '127.0.0.1',
    'port': 3306,
    'password': '1234.com',
}

# 连接目标数据库的用户
# 每个连接的目标数据库都需要创建，用于goInception、工单执行、备份、查询
# create user 'yasql_user'@'%' identified by '1234.com'
# grant all on *.* to 'yasql_user'@'%';
# 用户名和密码请进行自行修改，不要使用默认的
REOMOTE_USER = {
    'username': 'yasql_user',
    'password': '1234.com'
}

# REDIS配置
# 存储session、消息队列等
REDIS = {
    'host': '127.0.0.1',
    'port': 6379
}

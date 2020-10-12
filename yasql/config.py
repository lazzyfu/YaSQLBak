# -*- coding:utf-8 -*-
# edit by fuzongfei

# 配置MySQL数据库，库必须先创建，且库的字符集必须为:utf8
# 存储django程序运行的系统库表等数据
# 权限：grant all on *.* to 'xxx'@'%' with grant options
import ldap
from django_auth_ldap.config import LDAPSearch

DB = {
    'database': 'yasql',
    'user': 'yasql_rw',
    'host': '127.0.0.1',
    'port': 3306,
    'password': '1234.com',
}

# 连接目标数据库的用户
# 每个连接的目标数据库都需要创建，用于goInception、工单执行、备份、查询
# create user 'yasql_rw'@'%' identified by '1234.com'
# grant all on *.* to 'yasql_user'@'%';
# 用户名和密码请进行自行修改，不要使用默认的
REOMOTE_USER = {
    'user': 'yasql_rw',
    'password': '1234.com'
}

# REDIS配置
# 存储session、消息队列等
REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '1234.com'
}

# 启用LDAP
# LDAP配置如下，请按照自己公司的LDAP配置进行更正
LDAP_SUPPORT = {
    'enable': False,  # 为True启用LDAP，为False禁用LDAP
    'config': {
        'AUTH_LDAP_SERVER_URI': "ldap://ldapxx.xxx.com:389",
        'AUTH_LDAP_ALWAYS_UPDATE_USER': True,
        'AUTH_LDAP_BIND_DN': "cn=admin,dc=xxx,dc=com",  # 用户，绝对路径
        'AUTH_LDAP_BIND_PASSWORD': '123.com',  # 密码
        'AUTH_LDAP_USER_SEARCH': LDAPSearch("ou=people,dc=xxx,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"),
        # 用户映射，key为系统表字段，value为ldap字段
        # 请根据自己公司的ldap配置调整value部分（username/mail/givenName/mobile）
        'AUTH_LDAP_USER_ATTR_MAP': {
            'username': 'username',
            'email': 'mail',
            'displayname': 'givenName',
            'mobile': 'mobile'
        }
    }
}

# gh-ost工具使用
GH_OST_ARGS = ['--allow-on-master',
               '--assume-rbr',
               '--initially-drop-ghost-table',
               '--initially-drop-old-table',
               '-exact-rowcount',
               '--approve-renamed-columns',
               '--concurrent-rowcount=false',
               '--chunk-size=800',
               '--hooks-path=/data/www/yasql/hook/']

# GoInception
INCEPTION = {
    'host': '127.0.0.1',
    'port': 4000
}

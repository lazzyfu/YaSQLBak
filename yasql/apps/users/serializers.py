# -*- coding:utf-8 -*-
# edit by fuzongfei
from django.contrib.auth import authenticate
from rest_framework import serializers

from users import models


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=30, min_length=3, label='用户名',
                                     error_messages={'required': '用户名不能为空',
                                                     'min_length': '用户名至少3个字符',
                                                     'max_lenght': '用户名最大长度为30个字符',
                                                     'blank': '输入用户名不能为空，至少3个字符，最多30个字符'
                                                     }
                                     )
    password = serializers.CharField(required=True, max_length=30, min_length=7, label='密码',
                                     error_messages={'required': '密码不能为空',
                                                     'min_length': '密码至少7个字符',
                                                     'max_lenght': '密码最大长度为30个字符',
                                                     'blank': '输入密码不能为空，至少7个字符，最多30个字符'
                                                     }
                                     )

    def login(self):
        username = self.validated_data.get('username')
        password = self.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return False, '用户名或密码错误'

        try:
            user = models.UserAccounts.objects.get(username=username)
        except models.UserAccounts.DoesNotExist:
            return False, '用户不存在'

        if not user.is_active:
            return False, '用户被禁用，请联系管理员'

        token = user.token
        return True, token


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccounts
        fields = ['uid', 'displayname', 'mobile', 'avatar_file', 'username', 'is_superuser', 'email']


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccounts
        fields = ['username', 'displayname', 'email']

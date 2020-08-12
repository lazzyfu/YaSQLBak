# -*- coding:utf-8 -*-
# edit by fuzongfei
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_jwt.settings import api_settings


class UserAccounts(AbstractUser):
    uid = models.BigAutoField(primary_key=True, verbose_name=u'uid')
    user_secret = models.UUIDField(default=uuid4(), verbose_name=u'用户JWT秘钥')
    is_active = models.BooleanField(default=True, verbose_name=u'是否激活')
    displayname = models.CharField(max_length=128, default='', verbose_name=u'别名')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'用户手机号')
    avatar_file = models.ImageField(upload_to='img/%Y/%m/%d/',
                                    default=u'img/avatar1.png',
                                    verbose_name=u'用户头像')

    def __str__(self):
        return self.username

    @property
    def token(self):
        # 生成token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        obj = UserAccounts.objects.get(uid=self.uid)
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        app_label = 'users'
        db_table = 'yasql_user_accounts'

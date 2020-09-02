# -*- coding:utf-8 -*-
# edit by fuzongfei
import json
import re
import uuid
from datetime import datetime

import sqlparse
from django.db.models import F
from rest_framework import serializers

from sqlorders import models, utils, libs
from sqlorders.api.goInceptionApi import InceptionApi
from users.models import UserAccounts
from yasql.config import REOMOTE_USER


class ReleaseVersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReleaseVersions
        fields = ['username', 'version', 'expire_time', 'created_at']

    def to_representation(self, instance):
        ret = super(ReleaseVersionsSerializer, self).to_representation(instance)
        ret["created_at"] = datetime.strftime(instance.created_at, "%Y-%m-%d %H:%M:%S")
        return ret


class DbEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DbEnvironment
        fields = ['id', 'name']


class DbSchemasSerializer(serializers.Serializer):
    env_id = serializers.CharField()
    rds_category = serializers.ChoiceField(choices=utils.rdsCategory)

    @property
    def query(self):
        super(DbSchemasSerializer, self)
        vdata = self.validated_data
        queryset = models.DbSchemas.objects.filter(
            cid__env_id=vdata['env_id'],
            cid__use_type=0,
            cid__is_enabled=0,
            cid__rds_category=vdata['rds_category']
        ).annotate(host=F('cid__host'),
                   port=F('cid__port'),
                   comment=F('cid__comment')
                   ).values('id', 'cid', 'host', 'port', 'schema', 'comment')
        return queryset


class IncepSyntaxCheckSerializer(serializers.Serializer):
    rds_category = serializers.ChoiceField(choices=utils.rdsCategory,
                                           error_messages={
                                               'required': '请先选择左侧的【DB类别】',
                                               'blank': '请先选择左侧的【DB类别】'
                                           })
    database = serializers.CharField(
        error_messages={
            'required': '请先选择左侧的【环境】和【库名】',
            'blank': '请先选择左侧的【环境】和【库名】'
        }
    )
    sqls = serializers.CharField(error_messages={
        'required': '审核内容不能为空',
        'blank': '审核内容不能为空'
    })
    sql_type = serializers.ChoiceField(choices=utils.sqlTypeChoice)

    def validate(self, attrs):
        # ddl工单提交ddl语句，dml工单提交dml语句
        status, msg = libs.verify_sql_type(sqls=attrs['sqls'], sql_type=attrs['sql_type'])
        if not status:
            raise serializers.ValidationError(msg)

        # TiDB的ALTER语句需要单独的处理
        if attrs['rds_category'] == 2:
            if attrs['sql_type'] == 'DDL':
                sc = re.compile(r'^ALTER([\s\S]+)([,])(\s+)(ADD|CHANGE|RENAME|MODIFY|DROP|CONVERT)([\s\S]+)', re.I)
                for sql in sqlparse.split(attrs['sqls']):
                    try:
                        m = sc.match(sql)
                        if m.groups():
                            raise serializers.ValidationError('TiDB下的同一个表的多个操作，请拆分成多个ALTER语句')
                    except AttributeError:
                        pass
        return super(IncepSyntaxCheckSerializer, self).validate(attrs)

    def check(self):
        vdata = self.validated_data
        cid, database = vdata['database'].split('__')
        obj = models.DbConfig.objects.get(pk=cid)
        cfg = {
            'host': obj.host,
            'port': obj.port,
            'database': database
        }
        cfg.update(REOMOTE_USER)
        api = InceptionApi(cfg=cfg, sqls=vdata['sqls'], rds_category=vdata['rds_category'])
        context = api.run_check()
        status = api.is_check_pass()
        return status, context


class SqlOrdersCommitSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField()

    class Meta:
        model = models.DbOrders
        exclude = ['applicant', 'auditor', 'reviewer', 'email_cc', 'cid', 'order_id']

    def convert_to_dict(self, data):
        """
        auditor = reviewer = [
            {'user': 'zhangsan', 'is_superuser': 0, 'status': 0, 'msg': '', 'time': ''},
            ...
            ]
        status:
            0：未审核或未复核
            1：已审核或已复核
            2: 已驳回
        is_superuser:
            0：不是一键审核人或复核人
            1：是一键审核人或复核人
        msg: 附加的信息
        time: 操作时间
        """
        r = []
        for i in data:
            r.append({'user': i, 'is_superuser': 0, 'status': 0, 'msg': '', 'time': ''})
        return json.dumps(r)

    def check_number(self, data):
        """单次最大支持1024条语句提交"""
        sql_list = [sql for sql in sqlparse.split(data)]
        if len(sql_list) > 1024:
            return False, len(sql_list)
        return True, None

    def validate_sql_type(self, data):
        if data in ('DDL', 'DML'):
            # 检查语句条数
            status, length = self.check_number(self.initial_data.get('contents'))
            if not status:
                raise serializers.ValidationError(f'单次最大支持一次提交1024条SQL语句，当前条数: {length}')
        return data

    def validate(self, attrs):
        # 判断提交的SQL是否符合SQL类型
        # 如：DML只能提交DML语句，DDL工单只能提交DDL语句
        status, msg = libs.verify_sql_type(sqls=attrs['contents'], sql_type=attrs['sql_type'])
        if not status:
            raise serializers.ValidationError(msg)

        # 当语法未检查通过时，拦截提交
        cid, database = attrs['database'].split('__')
        obj = models.DbConfig.objects.get(pk=cid)
        cfg = {
            'host': obj.host,
            'port': obj.port,
            'database': database
        }
        cfg.update(REOMOTE_USER)
        if not InceptionApi(cfg=cfg, sqls=attrs['contents'], rds_category=attrs['rds_category']).is_check_pass():
            raise serializers.ValidationError('SQL语法存在异常，提交失败，请先检查SQL语法，请点击：[语法检查]')

        # TiDB的ALTER语句需要单独的处理
        if attrs['rds_category'] == 2:
            if attrs['sql_type'] == 'DDL':
                sc = re.compile(r'^ALTER([\s\S]+)([,])(\s+)(ADD|CHANGE|RENAME|MODIFY|DROP|CONVERT)([\s\S]+)', re.I)
                for sql in sqlparse.split(attrs['contents']):
                    try:
                        m = sc.match(sql)
                        if m.groups():
                            raise serializers.ValidationError('TiDB下的同一个表的多个操作，请拆分成多个ALTER语句')
                    except AttributeError:
                        pass

        # 提交工单
        request = self.context['request']
        attrs["applicant"] = request.user.username
        attrs["auditor"] = self.convert_to_dict(self.initial_data.get('auditor'))
        attrs["reviewer"] = self.convert_to_dict(self.initial_data.get('reviewer'))
        attrs["executor"] = self.convert_to_dict(['None'])
        attrs["closer"] = self.convert_to_dict(['None'])
        attrs["email_cc"] = ','.join(self.initial_data.get('email_cc'))

        attrs['title'] = attrs['title'] + '_[' + datetime.now().strftime("%Y%m%d%H%M%S") + ']'
        attrs['order_id'] = ''.join(str(uuid.uuid4()).split('-'))  # 基于UUID生成工单id
        attrs['cid_id'], attrs['database'] = attrs['database'].split('__')
        attrs["department"] = request.user

        return super(SqlOrdersCommitSerializer, self).validate(attrs)


class SqlOrdersListSerializer(serializers.ModelSerializer):
    applicant = serializers.SerializerMethodField()
    auditor = serializers.SerializerMethodField()
    reviewer = serializers.SerializerMethodField()
    # 获取choices字段
    progress = serializers.SerializerMethodField()
    # 获取外键的字段
    version = serializers.ReadOnlyField(source='version.version')
    host = serializers.ReadOnlyField(source='cid.host')
    port = serializers.ReadOnlyField(source='cid.port')
    # 环境
    env_name = serializers.ReadOnlyField(source='env.name')

    class Meta:
        model = models.DbOrders
        fields = ['id', 'title', 'progress', 'remark', 'env_name', 'sql_type', 'file_format', 'department', 'is_hide',
                  'applicant', 'order_id', 'auditor', 'reviewer', 'version', 'cid', 'host', 'port', 'database',
                  'created_at']

    def get_applicant(self, obj):
        try:
            obj.applicant = UserAccounts.objects.get(username=obj.applicant).displayname
        except UserAccounts.DoesNotExist:
            pass
        return obj.applicant

    def get_auditor(self, obj):
        data = json.loads(obj.auditor)
        for row in data:
            try:
                row['display_name'] = UserAccounts.objects.get(username=row['user']).displayname
            except UserAccounts.DoesNotExist:
                pass
        return json.dumps(data)

    def get_reviewer(self, obj):
        data = json.loads(obj.reviewer)
        for row in data:
            try:
                row['display_name'] = UserAccounts.objects.get(username=row['user']).displayname
            except UserAccounts.DoesNotExist:
                pass
        return json.dumps(data)

    def get_progress(self, obj):
        obj.progress = dict(utils.sqlProgressChoice).get(obj.progress)
        return obj.progress

    def to_representation(self, instance):
        ret = super(SqlOrdersListSerializer, self).to_representation(instance)
        ret["escape_title"] = instance.title
        ret["created_at"] = datetime.strftime(instance.created_at, "%Y-%m-%d %H:%M:%S")
        return ret


class SqlOrderDetailSerializer(serializers.ModelSerializer):
    # 获取choices字段
    env_id = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    host = serializers.ReadOnlyField(source='cid.host')
    port = serializers.ReadOnlyField(source='cid.port')

    class Meta:
        model = models.DbOrders
        fields = "__all__"

    def get_env_id(self, obj):
        obj.env_id = models.DbEnvironment.objects.get(pk=obj.env_id).name
        return obj.env_id

    def get_progress(self, obj):
        obj.progress = dict(utils.sqlProgressChoice).get(obj.progress)
        return obj.progress

    def to_representation(self, instance):
        ret = super(SqlOrderDetailSerializer, self).to_representation(instance)
        ret["created_at"] = datetime.strftime(instance.created_at, "%Y-%m-%d %H:%M:%S")
        return ret

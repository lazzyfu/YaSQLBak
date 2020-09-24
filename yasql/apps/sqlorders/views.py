# -*- coding:utf-8 -*-
# edit by fuzongfei
import datetime
# Create your views here.
import json

from django.http import Http404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from libs.Pagination import Pagination
from libs.RenderColumns import render_dynamic_columns
from libs.response import JsonResponseV1
from sqlorders import models, serializers
from sqlorders.filters import SqlOrderListFilter, GetTasksListFilter


class GetReleaseVersions(ListAPIView):
    queryset = models.ReleaseVersions.objects.all()
    serializer_class = serializers.ReleaseVersionsSerializer

    def get(self, request, *args, **kwargs):
        before_30_days = (timezone.now() - datetime.timedelta(days=30))
        queryset = self.get_queryset().filter(expire_time__gte=before_30_days).order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponseV1(data=serializer.data)


class GetDBEnvironment(ListAPIView):
    queryset = models.DbEnvironment.objects.all()
    serializer_class = serializers.DbEnvironmentSerializer

    # 获取工单环境
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return JsonResponseV1(data=serializer.data)


class GetDbSchemas(APIView):
    # 获取指定环境审核用途(use_type=0)的schemas列表
    def get(self, request):
        serializer = serializers.DbSchemasSerializer(data=request.query_params)
        if serializer.is_valid():
            return JsonResponseV1(data=serializer.query)
        return JsonResponseV1(message=serializer.errors, code='0001')


class IncepSyntaxCheckView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.IncepSyntaxCheckSerializer(data=request.data)

        if serializer.is_valid():
            s, data = serializer.check()
            render_columns = [
                {'key': 'order_id', 'value': '序号'},
                {'key': 'stage', 'value': '阶段'},
                {'key': 'stage_status', 'value': '阶段状态'},
                {'key': 'error_level', 'value': '错误级别'},
                {'key': 'error_message', 'value': '错误信息', 'width': '35%'},
                {'key': 'sql', 'value': 'SQL内容', 'width': '25%', 'ellipsis': True},
                {'key': 'affected_rows', 'value': '影响/扫描行数'}
            ]
            columns = render_dynamic_columns(render_columns)
            message = '语法检查未发现异常，可以提交'
            if not s:
                message = '语法检查发现异常，详情请查看输出，更正后在提交'
            d = {
                'status': 0 if s else 1,
                'data': data
            }
            data = {'columns': columns, 'data': d}
            return JsonResponseV1(data=data, message=message)
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class SqlOrdersCommit(GenericAPIView):
    serializer_class = serializers.SqlOrdersCommitSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(message="提交成功")
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class SqlOrdersList(ListAPIView):
    # permission_classes = (permissions.CanViewOrdersPermission,)
    queryset = models.DbOrders.objects.all()
    serializer_class = serializers.SqlOrdersListSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = SqlOrderListFilter
    ordering = ['-created_at']
    search_fields = ['title', 'database', 'remark', 'applicant', 'progress', 'contents']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        render_columns = [
            {'key': 'progress', 'value': '进度', 'width': '8%'},
            {'key': 'applicant', 'value': '申请人'},
            {'key': 'department', 'value': '部门'},
            {'key': 'env_name', 'value': '环境'},
            {'key': 'escape_title', 'value': '标题', 'width': '18%', 'ellipsis': True},
            {'key': 'sql_type', 'value': '类型'},
            {'key': 'remark', 'value': '备注'},
            {'key': 'version', 'value': '版本'},
            {'key': 'host', 'value': '实例/库'},
            {'key': 'auditor', 'value': '审核人'},
            {'key': 'reviewer', 'value': '复核人'},
        ]
        columns = render_dynamic_columns(render_columns)
        data = {'columns': columns, 'data': serializer.data}
        return self.get_paginated_response(data)


class SqlOrdersDetail(ListAPIView):
    """SQL工单详情"""
    # permission_classes = (permissions.CanViewOrdersPermission,)
    queryset = models.DbOrders.objects.all()
    serializer_class = serializers.SqlOrderDetailSerializer
    lookup_field = 'order_id'

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, context={"request": request})
        return JsonResponseV1(data=serializer.data)


class OpSqlOrderView(ViewSet):
    """更新SQL工单状态，如：审核，关闭等"""

    def get_obj(self, pk):
        try:
            obj = models.DbOrders.objects.get(pk=pk)
            return obj
        except models.DbOrders.DoesNotExist:
            raise Http404

    def approve(self, request, pk):
        serializer = serializers.OpSqlOrderSerializer(instance=self.get_obj(pk),
                                                      data=request.data,
                                                      context={"request": request, "handler": "_approve"})

        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(data=serializer.data, message="操作成功")
        return JsonResponseV1(message=serializer.errors, code='0001')

    def feedback(self, request, pk):
        serializer = serializers.OpSqlOrderSerializer(instance=self.get_obj(pk),
                                                      data=request.data,
                                                      context={"request": request, "handler": "_feedback"})
        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(data=serializer.data, message="操作成功")
        return JsonResponseV1(message=serializer.errors, code='0001')

    def close(self, request, pk):
        serializer = serializers.OpSqlOrderSerializer(instance=self.get_obj(pk),
                                                      data=request.data,
                                                      context={"request": request, "handler": "_close"})
        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(data=serializer.data, message="操作成功")
        return JsonResponseV1(message=serializer.errors, code='0001')

    def review(self, request, pk):
        serializer = serializers.OpSqlOrderSerializer(instance=self.get_obj(pk),
                                                      data=request.data,
                                                      context={"request": request, "handler": "_review"})
        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(data=serializer.data, message="操作成功")
        return JsonResponseV1(message=serializer.errors, code='0001')


class GenerateTasksView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.GenerateSqlOrdersTasksSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save(request)
            return JsonResponseV1(data=data)
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class GetTaskIdView(APIView):
    def get(self, request, *args, **kwargs):
        """根据order id返回taskid"""
        order_id = kwargs.get('order_id')
        task_id = models.DbOrdersExecuteTasks.objects.filter(order_id=order_id).first().task_id
        return JsonResponseV1(data=task_id)


class GetTasksPreviewView(ListAPIView):
    queryset = models.DbOrdersExecuteTasks.objects.all()
    serializer_class = serializers.SqlOrdersTasksListSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = GetTasksListFilter
    search_fields = ['sql']
    ordering = ['created_time']

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        queryset = self.filter_queryset(self.get_queryset().filter(task_id=task_id))

        # 数据隐藏按钮打开了
        # 仅允许申请人、审核人、复核人和超权用户查看数据
        obj = models.DbOrders.objects.get(
            pk=models.DbOrdersExecuteTasks.objects.filter(task_id=task_id).first().order_id
        )
        if obj.is_hide == 'ON' and not request.user.is_superuser:
            allowed_view_users = [obj.applicant]
            allowed_view_users.extend([x['user'] for x in json.loads(obj.auditor)])
            allowed_view_users.extend([x['user'] for x in json.loads(obj.reviewer)])
            if request.user.username not in allowed_view_users:
                raise PermissionDenied(detail='您没有权限查看该工单的数据，5s后，自动跳转到工单列表页面')

        origin_queryset = self.queryset.filter(task_id=task_id)
        total = origin_queryset.count()
        progress_0 = origin_queryset.filter(progress=0).count()
        progress_1 = origin_queryset.filter(progress=1).count()
        progress_3 = origin_queryset.filter(progress=3).count()

        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, context={'request': request}, many=True)
        render_columns = [
            {'key': 'num', 'value': '序号'},  # 自定义num，前台显示序号使用
            {'key': 'applicant', 'value': '申请人'},
            {'key': 'sql', 'value': 'SQL', 'ellipsis': True, 'width': '50%'},
            {'key': 'progress', 'value': '进度'},
            {'key': 'result', 'value': '查看结果'},  # 自定义result
        ]
        columns = render_dynamic_columns(render_columns)
        data = {'columns': columns,
                'data': {'data': serializer.data,
                         'total': total,
                         'progress_0': progress_0,
                         'progress_1': progress_1,
                         'progress_3': progress_3}}
        return self.get_paginated_response(data)


class GetTasksListView(ListAPIView):
    queryset = models.DbOrdersExecuteTasks.objects.all()
    serializer_class = serializers.SqlOrdersTasksListSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = GetTasksListFilter
    search_fields = ['sql']
    ordering = ['created_time']

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        queryset = self.filter_queryset(self.get_queryset().filter(task_id=task_id))

        # 数据隐藏按钮打开了
        # 仅允许申请人、审核人、复核人和超权用户查看数据
        obj = models.DbOrders.objects.get(
            pk=models.DbOrdersExecuteTasks.objects.filter(task_id=task_id).first().order_id
        )
        if obj.is_hide == 'ON' and not request.user.is_superuser:
            allowed_view_users = [obj.applicant]
            allowed_view_users.extend([x['user'] for x in json.loads(obj.auditor)])
            allowed_view_users.extend([x['user'] for x in json.loads(obj.reviewer)])
            if request.user.username not in allowed_view_users:
                raise PermissionDenied(detail='您没有权限查看该工单的数据，5s后，自动跳转到工单列表页面')

        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, context={'request': request}, many=True)
        render_columns = [
            {'key': 'num', 'value': '序号'},  # 自定义num，前台显示序号使用
            {'key': 'applicant', 'value': '申请人'},
            {'key': 'sql', 'value': 'SQL', 'ellipsis': True, 'width': '50%'},
            {'key': 'progress', 'value': '进度'},
            {'key': 'execute', 'value': '执行'},  # 自定义execute
            {'key': 'result', 'value': '查看结果'},  # 自定义result
        ]
        if queryset.exists():
            if queryset.first().sql_type == 'DDL':
                render_columns.insert(-1, {'key': 'ghost_pause', 'value': '暂停(gh-ost)'})
                render_columns.insert(-1, {'key': 'ghost_recovery', 'value': '恢复(gh-ost)'})
        columns = render_dynamic_columns(render_columns)
        data = {'columns': columns, 'data': serializer.data}
        return self.get_paginated_response(data)


class ExecuteSingleTaskView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ExecuteSingleTaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.execute(request)
            return JsonResponseV1(message="任务提交成功，请查看输出")
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class ExecuteMultiTasksView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ExecuteMultiTasksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.execute(request)
            return JsonResponseV1(message="任务提交成功，请查看输出")
        return JsonResponseV1(message=serializer.errors, code='0001', flat=False)


class ThrottleTaskView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ThrottleTaskSerializer(data=request.data)

        if serializer.is_valid():
            message = serializer.execute(request)
            return JsonResponseV1(message=message)
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class GetTasksResultView(ListAPIView):
    """SQL工单详情"""
    queryset = models.DbOrdersExecuteTasks.objects.all()
    serializer_class = serializers.GetTasksResultSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, context={"request": request})
        return JsonResponseV1(data=serializer.data)


class HookSqlOrdersView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.HookSqlOrdersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(message="任务提交成功，请查看输出")
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)
# -*- coding:utf-8 -*-
# edit by fuzongfei
import datetime

# Create your views here.
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView

from libs import permissions
from libs.Pagination import Pagination
from libs.RenderColumns import render_dynamic_columns
from libs.response import JsonResponseV1
from sqlorders import models, serializers
from sqlorders.filters import SqlOrderListFilter


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


class SqlOrdersCommit(GenericAPIView):
    serializer_class = serializers.SqlOrdersCommitSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponseV1(message="提交成功")
        return JsonResponseV1(message=serializer.errors, code='0001', flat=True)


class SqlOrdersList(ListAPIView):
    permission_classes = (permissions.CanViewOrdersPermission,)
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
            {'key': 'progress', 'value': '进度', 'width': '7%'},
            {'key': 'env_name', 'value': '环境', 'width': '10%'},
            {'key': 'escape_title', 'value': '标题', 'width': '18%', 'ellipsis': True},
            {'key': 'sql_type', 'value': '类型', 'width': '5%'},
            {'key': 'remark', 'value': '备注', 'width': '8%'},
            {'key': 'version', 'value': '版本', 'width': '8%'},
            {'key': 'host', 'value': '实例/库', 'width': '10%'},
            {'key': 'applicant', 'value': '申请人', 'width': '10%'},
            {'key': 'auditor', 'value': '审核人', 'width': '12%'},
            {'key': 'reviewer', 'value': '复核人', 'width': '12%'},
        ]
        columns = render_dynamic_columns(render_columns)
        data = {'columns': columns, 'data': serializer.data}
        return self.get_paginated_response(data)


class SqlOrdersDetail(ListAPIView):
    """SQL工单详情"""
    permission_classes = (permissions.CanViewOrdersPermission,)
    queryset = models.DbOrders.objects.all()
    serializer_class = serializers.SqlOrderDetailSerializer
    lookup_field = 'order_id'

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, context={"request": request})
        return JsonResponseV1(data=serializer.data)

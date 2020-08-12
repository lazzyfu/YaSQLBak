# Create your views here.
import json
from uuid import uuid4

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from libs.response import JsonResponseV1
from users import serializers, models


class LoginView(APIView):
    """登录"""
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid():
            code, data = serializer.login()
            if code:
                return JsonResponseV1(data={'token': data})
            return JsonResponseV1(message=data, code='0001')
        return JsonResponseV1(serializer.errors, code='0001')


class LogoutView(APIView):
    """退出登录"""

    def post(self, request, *args, **kwargs):
        user = request.user
        # 每次退出登录时，修改user_secret的值，即可实现token失效
        user.user_secret = uuid4()
        user.save()
        return JsonResponseV1(status=status.HTTP_200_OK)


class UserInfoView(APIView):
    """获取登录用户信息"""

    def get(self, request):
        user = serializers.UserInfoSerializer(request.user)
        return JsonResponseV1(data=user.data)


class GetUsersView(ListAPIView):
    queryset = models.UserAccounts.objects.all()
    serializer_class = serializers.UsersListSerializer

    # 获取审核、复核、抄送的用户列表
    def get(self, request,  *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponseV1(data=serializer.data)

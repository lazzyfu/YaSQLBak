# -*- coding:utf-8 -*-
# edit by fuzongfei
from django.urls import path

from users import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='v1.user_login'),
    path('logout', views.LogoutView.as_view(), name='v1.user_logout'),
    path('info', views.UserInfoView.as_view(), name='v1.user_info'),
    path('list', views.GetUsersView.as_view(), name='v1.get_users')
]

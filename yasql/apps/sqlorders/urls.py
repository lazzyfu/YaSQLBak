# -*- coding:utf-8 -*-
# edit by fuzongfei

from django.urls import path

from sqlorders import views

urlpatterns = [
    # SQL工单
    path('versions', views.GetReleaseVersions.as_view(), name='v1.sqlorders.release-versions'),
    path('envs', views.GetDBEnvironment.as_view(), name='v1.sqlorders.db-environment'),
    path('schemas', views.GetDbSchemas.as_view(), name='v1.sqlorders.db-schemas'),
    # path('incep/syntaxcheck', views.IncepSyntaxCheckView.as_view(), name='v1.dbms.incep.syntaxcheck'),
    path('commit', views.SqlOrdersCommit.as_view(), name='v1.sqlorders.commit'),
    path('list', views.SqlOrdersList.as_view(), name='v1.sqlorders.list'),
    path('detail/<str:order_id>', views.SqlOrdersDetail.as_view(), name='v1.sqlorders.detail'),
    # path('op/approve/<int:pk>', views.OpSqlOrderView.as_view({"put": "approve"}), name='v1.dbms.sqlorders.approve'),
    # path('op/feedback/<int:pk>', views.OpSqlOrderView.as_view({"put": "feedback"}), name='v1.dbms.sqlorders.feedback'),
    # path('op/close/<int:pk>', views.OpSqlOrderView.as_view({"put": "close"}), name='v1.dbms.sqlorders.close'),
    # path('op/review/<int:pk>', views.OpSqlOrderView.as_view({"put": "review"}), name='v1.dbms.sqlorders.review'),
    # # 生成工单任务
    # path('tasks/generate', views.GenerateTasksView.as_view(), name='v1.dbms.sqlorders.generate-tasks'),
    # path('tasks/list/<str:taskid>', views.GetTasksListView.as_view(), name='v1.dbms.sqlorders.get-tasks-list'),
    # # 执行任务
    # path('tasks/execute/single', views.ExecuteSingleTaskView.as_view(), name='v1.dbms.sqlorders.execute-single-task'),
    # path('tasks/execute/multi', views.ExecuteMultiTasksView.as_view(), name='v1.dbms.sqlorders.execute-multi-tasks'),
    # path('tasks/throttle', views.ThrottleTaskView.as_view(), name='v1.dbms.sqlorders.throttle-task'),
    # path('tasks/result/<int:id>', views.GetTasksResultView.as_view(), name='v1.dbms.sqlorders.get-tasks-result'),
    # # Hook
    # path('hook', views.HookSqlOrdersView.as_view(), name='v1.dbms.hook-sqlorders')
]

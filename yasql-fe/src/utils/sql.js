// SQL类型
export const SqlType = [
  { key: 'ddl', value: 'DDL工单' },
  { key: 'dml', value: 'DML工单' },
  { key: 'export', value: '导出工单' }
]

// DB类别
export const rdsCategory = [
  {'key': 1, 'value': 'mysql'},
  {'key': 2, 'value': 'tidb'},
]

export const SqlRemark = [
'立即执行',
'窗口执行',
'上线执行'
]

export const SqlTimeList = [
"10:00~11:00",
'14:00~15:00',
'17:00~18:00',
'21:00~23:00'
]

export const SqlOrderProgress = [
  {'key': 0, 'value': '待审核', 'color': 'warning'},
  {'key': 1, 'value': '已驳回', 'color': 'danger'},
  {'key': 2, 'value': '已批准', 'color': 'primary'},
  {'key': 3, 'value': '处理中', 'color': 'warning'},
  {'key': 4, 'value': '已完成', 'color': 'success'},
  {'key': 5, 'value': '已关闭', 'color': 'danger'},
  {'key': 6, 'value': '已复核', 'color': 'info'},
  {'key': 7, 'value': '已勾住', 'color': 'default'},
]

// 工单任务执行计划
export const executeProgress = [
  {'key': 0, 'value': '未执行'},
  {'key': 1, 'value': '已完成'},
  {'key': 2, 'value': '处理中'},
  {'key': 3, 'value': '失败'},
  {'key': 4, 'value': '异常'},
]
const route = {
  name: 'view.sqlorders',
  path: '/sqlorders',
  component: () => import('./index.vue'),
  redirect: {name: 'view.sqlorders.list'},
  meta: { title: 'DB工单', keepAlive: true, icon: 'database' },
  children: [
    {
      name: 'view.sqlorders.list',
      path: '/sqlorders/list',
      component: () => import('./list.vue'),
      meta: { title: '工单列表', keepAlive: true, icon: 'bars' }
    },
    {
      name: 'view.sqlorders.detail',
      path: '/sqlorders/detail/:order_id',
      hidden: true,
      component: () => import('./detail.vue'),
      meta: { title: '工单详情', keepAlive: true }
    },
    {
      name: 'view.sqlorders.commit.ddl',
      path: '/sqlorders/commit/ddl',
      component: () => import('./commit.vue'),
      meta: { title: '提交DDL工单', keepAlive: true, icon: 'bars' }
    },
    {
      name: 'view.sqlorders.commit.dml',
      path: '/sqlorders/commit/dml',
      component: () => import('./commit.vue'),
      meta: { title: '提交DML工单', keepAlive: true, icon: 'bars' }
    },
    {
      name: 'view.sqlorders.commit.export',
      path: '/sqlorders/commit/export',
      component: () => import('./commit.vue'),
      meta: { title: '提交导出工单', keepAlive: true, icon: 'bars' }
    },
    

    // {
    //   name: "view.sqlorders.tasks.list",
    //   path: "tasks/list/:taskid",
    //   component: () => import("./SqlOrders/tasks/index.vue"),
    //   meta: { title: "工单任务", hidden: true }
    // }
  ]
}

export default route

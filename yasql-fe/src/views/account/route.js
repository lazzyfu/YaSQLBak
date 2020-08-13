const route = {
    path: 'account',
    name: 'account',
    component: () => import('./settings/BaseSetting'),
    meta: { title: '个人页', icon: 'user', keepAlive: false }
  }
  
  export default route
  
const route = [
    {
      path: '404',
      component: () => import('./404.vue')
    },
    {
      path: '403',
      component: () => import('./403.vue')
    },
    {
      path: '500',
      component: () => import('./500.vue')
    },
  ]
  
  export default route
  
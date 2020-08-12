// eslint-disable-next-line
import { UserLayout, BasicLayout } from '@/layouts'
import SqlOrders from '@/views/sqlorders/route'

export const asyncRouterMap = [
  {
    path: '/',
    name: 'menu.home',
    component: BasicLayout,
    redirect: {'name': 'account'},
    children: [
      // account
      {
        path: 'account',
        component: () => import('@/views/account/settings/BaseSetting'),
        name: 'account',
        meta: { title: '个人页', icon: 'user', keepAlive: true }
      },
      SqlOrders,
    ]
  },
  {
    path: '*',
    redirect: { name: 'menu.home' }
  }
]

/**
 * 基础路由
 * @type { *[] }
 */
export const constantRouterMap = [
  {
    path: '/user',
    component: UserLayout,
    redirect: '/user/login',
    hidden: true,
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import(/* webpackChunkName: "user" */ '@/views/user/Login')
      }
    ]
  },
  {
    name: '404',
    path: '/404',
    component: () => import('@/views/exception/404.vue')
  },
  {
    name: '403',
    path: '/403',
    component: () => import('@/views/exception/403.vue')
  },
  {
    name: '500',
    path: '/500',
    component: () => import('@/views/exception/500.vue')
  }
]

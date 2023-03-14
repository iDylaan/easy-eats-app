import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Loged from '../views/LogedView.vue'
import HeaderVue from '@/components/home/Header.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/loged',
    name: 'loged',
    component: Loged
  },
  {
    path: '/header',
    name: 'header',
    component: Header
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

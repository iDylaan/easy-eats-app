import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Signin from '../views/SigninView.vue'
import Loged from '../views/LogedView.vue'
import Lucero from '../views/LuceroView.vue'

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
    path: '/signin',
    name: 'signin',
    component: Signin
  },
  {
    path: '/loged',
    name: 'loged',
    component: Loged
  },
  {
    path: '/lucero',
    name: 'lucero',
    component: Lucero
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

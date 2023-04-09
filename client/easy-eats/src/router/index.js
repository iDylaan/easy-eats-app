import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Loged from '../views/LogedView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login-SigninPages/LoginView.vue')
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import('@/views/Login-SigninPages/SigninView.vue')
  },
  {
    path: '/loged',
    name: 'loged',
    component: Loged
  },
  {
    path: '/nosotros',
    name: 'nosotros',
    component: () => import('@/views/NosotrosView.vue')
  },
  {
    path: '/nueva-receta',
    name: 'NuevaReceta',
    component: () => import('@/views/Recetas/NuevaRecetaView.vue')
  },
  {
    path: '/detallesPerfil',
    name: 'detallesPerfil',
    component: () => import('@/views/perfil/DetallesView.vue')
  },
  {
    path: '/fromPerfil',
    name: 'fromPerfil',
    component: () => import('@/views/perfil/FromPerfil.vue')
  },
  {
    path: '/recetas',
    name: 'recetas',
    component: () => import('@/views/RecetasView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

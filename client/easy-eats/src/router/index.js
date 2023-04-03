import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Loged from '../views/LogedView.vue'
import Nosotros from '../views/NosotrosView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login-SigninPages/LoginView.vue')
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import('../views/Login-SigninPages/SigninView.vue')
  },
  {
    path: '/loged',
    name: 'loged',
    component: Loged
  },
  {
    path: '/nosotros',
    name: 'nosotros',
<<<<<<< HEAD
    component: () => import('../views/NosotrosView.vue')
=======
    component: () => import('@/views/NosotrosView.vue')
  },
  {
    path: '/nueva-receta',
    name: 'NuevaReceta',
    component: () => import('@/views/Recetas/NuevaRecetaView.vue')
>>>>>>> 4aaad6c7d72b656971c0530cfd4afb8d12cb99b3
  },
  {
    path: '/detallesPerfil',
    name: 'detallesPerfil',
    component: () => import('../views/perfil/DetallesView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

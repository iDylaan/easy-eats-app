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
    component: () => import('../views/NosotrosView.vue')
  },
  {
    path: '/detallesPerfil',
    name: 'detallesPerfil',
    component: () => import('../views/perfil/DetallesView.vue')
  },
  {
    path: '/fromPerfil',
    name: 'fromPerfil',
    component: () => import('../views/perfil/FromPerfil.vue')
  },
  {
    path: '/actualizarFoto',
    name: 'actualizarFoto',
    component: () => import('../views/perfil/ActualizarFoto.vue')
  },
  {
    path: '/recetas',
    name: 'recetas',
    component: () => import('../views/RecetasView.vue')
  },
  {
    path: '/detallesRecetas',
    name: 'detsallesRecetas',
    component: () => import('../views/recetas/DetallesRecetas.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

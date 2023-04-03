import { createRouter, createWebHistory } from 'vue-router'

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
    component: () => import('@/views/LogedView.vue')
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
    component: () => import('../views/perfil/DetallesView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

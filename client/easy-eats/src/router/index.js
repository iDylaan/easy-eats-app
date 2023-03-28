import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Signin from '../views/SigninView.vue'
import Loged from '../views/LogedView.vue'
import Nosotros from '../views/Nosotros.vue'
import recetasCategoria from '../views/RecetasCatView.vue' 


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
    path: '/nosotros',
    name: 'nosotros',
    component: Nosotros
  },
  {
    path: '/preferencias',
    name: 'preferencias',
    component: () => import('../views/PreferenciasView.vue')
  },
  {
    path: '/subir-receta',
    name: 'subir-receta',
    component: () => import('../views/SubirRecetaView.vue')
  },
  {
    path: '/recetasCategoria',
    name: 'recetasCategoria',
    component: () => import('../views/RecetasCatView.vue')
  },
  {
    path: '/detallesPasos',
    name: 'detallesPasos',
    component: () => import('../views/DetallesPasosView.vue')
  },
  {
    path: '/reviewComments',
    name: 'reviewComments',
    component: () => import('../views/ReviewCommentsView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

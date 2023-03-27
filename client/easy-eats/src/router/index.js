import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Signin from '../views/SigninView.vue'
import Loged from '../views/LogedView.vue'
import Preferencias from '../views/PreferenciasView.vue'
import SubirRecetas from '../views/SubirRecetaView.vue' 
import RecetasCategoria from '../views/RecetasCatView.vue'

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
    path: '/preferencias',
    name: 'preferencias',
    component: Preferencias
  },
  {
    path: '/subirReceta',
    name: 'subirReceta',
    component: SubirRecetas
  },
  {
    path: '/recetasCategoria',
    name: 'recetasCategoria',
    component: RecetasCategoria
  } 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

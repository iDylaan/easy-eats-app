import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Login from '../views/LoginView.vue'
import Signin from '../views/SigninView.vue'
import Nosotros from '../views/Nosotros.vue'

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
    path: '/nosotros',
    name: 'nosotros',
    component: Nosotros
  },
  {
    path: '/editar-perfil',
    name: 'editar-perfil',
    component: () => import('../views/EditPerfil.vue')
  },
  {
  path:'/users',
  name: 'crudusers',
  component: () => import('../views/CrudUsersView.vue')
  },
  {
    path:'/coments',
    name: 'coments',
    component: () => import('../views/ComentsView.vue')
    },
    {
      path:'/favorites',
      name: 'favorites',
      component: () => import('../views/FavoritesRecepitesView.vue')
      },
      {
        path:'/ingredients',
        name: 'ingredients',
        component: () => import('../views/IngredientsCrud.vue')
        },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

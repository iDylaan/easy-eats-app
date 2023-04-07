import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Loged from '../views/LogedView.vue'
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
    path: '/recetas-categoria',
    name: 'rectCat',
    component: () => import('../views/RecetasCatView.vue')
  },

  {
    path: '/crudingredients',
    name: 'crud-ingredientes',
    component: () => import('../views/IngredientsCrud.vue')
  },
  {
    path: '/editar-perfil',
    name: 'editar-perfil',
    component: () => import('../views/EditPerfil.vue')
  },
  {
    path: '/users',
    name: 'crudusers',
    component: () => import('../views/CrudUsersView.vue')
  },
  {
    path: '/coments',
    name: 'coments',
    component: () => import('../views/ComentsView.vue')
  },
  {
    path: '/ingredients',
    name: 'ingredients',
    component: () => import('../views/IngredientsCrud.vue')
  },
 
  {
    path: '/agreingre',
    name: 'agregar-ingredientes',
    component: () => import('../views/AgregarIngrediente.vue')
  },
  {
    path: '/editingre',
    name: 'editar-ingredientes',
    component: () => import('../views/EditarIngrediente.vue')
  },
  {
    path: '/deleteingre',
    name: 'eliminar-ingredientes',
    component: () => import('../views/BorrarIngrediente.vue')
  },
  {
    path: '/editusers',
    name: 'editar-usuario',
    component: () => import('../views/EditUsers.vue')
  },
  {
    path: '/agregaringre',
    name: 'agregar-ingrediente',
    component: () => import('../views/AgregarIngrediente.vue')
  },
  {
    path: '/deleteuser',
    name: 'eliminar-usuario',
    component: () => import('../views/EliminarUsuario.vue')
  },
  {
    path: '/agregarusers',
    name: 'agregar-usuario',
    component: () => import('../views/AgregarUsuario.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

import { createRouter, createWebHistory } from 'vue-router'
import Signup from '../components/Signup.vue'
import Login from '../components/Login.vue'
import CreateTopoBoard from '../components/CreateTopoBoard.vue'
import StudioTopoBoard from '../components/StudioTopoBoard.vue'
import PublicBoardView from '../components/PublicBoardView.vue'
import Dashboard from '../components/Dashboard.vue'

const routes = [
  { path: '/', redirect: '/signup' },
  { path: '/signup', name: 'Signup', component: Signup },
  { path: '/login', name: 'Login', component: Login },
  { path: '/create-topoboard', name: 'CreateTopoBoard', component: CreateTopoBoard },
  { path: '/studio', name: 'StudioTopoBoard', component: StudioTopoBoard },
  { path: '/board/:id', name: 'PublicBoardView', component: PublicBoardView },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

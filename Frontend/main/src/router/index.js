import { createRouter, createWebHistory } from 'vue-router'
import WelcomeView from '../views/WelcomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'welcome',
    component: WelcomeView,
    meta: {title:"Mentor's Portal"}
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: {title:"Register"}
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: {title:"Login"}
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: {title:"Dashboard"}
  },
]

const router = createRouter({
  mode:'history',
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to,from,next)=>{
  document.title=`${to.meta.title}`;
  next()
});
export default router

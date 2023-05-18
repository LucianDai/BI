import Vue from 'vue'
import VueRouter from 'vue-router'
import ScreenPage from '@/views/ScreenPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/screen',
  },
  {
    path: '/screen',
    component: ScreenPage,
    query: {
      company1: '',
      company2: ''
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

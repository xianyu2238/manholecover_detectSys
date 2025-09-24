import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'log',
    component: ()=>import("../views/logIndex.vue")
  },
  {
    path: '/manager',
    name: 'home',
    component: ()=>import("../views/IndexData.vue")
  },
  {
    path: '/fix',
    name: 'fix',
    component: ()=>import("../views/fixView.vue")
  },
]

const router = new VueRouter({
  routes
})

export default router
